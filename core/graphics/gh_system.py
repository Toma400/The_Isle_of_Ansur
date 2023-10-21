from core.file_system.repo_manag import dir_checker
from core.file_system.theme_manag import bg_handler
from core.gui.registry.gui_objects import GUI_Helper
from core.gui.registry.pgui_objects import PGUI_Helper
from core.graphics.text_manag import text_splitter as tspl
from system.mod_manag import mod_lister
from core.data.journey import Journey
from core.graphics.gh_manag import *
from core.utils import *
import os, random, pygame, pygame_gui

# Background menu image handler
def bgm_screen():
    worldpacks = mod_lister("worlds"); bgs = []
    for i in worldpacks:
        tpath = f"{gpath}/worlds/{i}/assets/backgrounds/"
        if os.path.isdir(tpath):
            files = dir_checker(tpath, "file")
            for j in files:
                if j.endswith(".jpg"): bgs.append(f"worlds/{i}/assets/backgrounds/{j}")
                if j.endswith(".png"): bgs.append(f"worlds/{i}/assets/backgrounds/{j}")
    if any("%PR_" in v for v in bgs):
        return tspl(bgp_screen(bgs), "/assets/backgrounds/", 0)
    return tspl(random.choice(bgs), "/assets/backgrounds/", 0)

# Prioritised background menu image handler
def bgp_screen(bgs: list):
    bgsp = []
    for m in bgs:
        if "%PR_" in m:
            bgsp.append(m)
    return random.choice(bgsp)

def run_screen():
    while True:
        try:
            pygame.display.quit(); pygame.display.init()

            screen = pygame.display.set_mode([scx("svx"), scx("svy")])
            pygame.display.set_caption(sysref("name"))
            pygame.display.set_icon(imgLoad(bg_handler("icon", True)[0], bg_handler("icon", True)[1]))
            return screen
        except pygame.error: continue

def run_pgui():
    return pygame_gui.UIManager((scx("svx"), scx("svy")))

class Screen:

    def __init__(self):
        self.dyn_screen = [run_screen()]            # PyGame main screen (use 'self.screen' instead)
        self.panorama   = bgm_screen()
        self.pgui       = run_pgui()                # PyGameGUI manager
        self.screen     = self.dyn_screen[0]        # Main handler for PyGame main screen
        self.objects    = GUI_Helper(self.panorama) # Registry of GUI objects
        self.pobjects   = PGUI_Helper(self.pgui)    # Registry of PyGameGUI objects
        self.update     = version_checker()         # Bool value of whether game is up-to-date
        self.clock      = pygame.time.Clock()       # Clock (mostly to hold PyGameGUI processes)
        self.journey    = Journey()                 # Main game handler

    def reset(self):
        """hard refresh of screen | should reassign currently used 'screen' variable"""
        self.dyn_screen[0] = run_screen()
        self.pgui          = run_pgui()
        self.screen        = self.dyn_screen[0]
        self.objects.restart(self.panorama)
        self.pobjects.restart(self.pgui)
        return self.screen

    def soft_reset(self):
        """soft refresh of screen | updates some elements, for example translations"""
        self.objects.restart(self.panorama)
        self.pobjects.restart(self.pgui)

    def gui(self, value: str):
        return self.objects.get_element(value)

    def get_pgui_choice(self, element: str) -> str | None:
        """Gets currently selected entry in GUI element (available only for some types)"""
        return self.pobjects.get_value(element)

    def get_pgui_index(self, element: str) -> int | None:
        """Gets currently selected entry in GUI element (available only for some types)"""
        return self.pobjects.get_element_index(element)

    def set_pgui_element(self, element: str, overwrite):
        """Overwrites GUI element's contents (available only for some types)"""
        self.pobjects.set_value(element, overwrite)

    def put_pgui(self, element: str):
        """Reveals GUI element currently being hidden"""
        self.pobjects.show_element(element)

    def reset_pgui(self, complete=False):
        """Resets PGUI elements to their default state"""
        self.pobjects.reset_selection_list_all()
        if complete:
            for i in range(0, 8):
                self.journey.stages[i] = False

    def clear_pgui(self):
        """Flushes out all visibility of elements currently shown (used by 'switch_gscr' func)"""
        self.pobjects.clear_values()
        self.pobjects.hide_elements()