from enum import Enum

# class ID(Enum):
#     CID: "ClassID"
#     RID: "RaceID"
#     GID: "GenderID"
#     AID: "AttributeID"
#     SID: "SkillID"
#     # planned
#     EID: "EntityID"
#     LID: "LocationID"
#     HID: "ChestID"

def agnosticID(string: str) -> str:
    if "ansur:" in string:
        return string.replace("ansur:", "")
    return string

def agnosticIDRev(string: str) -> str:
    if ":" not in string:
      return f"ansur:{string}"
    return string