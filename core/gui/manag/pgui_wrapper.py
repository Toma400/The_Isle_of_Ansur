from pygame_gui.elements.ui_drop_down_menu import UISelectionList

def getCurrentID(slist: UISelectionList) -> str or None:
    """Retrieves ID from UISelectionList selected element"""
    for item in slist.item_list:
        if item['selected']:
            return item["object_id"]
    return None

# use of 'getCurrentID' is preferable
def getCurrentText(slist: UISelectionList) -> str or None:
    for item in slist.item_list:
        if item['selected'] is not None:
            return item["text"]