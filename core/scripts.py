import logging as log
#==========|=====================================================================================
# EVENT    | Handles events happening in game and manages forged_events composition.
# HANDLER  |
#==========|=====================================================================================
def event_handler(event_container: list, guitype):

    event_menus = [
        "MENU", "SETTINGS"
    ]

    for i in event_menus:
        if guitype[0] == i.lower() and i not in event_container:
            event_container.append(i)
        if guitype[0] != i.lower() and i in event_container:
            event_container.remove(i)

#==========|=====================================================================================
# SCRIPT   | Handles scripts running depending on forged_events. Currently needs implementation.
# HANDLER  |
#==========|=====================================================================================
def script_handler(event_container: list, screen, pg_events, dyn_screen):

    for i in ioaScript.subclasses:
        try:
            if i.event in event_container:
                i.tick(i, screen, pg_events, fg_events=event_container, fg_core=dyn_screen)
        except AttributeError: ioaScript.subclasses.remove(i); log.warning(f"Script [{i.__name__}] had AttributeError. Removing it from running scripts...")

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