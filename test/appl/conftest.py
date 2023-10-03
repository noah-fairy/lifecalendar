from test.appl.container import compose_container
from test.appl.container import container as _container

import pytest


@pytest.fixture(scope="session")
def container():
    compose_container()
    return _container
