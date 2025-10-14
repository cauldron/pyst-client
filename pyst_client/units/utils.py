import json
import re
from pathlib import Path
from typing import TextIO
from zipfile import ZipFile
from urllib.parse import quote_plus, urljoin
from pprint import pprint

import httpx
import requests
import structlog
from platformdirs import user_data_dir
from rdflib import Graph, Literal

from pyst_client.units.errors import GraphFilterError, QUDTLoaderHTTPError

logger = structlog.get_logger("sentier_vocab")
transport = httpx.AsyncHTTPTransport(retries=5)

DEFAULT_DATA_DIR = Path(user_data_dir("sentier.dev", "dds"))
DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_filename(response: requests.Response, url: str) -> str:
    """
    Get filename from response headers or URL.
    """
    if "Content-Disposition" in response.headers.keys():
        filename = re.findall("filename=(.+)", response.headers["Content-Disposition"])[
            0
        ]
    else:
        filename = url.split("/")[-1]
    if filename[0] in "'\"":
        filename = filename[1:]
    if filename[-1] in "'\"":
        filename = filename[:-1]
    if not filename:
        raise ValueError("Can't determine suitable filename")
    return filename


def streaming_download(
    url: str,
    filename: str | None = None,
    dirpath: Path | None = None,
    chunk_size: int = 4096 * 8,
) -> Path:
    """
    Download file from URL.

    Parameters
    ----------
    url : str
        URL to download from.
    filename : str, optional
        Filename to save to. If not given, will be determined from URL.
    dirpath : Path, optional
        Directory to save to. If not given, will be current working directory.
    chunk_size : int, optional
        Chunk size to use when downloading.

    Returns
    -------
    pathlib.Path
        Path to downloaded file.
    """
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise ValueError(f"URL {url} returns status code {response.status_code}")

    total_length = response.headers.get("content-length")
    filename = filename or get_filename(response, url)
    dirpath = Path(dirpath) if dirpath else Path(DEFAULT_DATA_DIR)
    dirpath.mkdir(parents=True, exist_ok=True)
    filepath = dirpath / filename

    with open(filepath, "wb") as f:
        logger.info(f"Downloading {filename} to {filepath}")
        if not total_length:
            f.write(response.content)
        else:
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)

    return filepath


def get_one_in_graph(graph: Graph, criteria: tuple) -> tuple:
    candidates = list(graph.triples(criteria))
    if len(candidates) == 1:
        return candidates[0]
    else:
        ERROR = f"""
Given criteria produced {len(candidates)} results; needed exactly 1.
Criteria: {criteria}"""
        if candidates:
            ERROR += "\n\t" + "\n\t".join(str(line) for line in candidates)
        raise GraphFilterError(ERROR)


def get_latest_github_file_from_release(
    repo_url: str, filepath: str, data_dir: Path = DEFAULT_DATA_DIR
) -> TextIO:
    return GithubZipfileRelease(
        repo_url=repo_url, data_dir=data_dir
    ).get_file_in_archive(filepath)


class GithubZipfileRelease:
    def __init__(self, repo_url: str, data_dir: Path = DEFAULT_DATA_DIR) -> None:
        if repo_url.endswith("/"):
            repo_url = repo_url[:-1]
        self.zipball_url = self.get_zipball_url(repo_url)
        self.catalogue_filepath = data_dir / f"{repo_url.split("/")[-1]}.json"
        self.zip_archive = ZipFile(
            open(
                self.get_latest_version(
                    data_dir=data_dir,
                    catalogue_filepath=self.catalogue_filepath,
                    zipball_url=self.zipball_url,
                ),
                "rb",
            )
        )
        self.zipfile_prefix = self.get_zipfile_prefix()

    def get_zipball_url(self, repo_url: str) -> str:
        if not repo_url.startswith("https://github.com/"):
            raise ValueError(
                "`repo_url` must be a Github repository and start with 'https://github.com/'"
            )
        if repo_url.count("/") != 4:
            raise ValueError(
                "`repo_url` must have form 'https://github.com/<something>/<something>' with four '/' characters"
            )
        return requests.get(
            f"https://api.github.com/repos/{repo_url.replace("https://github.com/", "")}/releases/latest"
        ).json()["zipball_url"]

    def get_latest_version(
        self, data_dir: Path, catalogue_filepath: Path, zipball_url: str
    ) -> Path:
        try:
            catalogue = json.load(open(catalogue_filepath))
        except (OSError,):
            catalogue = {}
        if catalogue.get("release") != zipball_url:
            fp = streaming_download(zipball_url, dirpath=data_dir)
            with open(catalogue_filepath, "w") as f:
                json.dump({"release": zipball_url, "filepath": str(fp)}, f, indent=2)
            return fp
        return catalogue["filepath"]

    def get_zipfile_prefix(self) -> str:
        prefix = set()

        for zipinfo in self.zip_archive.infolist():
            prefix.add(zipinfo.filename.split("/")[0])

        assert len(prefix) == 1
        return prefix.pop()

    def get_file_in_archive(self, path: str) -> TextIO:
        for zipinfo in self.zip_archive.infolist():
            if zipinfo.filename.startswith(self.zipfile_prefix + path):
                return self.zip_archive.open(zipinfo.filename)
        raise KeyError


