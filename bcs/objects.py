from bcs.operators import settings, img_load, cells, langstr
import pygame, pygame_gui

class Screen:

    def __init__(self):
        self.dyn_screen = [self.run_screen()]
        self.screen     = self.dyn_screen[0]
        self.gui_manag  = pygame_gui.UIManager((settings("res_x"), settings("res_y")))
        self.gui        = GUI_Helper(self.gui_manag)

    def reset(self):
        """hard refresh of screen | should reassign currently used 'screen' variable"""
        self.dyn_screen[0] = self.run_screen()
        self.screen        = self.dyn_screen[0]
        return self.screen

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

    def __init__(self, pg_gui):
        self.login__enter  = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(cells(15, 80), cells(20, 10)),
                                                         text=langstr("login__enter"),  manager=pg_gui)
        self.login_add     = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(cells(40, 80), cells(20, 10)),
                                                         text=langstr("login__add"),    manager=pg_gui)
        self.login__remove = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(cells(65, 80), cells(20, 10)),
                                                         text=langstr("login__remove"), manager=pg_gui)

    @staticmethod
    def is_clicked(event_list):
        if event_list.type == pygame_gui.UI_BUTTON_PRESSED:
            return event_list.ui_element