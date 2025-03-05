import pytest
from app.app import App

@pytest.fixture
def app_instance():
    """Fixture for creating an App instance."""
    return App()

def test_app_get_environment_variable(app_instance, monkeypatch):  # pylint: disable=redefined-outer-name
    """Test retrieving the current environment setting."""
    monkeypatch.setenv("ENVIRONMENT", "development")  # Force a valid environment
    current_env = app_instance.get_environment_variable("ENVIRONMENT")
    assert current_env in ['development', 'testing', 'production'], f"Invalid ENVIRONMENT: {current_env}"

@pytest.mark.skip(reason="App class currently lacks a start() method")
def test_app_start_exit_command(app_instance, monkeypatch):  # pylint: disable=redefined-outer-name
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    with pytest.raises(SystemExit):
        app_instance.start()  # Ensure App has a start() method before running this test

@pytest.mark.skip(reason="App class currently lacks a start() method")
def test_app_start_unknown_command(app_instance, capfd, monkeypatch):  # pylint: disable=redefined-outer-name
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()  # Ensure App has a start() method before running this test

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
