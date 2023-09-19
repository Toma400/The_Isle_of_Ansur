from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu, UISelectionList
from core.data.player.gender import getGendersTuple
import pygame

class PGUI_Helper:
    """
    Variant of GUI_Helper class that operates with PyGame_GUI objects.
    It is separated for easier deprecation in the future.

    Naming conventions:
    char | character creation

    lb | listbox (later element type)
    """

    def __init__(self, manager):
        #self.char__lb_race = UIDropDownMenu(options_list=getGendersStrings(), relative_rect=pygame.Rect((400, 100), (400, 50)), starting_option=getGendersStrings()[0], manager=manager)
        self.char__lb_race = UISelectionList(item_list=getGendersTuple(), relative_rect=pygame.Rect((400, 100), (400, 75)), manager=manager)
        self.hide_elements()

    def get_element(self, element: str):
        """Returns specific field/attribute given its string"""
        return self.__getattribute__(element)

    def get_elements(self) -> [str]:
        """Returns list of fields/attributes of the class"""
        return self.__dict__.keys()

    def show_element(self, element: str):
        """Swap visibility of element from default invisibility"""
        self.get_element(element).show()

    def hide_elements(self):
        """Hide all elements from PGUI_Helper. Usually used to automatically flush all visible ones between screens"""
        for uie in self.get_elements():
            self.get_element(uie).hide()

    def get_element_choice(self, element: str) -> str or None:
        """Returns selected element of the GUI (available only for some GUI types)"""
        match type(self.get_element(element)):
           case UISelectionList: return self.get_element(element).get_single_selection() # should return ID, not translation

    def restart(self, manager):
        """Restarts whole initialisation process of the class"""
        self.__init__(manager)