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
    "avatars",
    "containers", # TODO
    "locations",  # TODO
    "reputation", # TODO
    "statistics",
    "inventory"   # TODO
]
REQUIRED_FILES = [
    # main
    "data.toml",
    "mods.toml",                 # TODO ('mod_id': 'ver')
    # nested
    "reputation/towns.yaml",     # TODO # Where to put detailed ideas on towns/guilds/religions, instead of just numbers?
    "reputation/guilds.yaml",    # TODO
    "reputation/religions.yaml", # TODO
    "statistics/attributes.yaml",
    "statistics/skills.yaml"
]
# To make
# - quest log
# - location data
# - banking accounts
# - used mod IDs
# - diary

# Default points or values
DEF_ATTR = 8
DEF_SKL  = 0

# Default added points or values
ADD_ATTR = 1
ADD_SKL  = 3