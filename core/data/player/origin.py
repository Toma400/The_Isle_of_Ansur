from core.data.pack_manag.packs import getPacks, PackTypes
from core.gui.manag.langstr import langjstring, ErrorDummy
from glob import glob as walkdir
from os.path import exists
import logging as log
import json

class Origin:

    cache = None

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for OID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

        self.file   : str  = f"stats/{self.mod_id}/origins/{self.name}.json"
        self.exists : bool = exists(self.file)
        if not self.exists:
            log.error(f"Tried to reach Origin file of OID {self.mod_id}:{self.name} but it doesn't exist. Path: {self.file}.")

    def oid(self) -> str:
        """Creates OID representation of origin, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(self.key, "stats", self.mod_id)

    def descr(self, gender: str = None) -> str:
        """Returns description of Origin taken from -key[_descr]-"""
        return langjstring(f"{self.key}_descr", "stats", self.mod_id, gender)

    def get(self, attribute: str) -> str | int | float | list | dict | None:
        """Returns specific attribute from Origin file. Any reuse of the same object reads from cache to optimise I/O"""
        if self.exists:
            if self.cache is None:
                with open(self.file) as jf:
                    self.cache = json.load(jf)
            if attribute in self.cache:
                return self.cache[attribute]
            return None # if attr not in cache
        return None     # if file doesn't exist

    def getc(self, category: str, attribute: str) -> str | int | float | list | dict | None:
        """Returns attribute from category dict. Used for more nested sections"""
        get = self.get(category)
        if type(get) == dict:
            if attribute in get:
                return get[attribute]
            return None # if attr not in 'get'
        return None     # if 'get' is None or type w/o keys

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()


def getOrigin(oid: str) -> Origin | ErrorDummy:
    """Origin constructor that uses OID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getOrigins()"""
    rlid_ems = oid.split(":")

    if exists(f"stats/{rlid_ems[0]}/origins/{rlid_ems[1]}.json"):
        def returnKey() -> str:  # returns translation key
            with open(f"stats/{rlid_ems[0]}/origins/{rlid_ems[1]}.json") as jf:
                pjf = json.load(jf)
                return pjf["key"]

        return Origin(name=rlid_ems[1], tr_key=returnKey(), mod_id=rlid_ems[0])
    return ErrorDummy()

def getOrigins() -> list[Origin]:
    """Main gatherer of origin data during load/reload"""
    ret: list[Origin] = []
    for stat_pack in getPacks(PackTypes.STAT_PACK):
        if exists(f"stats/{stat_pack}/origins"):
            for or_file in walkdir(f"stats/{stat_pack}/origins/*.json"):
                or_name = or_file.replace(f"stats/{stat_pack}/origins", "").replace(".json", "").strip("\\")
                with open(or_file) as jf:
                    pjf = json.load(jf)
                    ret.append(Origin(or_name, pjf["key"], stat_pack))
    return ret


def getOriginsTuple() -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Origin getter, returning tuple of <translation, OID>"""
    ret: list[(str, str)] = []
    for rlc in getOrigins():
        ret.append((rlc.langstr(), rlc.oid()))
    return ret