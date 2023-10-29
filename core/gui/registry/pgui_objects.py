from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from pygame_gui.elements.ui_text_entry_box import UITextEntryBox
from pygame_gui.elements.ui_drop_down_menu import UISelectionList
from pygame_gui.elements.ui_text_box import UITextBox
from core.gui.manag.langstr import langstring as lstr
from core.gui.manag.pgui_wrapper import getCurrentID, getCurrentIndex, resetSelected
from core.file_system.save_manag import listSaves
from core.data.player.religion import getReligionsTuple
from core.data.player.origin import getOriginsTuple
from core.data.player.profession import getClassesTuple
from core.data.player.gender import getGendersTuple
from core.data.player.race import getRacesTuple
from core.gui.manag.pc import toPxX, toPxY
import pygame, logging

class PGUI_Helper:
    """
    Variant of GUI_Helper class that operates with PyGame_GUI objects.
    It is separated for easier deprecation in the future.

    Naming conventions:
    char | character creation

    lb | listbox (later element type)
    """

    def __init__(self, manager):
        self.char__lb_gender = UISelectionList(item_list=getGendersTuple(),                 relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(8))),  manager=manager)
        self.char__tb_gender = UITextBox      (html_text=lstr("ccrt__gender"),              relative_rect=pygame.Rect((toPxX(40), toPxX(14)), (toPxX(40), toPxX(15))), manager=manager)
        self.char__lb_race   = UISelectionList(item_list=getRacesTuple(),                   relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__tb_race   = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(40), toPxX(26)), (toPxX(40), toPxX(20))), manager=manager)
        self.char__lb_class  = UISelectionList(item_list=getClassesTuple(),                 relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__tb_class  = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(40), toPxX(26)), (toPxX(40), toPxX(20))), manager=manager)
        self.char__lb_name   = UISelectionList(item_list=[],                                relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__ti_name   = UITextEntryLine(                                             relative_rect=pygame.Rect((toPxX(40), toPxX(27)), (toPxX(40), 50)),        manager=manager)
        # ---
        self.char__lb_attrs  = UISelectionList(item_list=[],                                relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(20), toPxX(10))), manager=manager)
        self.char__lb_skills = UISelectionList(item_list=[],                                relative_rect=pygame.Rect((toPxX(40), toPxX(17)), (toPxX(20), toPxX(20))), manager=manager)
        self.char__tb_attrs  = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(62), toPxX(6)),  (toPxX(29), toPxX(10))), manager=manager)
        self.char__tb_skills = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(62), toPxX(17)), (toPxX(29), toPxX(20))), manager=manager)
        # ---
        self.char__lb_rel    = UISelectionList(item_list=getReligionsTuple(),               relative_rect=pygame.Rect((toPxX(40), toPxX(6)),  (toPxX(40), toPxX(20))), manager=manager)
        self.char__tb_rel    = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(40), toPxX(26)), (toPxX(40), toPxX(20))), manager=manager)
        # ---
        self.char__lb_orig   = UISelectionList(item_list=getOriginsTuple(),                 relative_rect=pygame.Rect((toPxX(40), toPxY(8)),  (toPxX(20), toPxY(76))), manager=manager)
        self.char__tb_orig   = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(60), toPxY(8)),  (toPxX(20), toPxY(20))), manager=manager)
        self.char__ti_hist   = UITextEntryBox (                                             relative_rect=pygame.Rect((toPxX(60), toPxY(35)), (toPxX(20), toPxY(49))), manager=manager)
        # ---
        self.char__tb_pdth   = UITextBox      (html_text=lstr("ccrt__sett_hardcore_descr"), relative_rect=pygame.Rect((toPxX(50), toPxY(10)), (toPxX(40), 50)),        manager=manager)
        self.char__temp_warn = UITextBox      (html_text=lstr("ccrt__end_save_warn"),       relative_rect=pygame.Rect((toPxX(45), toPxY(70)), (toPxX(30), 100)),       manager=manager)
        # ---
        self.load__saves     = UISelectionList(item_list=[],                                relative_rect=pygame.Rect((toPxY(10), toPxY(10)), (toPxX(30), toPxY(70))), manager=manager)
        self.load__descr     = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(40), toPxY(45)), (toPxX(52), toPxY(35))), manager=manager)
        self.load__temp_warn = UITextBox      (html_text=lstr("ccrt__end_save_warn"),       relative_rect=pygame.Rect((toPxX(40), toPxY(38)), (toPxX(52), toPxY(5))),  manager=manager)
        # ---
        self.pack__zip_list  = UISelectionList(item_list=[],                                relative_rect=pygame.Rect((toPxY(10), toPxY(10)), (toPxX(30), toPxY(70))), manager=manager)
        self.pack__descr     = UITextBox      (html_text="",                                relative_rect=pygame.Rect((toPxX(50), toPxY(45)), (toPxX(40), toPxY(30))), manager=manager)
        self.char__ti_name.set_forbidden_characters("forbidden_file_path")
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
            case UITextEntryBox.__module__:  return self.get_element(element).get_text()

    def get_element_index(self, element: str) -> int | None:
        """Returns selected element of the GUI, as index number"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: return getCurrentIndex(self.get_element(element))

    def get_options(self, element: str) -> any:
        """Returns list of options for specific type. It doesn't return value!"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: return self.get_element(element).item_list
            case _:                          logging.warning(f"Tried to request -get_options- from PGUI element that does not support it: {element}")

    def set_default(self, element: str):
        """Resets selected element of the GUI, usually putting it in its default state"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: resetSelected(self.get_element(element))
            case _:                          logging.warning(f"Tried to request -set_default- from PGUI element that does not support it: {element}")

    def set_value(self, element: str, overwrite):
        """Overwrites item list of selected element"""
        match self.get_element(element).__module__:
            case UISelectionList.__module__: self.get_element(element).set_item_list(overwrite)
            case UITextBox.__module__:       self.get_element(element).set_text(overwrite)
            case UITextEntryBox.__module__:  self.get_element(element).set_text(overwrite)
            case UITextEntryLine.__module__: self.get_element(element).set_text(overwrite)
            case _:                          logging.warning(f"Tried to request -set_value- from PGUI element that does not support it: {element}")

    def clear_values(self):
        """Clears values of elements that are meant to be empty at the initial phase (look at __init__)"""
        UISelectionListList = ["char__lb_attrs", "char__lb_skills"]
        UITextBoxList       = ["char__tb_race", "char__tb_class", "char__tb_attrs", "char__tb_skills", "char__tb_rel", "char__tb_orig", "char__tb_hist", "load__descr"]
        UITextEntryBoxList  = ["char__ti_hist"]
        UITextEntryLineList = ["char__ti_name"]

        for el in self.get_elements():
            match self.get_element(el).__module__:
                case UISelectionList.__module__:
                    if el in UISelectionListList: self.get_element(el).set_item_list([])
                case UITextBox.__module__:
                    if el in UITextBoxList:       self.get_element(el).set_text("")
                case UITextEntryLine.__module__:
                    if el in UITextEntryLineList: self.get_element(el).set_text("")
                case UITextEntryBox.__module__:
                    if el in UITextEntryBoxList:  self.get_element(el).set_text("")

    def reset_selection_list_all(self):
        """Resets all elements of the GUI, putting them in their default state"""
        for pobj in self.get_elements():
            self.set_default(pobj)

    def restart(self, manager):
        """Restarts whole initialisation process of the class"""
        self.__init__(manager)