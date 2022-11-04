from PIL import Image as PILImage
from elements.utils import *
import pygame, os

gpath = os.path.dirname(os.path.abspath("battle.py"))
res_x = 900
res_y = 900

def dir_cleaner(path):
    if not os.path.isdir(f"{gpath}/_temp/img/{path}"):
        os.makedirs(f"{gpath}/_temp/img/{path}")

class Image:

    def __init__(self, path: str, name: str):
        self.ipath = path                    # img path
        self.iname = name                    # img name
        self.spath = f"{path}{name}"         # shortened path
        self.fpath = f"{gpath}/{path}{name}" # full path

    def resize(self, dest: tuple):
        dir_cleaner (f"{self.ipath}")

        # PIL operation on file
        image = PILImage.open(self.fpath)
        image = image.resize(dest)
        image.save(f"{gpath}/_temp/img/{self.spath}")

        # realigning path to new file
        self.fpath = f"{gpath}/_temp/img/{self.spath}"

    def load(self):
        surface = pygame.image.load(self.fpath)
        return surface.convert_alpha()

class Screen:

    title = "BattleTest"
    icon  = Image(path="", name="ioa.png")
    res_x = res_x
    res_y = res_y

    def __init__(self):
        pygame.display.init()
        self.tick   = 0
        self.screen = set()

    def put_image (self, img: Image, pos: tuple):
        if self.get_tick("M"):
            cellpos = returnCells(pos)
            self.set().blit(img.load(), cellpos)
            return img

    def set(self):
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon.load())
        return self.screen

    def ticking(self):
        self.tick += 1

    def get_tick(self, mode="M"):
        match mode:
            case "M": return self.tick % 2 == 0
            case "S": return self.tick % 2500 == 0

    def update(self):
        self.set().fill("#000000")

    @staticmethod
    def force_update():
        pygame.display.quit()
        pygame.display.init()

class Menu:

    def __init__(self, screen: Screen):
        self.screen_list = [screen]
        self.screen      = self.screen_list[0]
        self.menus       = (None, None, None, None, None) # handler for menu types (0 - main, 1-4 - submenus)

class Button:

    def __init__(self, size: tuple, pos: tuple, img: Image, screen: Screen):
        self.size   = returnCells(size)
        self.rawpos = pos
        self.pos    = returnCells(pos)
        self.img    = img
        self.rect   = pygame.rect.Rect((self.pos[0], self.pos[1]),
                                       (self.size[0], self.size[1]))

        self.img.resize(self.size)
        screen.put_image(self.img, self.rawpos)

    def is_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]