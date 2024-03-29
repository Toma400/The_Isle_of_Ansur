from pygame_gui.elements.ui_drop_down_menu import UISelectionList

def getCurrentID(slist: UISelectionList) -> str | None:
    """Retrieves ID from UISelectionList selected element"""
    for item in slist.item_list:
        if item['selected']:
            return item["object_id"]
    return None

def getCurrentIndex(slist: UISelectionList) -> int | None:
    """Retrieves index from UISelectionList selected element"""
    i = 0
    for item in slist.item_list:
        if item['selected']:
            return i
        i += 1
    return None

def resetSelected(slist: UISelectionList):
    """Used to reset selection of UISelectionList. Immediate breaking is used to optimise, but it is designed for single-selection."""
    for item in slist.item_list:
        if item['selected']:
            item['selected'] = False
            break