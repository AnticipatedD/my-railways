from __future__ import annotations

from typing import List, Dict, Any

from src.config import Settings
from src.logger import get_logger

class DeviceManager:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = get_logger("src.device_manager")

    def list_devices(self) -> List[Dict[str, Any]]:
        self.logger.info("Enumerating devices for platform: %s", self.settings.device_platform)
        return [
            {
                "platform": self.settings.device_platform,
                "device_id": "demo-device-001",
                "status": "online",
            }
        ]
