#-------------|--------------------------------------------------------------------------------------------------
# SYS_REF     | SysRef contains variables used to determine some values usable with IoA systems. Exterioring
#             | those is made to ease referencing in the future, samely as changing those.
#-------------|--------------------------------------------------------------------------------------------------
import os; gpath = os.path.dirname(os.path.abspath("main.py"))

class SysRef:

    name    = "The Isle of Ansur"
    status  = "pre alpha"
    version = "3"

    cname   = "Between Shadows and Light"
    cycle   = "0"

    save_system     = "1.0"
    vanilla_modules = [
        "ansur"
    ]