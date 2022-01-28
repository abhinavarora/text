import os

_TEXT_BUCKET = "https://download.pytorch.org/models/text/"
_CACHE_DIR = os.path.expanduser("~/.torchtext/cache")

from . import data
from . import datasets
from . import experimental
from . import functional
from . import models
from . import nn
from . import transforms
from . import utils
from . import vocab
from ._extension import _init_extension


try:
    from .version import __version__, git_version  # noqa: F401
except ImportError:
    pass

__all__ = ["data", "nn", "datasets", "utils", "vocab", "transforms", "functional", "models", "experimental"]


_init_extension()


del _init_extension
