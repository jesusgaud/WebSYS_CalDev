# pylint: disable=duplicate-code
from app.plugins.greet.greet import GreetCommand  # Ensure correct import path

def test_greet_command_output():
    """Test the greet command returns expected output."""
    greet_command = GreetCommand()
    result = greet_command.execute()  # Capture the output
    assert result == "Hello, welcome to the interactive calculator!"
