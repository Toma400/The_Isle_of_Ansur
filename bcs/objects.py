from bcs.operators import settings, img_load, cells, langstr, projectlist, ratio_adv
import pygame, pygame_gui

pggui = pygame_gui.elements

class Screen:

    def __init__(self, guitype: str):
        self.dyn_screen = [self.run_screen()]
        self.screen     = self.dyn_screen[0]
        self.gui_manag  = pygame_gui.UIManager(
                            window_resolution=(settings("res_x"), settings("res_y")),
                            theme_path=f"bcs/themes/{settings('bcs_theme')}.json")
        self.gui        = GUI_Helper(self.gui_manag, guitype)

    def reset(self):
        """hard refresh of screen | should reassign currently used 'screen' variable"""
        self.dyn_screen[0] = self.run_screen()
        self.screen        = self.dyn_screen[0]
        self.gui_manag     = pygame_gui.UIManager(
                              window_resolution=(settings("res_x"), settings("res_y")),
                              theme_path=f"bcs/themes/{settings('bcs_theme')}.json")
        return self.screen

    def guitype_switch(self, guitype: str):
        """Used to reload guitypes"""
        self.reset()
        self.gui           = GUI_Helper(self.gui_manag, guitype)

    @staticmethod
    def run_screen():
        while True:
            try:
                pygame.display.quit(); pygame.display.init()

                screen = pygame.display.set_mode([settings("res_x"), settings("res_y")])
                pygame.display.set_caption("Baedoor Creation Set")
                pygame.display.set_icon(img_load("bcs/assets/graphical/", "bcs.png"))
                return screen
            except pygame.error: continue

class GUI_Helper:

    def __init__(self, pg_gui, guitype):
        self.manager         = pg_gui
        # OBJECTS
        if guitype == "login":
            self.login__logo     = pggui.UIImage(        relative_rect=pygame.Rect(cells(3, 3),   ratio_adv(10)), image_surface=img_load("bcs/assets/graphical/", "bcs.png"), manager=pg_gui)
            self.login__text     = pggui.UILabel(        relative_rect=pygame.Rect(cells(15, 3),  cells(70, 10)), text=langstr("login__listbox"),                             manager=self.manager)
            self.login__projects = pggui.UISelectionList(relative_rect=pygame.Rect(cells(15, 15), cells(70, 70)), item_list=projectlist(),                                    manager=self.manager)
            self.login__enter    = pggui.UIButton(       relative_rect=pygame.Rect(cells(15, 90), cells(20, 5)),  text=langstr("login__open"),                                manager=self.manager)
            self.login__add      = pggui.UIButton(       relative_rect=pygame.Rect(cells(40, 90), cells(20, 5)),  text=langstr("login__add"),                                 manager=self.manager)
            self.login__remove   = pggui.UIButton(       relative_rect=pygame.Rect(cells(65, 90), cells(20, 5)),  text=langstr("login__remove"),                              manager=self.manager)
        if guitype == "logged":
            self.login__projects = pggui.UISelectionList(relative_rect=pygame.Rect(cells(15, 15), cells(70, 70)), item_list=projectlist(),                                    manager=self.manager)

    @staticmethod
    def is_clicked(event_list):
        if event_list.type == pygame_gui.UI_BUTTON_PRESSED:
            return event_list.ui_element