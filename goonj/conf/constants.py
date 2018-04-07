from enum import Enum

DEFAULT_CONFIG_FILE_PATH = "/var/tmp/goonj.yml"

DEFAULT_IMPORT_PATHS = '.'

DEFAULT_APP_ID = 'DefaultApp'


class Sev(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


SEV_VALUES = [Sev.LOW.value, Sev.MEDIUM.value,
              Sev.HIGH.value, Sev.CRITICAL.value]

CHANNEL_SLACK = "slack_channels"
CHANNEL_SMS = "sms_channels"
CHANNEL_EMAIL = "email_channels"
CHANNEL_LOGGER = "logger_channels"
