import importlib


def test_settings_loaded_root_env_path():
    from config.settings import settings

    assert settings.root_env_path.name == ".env"
    assert settings.root_env_path.parent == settings.slot_root


def test_process_env_overrides_dotenv(monkeypatch):
    monkeypatch.setenv("SLACK_ALERTS_ENABLED", "true")
    import config.settings as settings_module

    reloaded = importlib.reload(settings_module)
    try:
        assert reloaded.settings.slack_alerts_enabled is True
    finally:
        importlib.reload(settings_module)

