import pytest
from temporalio.testing import ActivityEnvironment

from ..activities import (  # Adjust the import as per your directory structure
    ComposeGreetingInput, compose_greeting)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input, expected_output",
    [
        (ComposeGreetingInput(greeting="Hello", name="Alice"), "Hello, Alice!"),
        (ComposeGreetingInput(greeting="Hi", name="Bob"), "Hi, Bob!"),
    ],
)
async def test_compose_greeting_activity(input, expected_output):
    activity_environment = ActivityEnvironment()
    result = await activity_environment.run(compose_greeting, input)
    assert expected_output == result
