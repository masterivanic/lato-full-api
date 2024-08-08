import pytest
from main import create_application

@pytest.fixture
def app():
    return create_application()