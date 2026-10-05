from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

from src.config import Settings
from src.logger import get_logger
from src.device_manager import DeviceManager

load_dotenv()

def main() -> None:
    settings = Settings()
    logger = get_logger("main.devices")
    logger.info("Starting My Railways orchestration")

    manager = DeviceManager(settings)
    devices = manager.list_devices()

    if not devices:
        logger.warning("No devices detected")
        return

    for device in devices:
        logger.info("Device discovered: %s", device)

if __name__ == "__main__":
    main()
