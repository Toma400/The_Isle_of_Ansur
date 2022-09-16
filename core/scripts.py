#==========|=====================================================================================
# EVENT    | Handles events happening in game and manages forged_events composition.
# HANDLER  |
#==========|=====================================================================================
def event_handler(event_container: list, guitype):

    # "MENU" | Forged Event | Run when main menu starts
    if guitype[0] == "menu" and "MENU" not in event_container:
        event_container.append("MENU")
    if guitype[0] != "menu" and "MENU" in event_container:
        event_container.remove("MENU")

#==========|=====================================================================================
# SCRIPT   | Handles scripts running depending on forged_events. Currently needs implementation.
# HANDLER  |
#==========|=====================================================================================
def script_handler(event_container: list, screen, pg_events):

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