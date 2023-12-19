"""CLI module docstring."""
import argparse
import logging

from .adt import AppConfig
from .constants import (
    CLI_HELP_DESCRIPTION,
    CLI_HELP_PROGRAM_NAME,
    DEFAULT_LOG_DATE_FORMAT,
    DEFAULT_LOG_FORMAT,
    DEFAULT_NETWORK_NODES,
    DEFAULT_NETWORK_TYPE,
    NETWORK_TYPES,
)
from .generate import generate_network


def configure_logging(config: AppConfig):
    """Configures logging.

    :param config: application configuration.
    :type config: AppConfig
    """
    logging.basicConfig(
        level=config.log_level,
        format=DEFAULT_LOG_FORMAT,
        datefmt=DEFAULT_LOG_DATE_FORMAT,
    )


def parse_config() -> AppConfig:
    """Parses command line parameters.

    :return: parsed parameters
    :rtype: AppConfig
    """
    parser = argparse.ArgumentParser(
        prog=CLI_HELP_PROGRAM_NAME,
        description=CLI_HELP_DESCRIPTION,
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        dest="log_level",
        help="Number of network nodes.",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--nodes",
        default=DEFAULT_NETWORK_NODES,
        dest="nodes",
        help="Number of network nodes.",
        type=int,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./gnv_output",
        dest="output_file",
        help="Output file to store the generated data.",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=NETWORK_TYPES,
        default=DEFAULT_NETWORK_TYPE,
        dest="network_type",
        help="Type of network to be generated.",
        type=str,
    )
    return parser.parse_args()


def entrypoint():
    """Main application entrypoint."""
    conf = parse_config()
    configure_logging(conf)

    generate_network(conf)
