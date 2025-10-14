class GraphFilterError(Exception):
    """Filter on graph produced undesired result"""

    pass


class MissingDimensionVector(Exception):
    """Unit is missing `hasDimensionVector` attribute"""

    pass


class QUDTLoaderHTTPError(Exception):
    """HTTP error occurred during QUDTLoader request"""

    def __init__(self, message: str, status_code: int, response_text: str = ""):
        self.status_code = status_code
        self.response_text = response_text
        super().__init__(message)
