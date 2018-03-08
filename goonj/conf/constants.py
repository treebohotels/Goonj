from enum import Enum

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/goonj.yml"

TARK_LOGGER_PREFIX = "goonj"

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/goonj.yaml"
DEFAULT_IMPORT_PATHS = '.'

DEFAULT_APP_ID = 'DefaultApp'


class Sev(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
