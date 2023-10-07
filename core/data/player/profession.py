from core.gui.manag.langstr import langjstring
from system.mod_manag import mod_lister
from glob import glob as walkdir
from os.path import exists
import json

class Class:

    cache = None

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for CID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def cid(self) -> str:
        """Creates CID representation of class, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(key=self.key, modtype="stats", modid=self.mod_id)

    def descr(self) -> str:
        """Returns description of Class taken from -key[_descr]-"""
        return langjstring(f"{self.key}_descr", "stats", self.mod_id)

    def get(self, attribute: str) -> str | int | float | list | dict:
        """Returns specific attribute from Class file. Any reuse of the same object reads from cache to optimise I/O"""
        if self.cache is None:
            with open(f"stats/{self.mod_id}/classes/{self.name}.json") as jf:
                self.cache = json.load(jf)
        return self.cache[attribute]

    def getc(self, category: str, attribute: str) -> str | int | float | list | dict:
        """Returns attribute from category dict. Used mostly with sections like -skills- or -attrs- by Classes"""
        return self.get(category)[attribute]

    def getRacesRequirement(self) -> list[str] | None:
        """Returns list of RIDs if class is exclusive to specific races - or None if it is not"""
        try:
            return self.get("races_exclusive")
        except:
            return None

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getClass(cid: str) -> Class:
    """Race constructor that uses CID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getClasses()"""
    cid_ems = cid.split(":")

    def returnKey() -> str: # returns translation key
        with open(f"stats/{cid_ems[0]}/classes/{cid_ems[1]}.json") as jf:
            pjf = json.load(jf)
            return pjf["key"]

    return Class(name=cid_ems[1], tr_key=returnKey(), mod_id=cid_ems[0])

def getClasses() -> list[Class]:
    """Main gatherer of class data during load/reload"""
    ret: list[Class] = []
    for stat_pack in mod_lister("stats"):
        if exists(f"stats/{stat_pack}/classes"):
            for class_file in walkdir(f"stats/{stat_pack}/classes/*.json"):
                class_name = class_file.replace(f"stats/{stat_pack}/classes", "").replace(".json", "").strip("\\")
                with open(class_file) as jf:
                    pjf = json.load(jf)
                    ret.append(Class(class_name, pjf["key"], stat_pack))
    return ret

def getClassesTuple(rid: str = None) -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Class getter, returning tuple of <translation, CID>"""
    ret: list[(str, str)] = []
    for cc in getClasses():
        # checks for exclusive race requirements
        if cc.getRacesRequirement() is not None and rid is not None:
            if rid in cc.getRacesRequirement():
                ret.append((cc.langstr(), cc.cid()))
        else:
            ret.append((cc.langstr(), cc.cid()))
    return ret