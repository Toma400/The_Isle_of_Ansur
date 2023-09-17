from core.file_system.repo_manag import dir_checker
from core.file_system.theme_manag import bg_handler
from core.gui.registry.gui_objects import GUI_Helper
from core.gui.registry.pgui_objects import PGUI_Helper
from utils.text_manag import text_splitter as tspl
from system.mod_manag import mod_lister
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
        self.pobjects   = PGUI_Helper()             # Registry of PyGameGUI objects
        self.update     = version_checker()         # Bool value of whether game is up-to-date
        self.clock      = pygame.time.Clock()       # Clock (mostly to hold PyGameGUI processes)

    def reset(self):
        """hard refresh of screen | should reassign currently used 'screen' variable"""
        self.dyn_screen[0] = run_screen()
        self.pgui          = run_pgui()
        self.screen        = self.dyn_screen[0]
        self.objects.restart(self.panorama)
        return self.screen

    def gui(self, value: str):
        return self.objects.get_element(value)

    def put_pgui(self, value: str):
        """Reveals GUI element currently being hidden"""
        self.pobjects.get_element(value).visible = True

    def clear_pgui(self):
        """Flushes out all visibility of elements currently shown (used by 'switch_gscr' func)"""
        for pgui_e in self.pobjects.get_elements():
            self.pobjects.get_element(pgui_e).visible = False