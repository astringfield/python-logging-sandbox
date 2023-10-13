import os
import logging
import logging.config
import yaml

# Import the module
from module_one import module_one
import module_two

# Create logging config from the .ini file
# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)

# Create logging config from the .yml file
with open("logging.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
logging.config.dictConfig(config)

# # Running the basic config will override all config set by above by the files/dictionaries
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(name)-24s: %(levelname)-8s %(message)s",
#     # handlers=[logging.FileHandler(logging_filename), logging.StreamHandler()],
# )

# Create a named logger for this main module
logger = logging.getLogger(__name__)
logger.info("Testing out some logging from a main module")

# Use the logger from the imported modules
module_one.log_something()
module_two.log_something()
new_inst = module_two.ClassOne()