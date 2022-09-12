from core.file_system.repo_manag import deep_file_lister
import logging as log
#==========|=====================================================================================
# EVENT    | Handles events happening in game and manages forged_events composition.
# HANDLER  |
#==========|=====================================================================================
def event_handler(event_container: list, guitype):

    # "MENU" | Forged Event | Run when main menu starts
    if guitype == "menu" and "MENU" not in event_container:
        event_container.append("MENU")

#==========|=====================================================================================
# SCRIPT   | Handles scripts running depending on forged_events. Currently needs implementation.
# HANDLER  |
#==========|=====================================================================================
def script_handler(event_container: list, screen, pg_events):

    script_loader()
    for i in ioaScript.subclasses:
        try:
            if i.event in event_container:
                i.run(i, screen, pg_events, fg_events=event_container)
        except AttributeError: pass

#==========|=====================================================================================
# HELPERS  | Functions to clean up code above
#==========|=====================================================================================
class ioaScript:
    subclasses = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
    def __init__(self):
        pass

def script_loader():
    for x in deep_file_lister(f"scripts/", ext="py"):  # | imports all modules from /scripts/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", "."); x2 = x2.replace("//", "."); x2 = x2.replace("//", ".")
        log.debug(f"Script is being imported: [{x2}]")
        __import__(x2)