from PIL import Image as PILImage
import pygame, os

gpath = os.path.dirname(os.path.abspath("battle.py"))
res_x = 900
res_y = 900

def dir_cleaner(path):
    if not os.path.isdir(f"{gpath}/_temp/img/{path}"):
        os.makedirs(f"{gpath}/_temp/img/{path}")

class Image:

    def __init__(self, path: str, name: str = ""):
        self.spath = f"{path}{name}"         # shortened path
        self.fpath = f"{gpath}/{path}{name}" # full path

    def resize(self, dest: tuple):
        dir_cleaner (f"{self.spath}")

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
    icon  = Image(path="ioa.png")
    res_x = res_x
    res_y = res_y

    def __init__(self):
        pygame.display.init()
        self.screen = set()

    def put_image (self, img: Image, pos: tuple):
        self.set().blit(img.load(), pos)

    def set(self):
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon.load())
        return self.screen

    def update(self):
        self.set().fill("#000000")

    @staticmethod
    def force_update():
        pygame.display.quit()
        pygame.display.init()