def get_file_in_downloadable_zip_archive(
    url: str, path: str, data_dir: Path = DEFAULT_DATA_DIR
) -> TextIO:
    zip_archive = ZipFile(
        open(
            streaming_download(url, dirpath=data_dir),
            "rb",
        )
    )
    for zipinfo in zip_archive.infolist():
        if zipinfo.filename.startswith(path):
            return zip_archive.open(zipinfo.filename)
    raise KeyError


def to_untyped_literal(typed_literal: Literal) -> Literal:
    """
    Transform a typed RDFLib Literal to an untyped Literal.

    This function removes the datatype from a typed Literal while preserving
    the value and language tag (if present).

    Args:
        typed_literal: An RDFLib Literal that may have a datatype

    Returns:
        A new untyped Literal with the same value and language tag

    Examples:
        >>> from rdflib import Literal
        >>> from rdflib.namespace import XSD
        >>>
        >>> # Typed literal
        >>> typed = Literal("42", datatype=XSD.integer)
        >>> untyped = to_untyped_literal(typed)
        >>> print(untyped)  # "42"
        >>> print(untyped.datatype)  # None
        >>>
        >>> # Language-tagged literal
        >>> lang_typed = Literal("hello", lang="en", datatype=XSD.string)
        >>> lang_untyped = to_untyped_literal(lang_typed)
        >>> print(lang_untyped)  # "hello"@en
        >>> print(lang_untyped.datatype)  # None
        >>> print(lang_untyped.language)  # "en"
    """
    if not isinstance(typed_literal, Literal):
        raise TypeError(f"Expected Literal, got {type(typed_literal)}")

    # Extract the value
    value = str(typed_literal)

    # Preserve language tag if present
    if typed_literal.language:
        return Literal(value, lang=typed_literal.language)
    else:
        return Literal(value)


async def async_request(
    url_component: str, data: bytes, host: str, api_key: str, url_iri: str | None = None, ignore_422_errors: bool = False
) -> httpx.Response:
    async with httpx.AsyncClient(transport=transport) as client:
        if not isinstance(data, bytes):
            raise TypeError

        response = await client.post(
            urljoin(host, url_component + quote_plus(url_iri or "")),
            headers={
                "X-PyST-Auth-Token": api_key,
                "Content-Type": "application/json",
            },
            content=data,
        )

        # Check for HTTP errors, but don't raise on 409 Conflict (duplicate resource)
        # Optionally ignore 422 Unprocessable Entity based on flag
        ignored_codes = {409}
        if ignore_422_errors:
            ignored_codes.add(422)

        if response.status_code >= 400 and response.status_code not in ignored_codes:
            try:
                response_text = response.text
            except Exception:
                response_text = "Unable to decode response text"

            error_message = (
                f"HTTP request failed with status {response.status_code}"
            )
            if url_iri:
                error_message += f" for resource: {url_iri}"

            pprint(response.json())
            raise QUDTLoaderHTTPError(
                message=error_message,
                status_code=response.status_code,
                response_text=response_text,
            )

    return response
