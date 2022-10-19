# type: ignore
import os
from pathlib import Path, _posix_flavour, _windows_flavour


class DotPath(Path):
    """To enable adding Paths as nested attributes of other Paths, which is not possible with a
    standard pathlib Path factory object. Replication _flavour setting from Path source code gets
    around an issue with inheriting from Path, though is a little ugly."""

    # why this? because of Path's __new__ method, see
    # https://codereview.stackexchange.com/questions/162426/subclassing-pathlib-path
    # also refer to whether a fix is implemented from
    # https://discuss.python.org/t/fixing-subclassing-in-pathlib/8983/8
    _flavour = _windows_flavour if os.name == "nt" else _posix_flavour


def make_dirs(indir: DotPath) -> None:
    """Recursively make all project directories of initial DotPath object fed in
    by looping through class attributes that are also custom added DotPath objects.

    :param indir: a DotPath object with child DotPath attributes already attached."""

    custom_child_attributes = (attr_name for attr_name in dir(indir) if "_" not in attr_name)
    for attr_name in custom_child_attributes:
        attribute = getattr(indir, attr_name)
        if isinstance(attribute, DotPath) and attr_name != "parent":
            attribute.mkdir(exist_ok=True, parents=False)
            # recursive call to traverse down the attribute tree if exists
            make_dirs(attribute)


# base DIR Path is (Dot)Path of the repository root directory
DIR = DotPath(__file__).parent.parent.resolve()
"""
DIR DotPath allows object-based access to all project directories with a single import.
The use of make_dirs(DIR) anytime the file is accessed ensures no errors from trying to access
folders that do not exist when code is run on containers/virtual machines.

Usage:

from common.directory import DIR

df = pd.read_csv(DIR.DATA.RAW / "raw_filename.csv"
"""

DIR.DATA = DIR / "data"
DIR.DATA.IMAGES = DIR.DATA / "images"
DIR.DATA.LOGS = DIR.DATA / "logs"
DIR.DATA.TEMP = DIR.DATA / "temp"


# run any time DIR is imported, even when __name__ != "__main__" to avoid any folder issues
make_dirs(DIR)
