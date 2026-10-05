import logging

from src.logger import get_logger

def test_logger_returns_logger():
    logger = get_logger("tests.logger")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "tests.logger"
