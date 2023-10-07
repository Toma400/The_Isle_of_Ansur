from core.data.pack_manag.packs import getPacks, PackTypes
from core.gui.manag.langstr import langjstring
from glob import glob as walkdir
from os.path import exists
import json

class Religion:

    cache = None

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

    def get(self, attribute: str) -> str | int | float | list | dict:
        """Returns specific attribute from Religion file. Any reuse of the same object reads from cache to optimise I/O"""
        if self.cache is None:
            with open(f"stats/{self.mod_id}/religions/{self.name}.json") as jf:
                self.cache = json.load(jf)
        return self.cache[attribute]

    def getc(self, category: str, attribute: str) -> str | int | float | list | dict:
        """Returns attribute from category dict. Used for more nested sections"""
        return self.get(category)[attribute]

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getReligion(rlid: str) -> Religion:
    """Religion constructor that uses RLID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getReligions()"""
    rlid_ems = rlid.split(":")

    def returnKey() -> str: # returns translation key
        with open(f"stats/{rlid_ems[0]}/religions/{rlid_ems[1]}.json") as jf:
            pjf = json.load(jf)
            return pjf["key"]

    return Religion(name=rlid_ems[1], tr_key=returnKey(), mod_id=rlid_ems[0])

def getReligions() -> list[Religion]:
    """Main gatherer of religion data during load/reload"""
    ret: list[Religion] = []
    for stat_pack in getPacks(PackTypes.STAT_PACK):
        if exists(f"stats/{stat_pack}/religions"):
            for rl_file in walkdir(f"stats/{stat_pack}/religions/*.json"):
                rl_name = rl_file.replace(f"stats/{stat_pack}/religions", "").replace(".json", "").strip("\\")
                with open(rl_file) as jf:
                    pjf = json.load(jf)
                    ret.append(Religion(rl_name, pjf["key"], stat_pack))
    return ret

def getReligionsTuple() -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Religion getter, returning tuple of <translation, RLID>"""
    ret: list[(str, str)] = []
    for rlc in getReligions():
        ret.append((rlc.langstr(), rlc.rlid()))
    return ret