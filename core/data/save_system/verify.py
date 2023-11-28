from os.path import exists
from enum import Enum

REQUIRED_DIRS = [
    "statistics",
    "inventory"
]
REQUIRED_FILES = [
    # main
    "data.toml",
    # nested
    "statistics/attributes.toml",
    "statistics/skills.toml"
]
class SV_KIND(Enum):
    BUFFER    = "buffer"    # buffer in single player
    ARENA     = "arena"     # buffer on arena
    CYCLICAL  = "cyclical"  # saved cyclically
    ADVENTURE = "adventure" # saved by hand

def verifySave(name: str, variant: SV_KIND = SV_KIND.BUFFER) -> bool:
    sdir = f"saves/{name}/{variant.value}"
    for rd in REQUIRED_DIRS:
        if not exists(f"{sdir}/{rd}"):
            return False
    for rf in REQUIRED_FILES:
        if not exists(f"{sdir}/{rf}"):
            return False
    return True

# TODO:
# ANCITIPATED STRUCTURE
# - {avatars}
# - statistics
#   - attributes.toml
#   - skills.toml
# - inventory
#
# - data.toml
# - {avatar.png}