from unittest import mock
import pytest
from tetra3 import Tetra3

from conftest import lib_root_dir

@pytest.mark.parametrize(
    "star_catalog, expected_name, expected_path",
    [
        ("bsc5", "bsc5", lib_root_dir() / "bsc5"),
        ("hip_main", "hip_main", lib_root_dir() / "hip_main.dat"),
        ("tyc_main", "tyc_main", lib_root_dir() / "tyc_main.dat"),
        ("/mock/path/hip_main.dat", "hip_main", "/mock/path/hip_main.dat"),
        ("/mock/path/hip_main", "hip_main", "/mock/path/hip_main.dat"),
        ("/mock/path/tyc_main.dat", "tyc_main", "/mock/path/tyc_main.dat"),
        ("/mock/path/tyc_main", "tyc_main", "/mock/path/tyc_main.dat"),
    ]
)
@mock.patch("tetra3.tetra3.Path.exists", return_value=True)
def test_build_catalog_path(mock_exists, star_catalog, expected_name, expected_path):
    catalog_name, catalog_path = Tetra3._build_catalog_path(star_catalog)

    assert catalog_name == expected_name
    assert str(catalog_path) == str(expected_path)
