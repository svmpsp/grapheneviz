"""CLI module docstring."""
import argparse
import logging
from typing import Any, Dict


def configure_logging(config: Dict[str, Any]):
    """Configures logging."""
    logging.basicConfig(level=config["log_level"])


def parse_config():
    """Parses CLI arguments."""
    print(argparse)
    return {"log_level": "INFO"}


def main():
    """Main application entrypoint."""
    conf = parse_config()
    configure_logging(conf)
    print("Hello world!")


if __name__ == "__main__":
    main()
