from core.data.pack_manag.packs import getPacks, PackTypes
from core.data.player.profession import getClass
from core.data.player.race import getRace
from core.gui.manag.langstr import langjstring as ljstr
from core.file_system.parsers import loadYAML
from core.data.pack_manag.id import absoluteID
from os.path import exists

DEFAULT_SK = 0               # default starting value for skill
RESERVED   = [               # reserved keywords in `skill.yaml`, serving unique purpose:
              "manual_excl"    # excluded in manual (player) selection
             ]

class Skill:

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for SID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def sid(self) -> str:
        """Creates SID representation of skill, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return ljstr(self.key, "stats", self.mod_id)

    def descr(self) -> str:
        """Returns description of Skill taken from -key[_descr]-"""
        return ljstr(f"{self.key}_descr", "stats", self.mod_id)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getSkills(manual_excl: bool = False) -> list[Skill]:
    """Main gatherer of skills available in game"""
    ret: list[Skill] = []
    for stat_pack in getPacks(PackTypes.STAT_PACK):
        if exists(f"stats/{stat_pack}/skills.yaml"):
            pjf = loadYAML(f"stats/{stat_pack}/skills.yaml")
            skx = pjf.get("manual_excl", [])
            for sk in pjf.keys():
                if sk not in RESERVED:
                    if manual_excl is False or sk not in skx:
                        ret.append(Skill(sk, pjf[sk]["key"], stat_pack))
    return ret

def getSkill(sid: str) -> Skill:
    for sk in getSkills():
        if sk.sid() == absoluteID(sid):
            return sk
    raise KeyError(f"Cannot find skill of SID: {sid}.")

def getSkillsTuple() -> list[(str, str)]:
    """Compatible variant that translates -getSkills()- into PyGame GUI compatible format"""
    ret = []
    for sk in getSkills():
        ret.append((sk.langstr(), f"{sk.sid}"))
    return ret

def getSkillsTupleAdjusted(cid: str, rid: str, manual_excl: bool) -> list[(str, str)]:
    """Variant that also gets numerical representation of skills. Works separately"""
    pre = {sk.sid(): DEFAULT_SK for sk in getSkills(manual_excl)}
    ret = []
    try:
        race = getRace(rid).get("skills")
        for sk_id in race:
            pre[absoluteID(sk_id)] += race[sk_id]
    except KeyError: pass
    finally:
        try:
            clss = getClass(cid).get("skills")
            for sk_id in clss:
                pre[absoluteID(sk_id)] += clss[sk_id]
        except KeyError: pass
    for sk_id in pre:
        ret.append((f"{getSkill(sk_id).langstr()}: {pre[sk_id]}", sk_id))
    return ret