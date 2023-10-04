from core.data.pack_manag.packs import PackTypes, getPacks
from core.data.pack_manag.id import agnosticID
from core.gui.manag.langstr import langjstring as ljstr
from core.file_system.parsers import loadYAML
from os.path import exists

from system.mod_manag import mod_lister

DEFAULT_ATTR = 8

class Attribute:

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for GID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def aid(self) -> str:
        """Creates AID representation of attribute, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return ljstr(self.key, "stats", self.mod_id)

    def descr(self) -> str:
        """Returns description of Attribute taken from -key[_descr]-"""
        return ljstr(f"{self.key}_descr", "stats", self.mod_id)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getAttributes() -> list[Attribute]:
    """Main gatherer of attributes available in game"""
    ret: list[Attribute] = []
    for stat_pack in getPacks(PackTypes.STAT_PACK):
        if exists(f"stats/{stat_pack}/attributes.yaml"):
            pjf = loadYAML(f"stats/{stat_pack}/attributes.yaml")
            for attr in pjf.keys():
                ret.append(Attribute(attr, pjf[attr]["key"], stat_pack))
    return ret

def getAttribute(aid: str) -> Attribute:
    for attr in getAttributes():
        if attr.name == agnosticID(aid):
            return attr
    raise KeyError(f"Cannot find attribute of AID: {aid}.")

def getAttributesTuple() -> list[(str, str)]:
    """Compatible variant that translates -getAttributes()- into PyGame GUI compatible format"""
    ret = []
    for attr in getAttributes():
        ret.append((attr.langstr(), f"{attr.aid}"))
    return ret