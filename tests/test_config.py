from src.config import Settings

def test_settings_defaults():
    settings = Settings()
    assert settings.app_name == "my-railways"
    assert settings.environment == "development"
    assert settings.device_platform == "android"
