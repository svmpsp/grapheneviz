import argparse
import logging
from typing import Dict, Any


def configure_logging(config: Dict[str, Any]):
    logging.basicConfig(level=config["log_level"])


def parse_config():
    return {
        "log_level": "INFO"
    }

if __name__ == "__main__":
    config = parse_config()
    configure_logging(config)
    print("Hello world!")