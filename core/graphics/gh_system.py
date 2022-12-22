from core.file_system.repo_manag import dir_checker
from utils.text_manag import text_splitter as tspl
from system.mod_manag import mod_lister
from core.graphics.gui_objects import GUI_Helper
from core.graphics.gh_manag import *
from core.utils import *
import os, random, pygame

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
            pygame.display.set_icon(imgLoad("core/assets/visuals/", "logo.png"))
            return screen
        except pygame.error: continue

class Screen:

    def __init__(self):
        self.dyn_screen = [run_screen()]
        self.panorama   = bgm_screen()
        self.screen     = self.dyn_screen[0]
        self.objects    = GUI_Helper(self.panorama)
        self.update     = version_checker()

    def reset(self):
        """hard refresh of screen | should reassign currently used 'screen' variable"""
        self.dyn_screen[0] = run_screen()
        self.screen        = self.dyn_screen[0]
        self.objects.restart()
        return self.screen

    def gui(self, value: str):
        return self.objects.get_element(value)