from core.data.pack_manag.packs import getPacks, PackTypes
from core.gui.manag.langstr import langjstring
from core.file_system.parsers import loadJSON
from glob import glob as walkdir
from os.path import exists

class Religion:

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for RLID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def rlid(self) -> str:
        """Creates RLID representation of religion, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(self.key, "stats", self.mod_id)

    def descr(self) -> str:
        """Returns description of Religion taken from -key[_descr]-"""
        return langjstring(f"{self.key}_descr", "stats", self.mod_id)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getReligion(rlid: str) -> Religion:
    """Religion constructor that uses RLID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getReligions()"""
    rlid_ems = rlid.split(":")

    def returnKey() -> str: # returns translation key
        return loadJSON(f"stats/{rlid_ems[0]}/religions/{rlid_ems[1]}.json")["key"]

    return Religion(name=rlid_ems[1], tr_key=returnKey(), mod_id=rlid_ems[0])

def getReligions() -> list[Religion]:
    """Main gatherer of religion data during load/reload"""
    ret: list[Religion] = []
    for stat_pack in getPacks(PackTypes.STAT_PACK):
        if exists(f"stats/{stat_pack}/religions"):
            for rl_file in walkdir(f"stats/{stat_pack}/religions/*.json"):
                rl_name = rl_file.replace(f"stats/{stat_pack}/religions", "").replace(".json", "").strip("\\")
                pjf = loadJSON(rl_file)
                ret.append(Religion(rl_name, pjf["key"], stat_pack))
    return ret

def getReligionsTuple() -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Religion getter, returning tuple of <translation, RLID>"""
    ret: list[(str, str)] = []
    for rlc in getReligions():
        ret.append((rlc.langstr(), rlc.rlid()))
    return ret