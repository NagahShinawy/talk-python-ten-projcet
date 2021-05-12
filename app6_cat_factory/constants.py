"""
created by Nagaj at 12/05/2021
"""

# ###########   CATS  ##########################

OUTPUT_FOLDER = "CATS"
APPNAME = "CAT FACTORY APP"
CAT_COUNTS = 8
CAT_NAME = "lolcat{i}"

# ###############  SERVICE  ###################

CATS_URL = (
    "http://consuming-python-services-api.azurewebsites.net/cats/random/"
)

# ###########  commands #######################
WINDOWS = "Windows"
WINDOWS_COMMAND = "explorer"

LINUX = "Linux"
LINUX_COMMAND = "xdg-open"

MACOS = "Darwin"
MACOS_COMMAND = "open"


# ###########  messages ##########################
CREATE_FOLDER = "CREATING NEW FOLDER AT '{}'"
NOT_SUPPORTED = "Don't Support Your OS '{}'"
DOWNLOAD = "Downloading Cat: {}"
DISPLAY = "Displaying Cats"