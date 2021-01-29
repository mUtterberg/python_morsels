from typing import Any


# def alias(in_attr: str) -> Any:
#     """Helper utility to make classes with alias attributes"""
#     return


class DataRecord:
    """Dev helper"""
    # title = alias('serial')

    def __init__(self, serial: Any) -> None:
        self.serial = serial
