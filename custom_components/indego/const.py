"""Constants for Indego integration."""
from typing import Final

DOMAIN: Final = "indego"

DATA_UPDATED: Final = f"{DOMAIN}_data_updated"

CONF_ATTR: Final = "attributes"
CONF_SEND_COMMAND: Final = "command"
CONF_SMARTMOWING: Final = "enable"
CONF_POLLING: Final = "polling"

DEFAULT_NAME: Final = "Indego"
DEFAULT_NAME_COMMANDS: Final = None

SERVICE_NAME_COMMAND: Final = "command"
SERVICE_NAME_SMARTMOW: Final = "smartmowing"

SENSOR_TYPE: Final = "sensor"
BINARY_SENSOR_TYPE: Final = "binary_sensor"
INDEGO_PLATFORMS: Final = [SENSOR_TYPE, BINARY_SENSOR_TYPE]

ENTITY_ONLINE: Final = "online"
ENTITY_UPDATE_AVAILABLE: Final = "update_available"
ENTITY_ALERT: Final = "alert"
ENTITY_MOWER_STATE: Final = "mower_state"
ENTITY_MOWER_STATE_DETAIL: Final = "mower_state_detail"
ENTITY_BATTERY: Final = "battery_percentage"
ENTITY_LAWN_MOWED: Final = "lawn_mowed"
ENTITY_LAST_COMPLETED: Final = "last_completed"
ENTITY_NEXT_MOW: Final = "next_mow"
ENTITY_MOWING_MODE: Final = "mowing_mode"
ENTITY_RUNTIME: Final = "runtime_total"
ENTITY_MOWER_ALERT: Final = "mower_alert"
