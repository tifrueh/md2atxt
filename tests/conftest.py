import pytest
import pathlib
import shutil


@pytest.fixture
def testenv_path(tmp_path):
    scriptpath = pathlib.Path(__file__)
    testpath = scriptpath.parent
    shutil.copytree(f"{testpath}", tmp_path, dirs_exist_ok=True)
    return tmp_path
