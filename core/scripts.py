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
def script_handler(event_container: list):

    if not event_container:
        pass