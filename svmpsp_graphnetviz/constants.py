"""Constants and magic numbers."""

CLI_HELP_PROGRAM_NAME = "GNV"
CLI_HELP_DESCRIPTION = "A network generation and visualization tool"

DEFAULT_LOG_DATE_FORMAT = "%Y-%m-%d %H:%M"
DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)-5s %(filename)s:%(lineno)d - %(message)s"
DEFAULT_NETWORK_NODES = 16
DEFAULT_NETWORK_TYPE = "complete"

NETWORK_TYPES = [
    "barabasi-albert",
    "complete",
    "erdos-renyi",
    "random",
]
