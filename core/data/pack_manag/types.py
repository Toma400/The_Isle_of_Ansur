from enum import Enum

class PackTypes(Enum):
    WORLD_PACK  = "worlds"
    STAT_PACK   = "stats"
    THEME_PACK  = "themes"

pack_types = [PackTypes.THEME_PACK.value, PackTypes.STAT_PACK.value, PackTypes.WORLD_PACK.value]