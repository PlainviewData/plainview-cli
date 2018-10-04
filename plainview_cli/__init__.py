from .version import version_info, __version__
from .CommandLine import ExecuteCommand

# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
    'version_info',
    'ExecuteCommand'
]
