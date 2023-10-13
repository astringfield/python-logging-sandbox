import logging

# Use the logger from the main script (main.py)
logger = logging.getLogger(__name__)

def log_something():

    # Log a message
    logger.info("This log message will be captured and written to 'captured_logs.log'")
    logger.debug("Module one debug log")
    logger.warning("Module one warning log")

    local_logger = logging.getLogger("local_method")
    local_logger.warning("Now lets try testing out another logger")