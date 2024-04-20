from pathlib import Path

import pytest

_DATA_DIR = Path(__file__).parent / 'data'


@pytest.fixture
def data_dir() -> Path:
    return _DATA_DIR
