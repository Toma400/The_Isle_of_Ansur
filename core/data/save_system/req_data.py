from enum import Enum

"""
Module that holds all variables related to save files.
"""

class SV_KIND (Enum):
    BUFFER    = "buffer"    # buffer in single player
    ARENA     = "arena"     # buffer on arena
    CYCLICAL  = "cyclical"  # saved cyclically
    ADVENTURE = "adventure" # saved by hand

REQUIRED_DIRS = [
    "statistics",
    "inventory"
]
REQUIRED_FILES = [
    # main
    "data.toml",
    # nested
    "statistics/attributes.yaml",
    "statistics/skills.yaml"
]

# Default points or values
DEF_ATTR = 8

# Default added points or values
ADD_ATTR = 1