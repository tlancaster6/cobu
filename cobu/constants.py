import os
try:
    from importlib.metadata import metadata  # Python 3.8
except ImportError:
    from importlib_metadata import metadata  # Python < 3.8

COBU_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(COBU_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'data')

# package metadata
_META = metadata("cobu")
NAME = _META["name"]
VERSION = _META["version"]
DESCRIPTION = _META["summary"]
AUTHOR = _META["author"]
AUTHOR_EMAIL = _META["author-email"]
URL = _META["home-page"]
LICENSE = _META["license"]
VERSION_LONG = "FiftyOne v%s, %s" % (VERSION, AUTHOR)
