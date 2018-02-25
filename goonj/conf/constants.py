from goonj.models.constants import DatabaseType

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/goonj.yml"

TARK_LOGGER_PREFIX = "goonj"

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/goonj.yaml"
DEFAULT_IMPORT_PATHS = '.'

DEFAULT_APP_ID = 'DefaultApp'
DEFAULT_DB_TYPE = DatabaseType.POSTGRESQL_DATABASE
DEFAULT_DB_NAME = 'goonj'
DEFAULT_DB_USER = 'root'
DEFAULT_DB_PASSWORD = ''
DEFAULT_DB_HOST = 'localhost'

SEV = {
    "LOW": "low",
    "MEDIUM": "medium",
    "HIGH": "high",
    "CRITICAL": "critical"
}
