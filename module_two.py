import logging

# Running the basic config will override any previous logging configurations 
#   set at the module level (i.e. in any other calling modules)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')

# Create a named logger for this module
logger = logging.getLogger(__name__)

logger.warning("This message should be printed whenever 'module_two' is imported "
               "and should have no log formatting/handlers applied to it")

def log_something():
    # These log messages should all be propagated to any console/file 
    #   handlers designated by the calling module
    logger.info("This log message will be captured and written to 'captured_logs.log'")
    logger.debug("Module two debug log")
    logger.warning("Module two warning log")


class ClassOne:
    def __init__(self) -> None:
        logger.warning("Warning log within module_two.ClassOne")