from __future__ import annotations

import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = "my-railways"
    environment: str = "development"
    log_level: str = "INFO"
    device_platform: str = "android"
    mcp_transport: str = "stdio"
    api_base_url: str = "http://localhost:8000"
    mobile_api_timeout: int = 30

    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", self.app_name)
        self.environment = os.getenv("ENVIRONMENT", self.environment)
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)
        self.device_platform = os.getenv("DEVICE_PLATFORM", self.device_platform)
        self.mcp_transport = os.getenv("MCP_TRANSPORT", self.mcp_transport)
        self.api_base_url = os.getenv("API_BASE_URL", self.api_base_url)
        self.mobile_api_timeout = int(os.getenv("MOBILE_API_TIMEOUT", self.mobile_api_timeout))
