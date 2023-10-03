from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from pygame_gui.elements.ui_drop_down_menu import UISelectionList
from pygame_gui.elements.ui_text_box import UITextBox
from core.gui.manag.langstr import langstring as lstr
from core.gui.manag.pgui_wrapper import getCurrentID, getCurrentIndex, resetSelected
from core.data.player.attributes import getAttributesTuple
from core.data.player.skills import getSkillsTuple
from core.data.player.profession import getClassesTuple
from core.data.player.gender import getGendersTuple
from core.data.player.race import getRacesTuple
from core.gui.manag.pc import toPxX, toPxY
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
        self.char__lb_gender = UISelectionList(item_list=getGendersTuple(),    relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(8))),  manager=manager)
        self.char__tb_gender = UITextBox      (html_text=lstr("ccrt__gender"), relative_rect=pygame.Rect((toPxX(40), toPxX(14)), (toPxX(40), toPxX(15))), manager=manager)
        self.char__lb_race   = UISelectionList(item_list=getRacesTuple(),      relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__tb_race   = UITextBox      (html_text="",                   relative_rect=pygame.Rect((toPxX(40), toPxX(26)), (toPxX(40), toPxX(20))), manager=manager)
        self.char__lb_class  = UISelectionList(item_list=getClassesTuple(),    relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__tb_class  = UITextBox      (html_text="",                   relative_rect=pygame.Rect((toPxX(40), toPxX(26)), (toPxX(40), toPxX(20))), manager=manager)
        self.char__lb_name   = UISelectionList(item_list=[],                   relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__ti_name   = UITextEntryLine(                                relative_rect=pygame.Rect((toPxX(40), toPxX(27)), (toPxX(40), 50)),        manager=manager)
        # ---
        self.char__lb_attrs  = UISelectionList(item_list=getAttributesTuple(), relative_rect=pygame.Rect((toPxX(40), toPxX(6)), (175, 200)), manager=manager)
        self.char__lb_skills = UISelectionList(item_list=getSkillsTuple(),     relative_rect=pygame.Rect((600, 100), (175, 200)), manager=manager)
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

    def get_value(self, element: str) -> str | None:
        """Returns value of selected GUI element (available only for some GUI types)"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: return getCurrentID(self.get_element(element))
            case UITextEntryLine.__module__: return self.get_element(element).text

    def get_element_index(self, element: str) -> int | None:
        """Returns selected element of the GUI, as index number"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: return getCurrentIndex(self.get_element(element))

    def set_default(self, element: str):
        """Resets selected element of the GUI, usually putting it in its default state"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: resetSelected(self.get_element(element))

    def set_value(self, element: str, overwrite):
        """Overwrites item list of selected element"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: self.get_element(element).set_item_list(overwrite)
            case UITextBox.__module__:       self.get_element(element).set_text(overwrite)
            case UITextEntryLine.__module__: self.get_element(element).set_text(overwrite)

    def reset_selection_list_all(self):
        """Resets all elements of the GUI, putting them in their default state"""
        for pobj in self.get_elements():
            self.set_default(pobj)

    def restart(self, manager):
        """Restarts whole initialisation process of the class"""
        self.__init__(manager)