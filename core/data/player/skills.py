from core.gui.manag.langstr import langstring as lstr

class Skill:

    def __init__(self, name: str, key: str):
        self.name = name
        self.key  = key

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return lstr(key=self.key)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()


def getSkills() -> list[Skill]:
    """Main gatherer of skills available in game"""
    return [
        Skill("", "")
    ]

def getSkillsTuple() -> list[(str, str)]:
    """Compatible variant that translates -getSkills()- into PyGame GUI compatible format"""
    ret = []
    for skill in getSkills():
        ret.append((skill.langstr(), skill.name))
    return ret