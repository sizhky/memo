from ._error import NotInstalled
from ._grid import grid, random_grid
from ._base import memlist, memfile, memfunc
from ._util import time_taken
from ._version import __version__

try:
    from memo._http import memweb
except ModuleNotFoundError:
    memweb = NotInstalled("memweb", "web")


__all__ = [
    "__version__"
    "grid",
    "random_grid",
    "memlist",
    "memfile",
    "memfunc",
    "memweb",
    "time_taken",
]
