from core.data.pack_manag.id import absoluteID
from core.file_system.parsers import loadYAML
import re

# Example of Stat Script:
# "800 + [A]ansur:endurance * 25 + [S]ansur:survival * 30"

# Use [A] to indicate attribute and [S] to indicate skill

ATTR_REF  = r"\[A\][\w:]*"
SKILL_REF = r"\[S\][\w:]*"

def statScript(player: str, sv_str: str, script: str) -> int:
    script_var = script
    # find [A]* and [S]* strings and replace them with int values
    ar = re.findall(ATTR_REF, script)
    sr = re.findall(SKILL_REF, script)
    for a in ar: #[A]attributeID
        al    = loadYAML(f"saves/{player}/{sv_str}/statistics/attributes.yaml")
        abs_a = absoluteID(a.replace("[A]", ""))
        script_var = script_var.replace(a, str(al[abs_a]))
    for s in sr: #[S]skillID
        sl    = loadYAML(f"saves/{player}/{sv_str}/statistics/skills.yaml")
        abs_s = absoluteID(s.replace("[S]", ""))
        script_var = script_var.replace(s, str(sl[abs_s]))
    # do math operation on string with replaced attribute/skill values
    return eval(script_var)