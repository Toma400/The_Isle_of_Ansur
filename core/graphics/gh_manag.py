from core.decorators import HelperMethod, Callable
from PIL import Image as PILImage
from operator import sub
from core.utils import *
import logging as log
import pygame

#========|===========================================================
# IMAGE  | General functions to work with images, such as loading
# MANAG  | them and resizing.
#========|===========================================================
# Basic:
def imgLoad(path, name="", alpha=False): # name is optional, if you want to separate folder path from file for some reason
    try:
        surface = pygame.image.load(f"{gpath}/{path}{name}")
        if alpha is False: return surface.convert()
        return surface.convert_alpha()  # for transparent textures (alpha=True)
    except pygame.error: log.error(f"Error occured during loading texture from path [{gpath}/{path}{name}].")
    except FileNotFoundError: log.error(f"Texture from path [{gpath}/{path}{name}] not found.")

def imgRes(path, name, dest_x, dest_y, variation=""): # path should be folder path, written like so: [stats/]
    # "variation" let you make two or three versions of the same img by naming it differently (for example: icon_name.png)
    dir_cleaner(path)
    image = PILImage.open(f"{gpath}/{path}{name}")
    image = image.resize((dest_x, dest_y)); image.save(f"{gpath}/_temp/img/{path}{variation}{name}")

# Blits:
def imgIter(screen, image):
    for x in range(scx("svx") // image.get_width() + 1):
        for y in range(scx("svy") // image.get_height() + 1):
            screen.blit(image, (x*image.get_width(), y*image.get_height()))

def imgFull(screen, folderpath, imgname, alpha=False): # folderpath should be written like so: [stats/]
    imgRes(folderpath, imgname, scx("svx"), scx("svy"))
    screen.blit(imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (0, 0))

def imgPut(screen, folderpath, imgname, size_x, size_y, pos_x, pos_y, alpha=False, no_blit=False): # size-pos should be cell%
    # folderpath should be written like so: [stats/]
    fs_x, fs_y = returnCells(size_x, size_y)
    fpos_x, fpos_y = returnCells(pos_x, pos_y)
    imgRes(folderpath, imgname, int(fs_x), int(fs_y))
    if no_blit: return imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (fpos_x, fpos_y) # for listboxes use
    else: screen.blit(imgLoad(f"_temp/img/{folderpath}{imgname}", alpha=alpha), (fpos_x, fpos_y)) # for normal use

def imgPutRes(screen, folderpath, imgname, pos_x, pos_y, endpos_x, endpos_y, alpha=False, no_blit=False, variation=""): # variation where size is based on start-end ratio
    # folderpath should be written like so: [stats/]
    spos_x, spos_y = returnCells(pos_x, pos_y)
    epos_x, epos_y = returnCells(endpos_x, endpos_y)
    vx, vy = epos_x - spos_x, epos_y - spos_y # resolution is based on rectangle corners
    imgRes(folderpath, imgname, int(vx), int(vy), variation)
    if no_blit: return imgLoad(f"_temp/img/{folderpath}{variation}{imgname}", alpha=alpha), (spos_x, spos_y) # for listboxes use
    else: screen.blit(imgLoad(f"_temp/img/{folderpath}{variation}{imgname}", alpha=alpha), (spos_x, spos_y)) # for normal use

# Blit manager (requires pyGame tuple of (image data, position tuple))
def rendPut(screen, data: tuple):
    screen.blit(data[0], data[1])

#===========|========================================================
# CELLS     | Cell system is made to place precisely elements on the
#-----------┘ screen and adjust their size depending on resolution
# settings. It does that by separating window to 100 "cells" and
# using multiplier to percentage given, it will return proper pixel
# length for current resolution.
#===========|========================================================
# Single element:
def returnCell(pos, axis):
    """Returns pixels of specific % of screen passed"""
    if axis == "x": svc = scx("svx") / 100
    else:           svc = scx("svy") / 100
    return int(pos * svc)

# Double element:
def returnCells(pos_x, pos_y):
    """Returns pixels of specific % of screen passed"""
    return returnCell(pos_x, "x"), returnCell(pos_y, "y")

# Any paired element
def iterateCells(values: tuple):
    axis = 2; values = list(values)
    for no, i in enumerate(values):
        if not axis % 2: values[no] = returnCell(i, "x")
        else:            values[no] = returnCell(i, "y")
        axis += 1
    return tuple(values)

# Pixels to cell%:
def revCell(pos, axis):
    if axis == "x": svc = scx("svx") / 100
    else:           svc = scx("svy") / 100
    return int(pos / svc)

def iterateRevCells(values: tuple):
    axis = 2; values = list(values)
    for no, i in enumerate(values):
        if not axis % 2: values[no] = revCell(i, "x")
        else:            values[no] = revCell(i, "y")
        axis += 1
    return tuple(values)

# Constructs cell% for user-given length (can be used for nested cells):
def nestCell(pos, comparation):
    svc = comparation / 100
    return pos * svc

# Constructs cell% for two user-given lengths (can be used for nested cells):
def nestCells(pos_x, pos_y, comp_x, comp_y):
    return nestCell(pos_x, comp_x), nestCell(pos_y, comp_y)

# Small function to return ratio-related aspects
def ratioCell(value: int = None, rev_mode=False):
    retval = None
    match rev_mode:
        case False: to_px = returnCell(value, "y"); retval = revCell(to_px, "x") # returns % for x-axis based on the same % of y-axis (useful for square based on y-axis)
        case True:  to_px = returnCell(value, "x"); retval = revCell(to_px, "y") # reverse to above, returns % for y-axis; much rarer use, I suppose
    return retval

#========|===========================================================
# COLLIS | Checks whether element collides with another
#========|===========================================================
# Simple mouse collider using cells:
def mouseColliderCell(st_x, st_y, end_x, end_y):
    pos0 = tuple(returnCells(st_x, st_y))[0] <= pygame.mouse.get_pos()[0] <= tuple(returnCells(end_x, end_y))[0]
    pos1 = tuple(returnCells(st_x, st_y))[1] <= pygame.mouse.get_pos()[1] <= tuple(returnCells(end_x, end_y))[1]
    return pos0 and pos1

# Alternative mouse collider using pixels
def mouseColliderPx(st_x, st_y, end_x, end_y):
    pos0 = (st_x, st_y)[0] <= pygame.mouse.get_pos()[0] <= (end_x, end_y)[0]
    pos1 = (st_x, st_y)[1] <= pygame.mouse.get_pos()[1] <= (end_x, end_y)[1]
    return pos0 and pos1

# Returns whether specific mouse button is pressed (by default = left)
def mouseRec(pg_events, mouse_button=1):
    for event in pg_events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == mouse_button:
            return True
    return False


#========|===========================================================
# HELPER | Some helping functions to keep code cleaner
#========|===========================================================
# Used to switch screen. Put this return in respective guitype[pos]
def switch_scr(screen, gui_aimed):
    screen.fill("#000000"); log.debug(f"Switching screen to guitype value: [{gui_aimed}]")
    return gui_aimed

def dir_cleaner(path):
    if not os.path.isdir(f"{gpath}/_temp/img/{path}"):
        os.makedirs(f"{gpath}/_temp/img/{path}")

#==========|========================================================
# IMAGE    | Used for objectify image features
# OBJECT   |
#          |
#==========|========================================================
class Image:

    alpha = True # transparency

    def __init__(self, path: str, file: str, pos: tuple):
        """
        path | Folder path to the image (should end with "/")
        file | File name with extension
        pos  | Coordinates of the image (tuple of two or four values). If tuple has four values, it will draw rectangle and resize image to fit within it.
             | You can use -ratioCell- to match positions to squared form:
             |    (0, 0, ratioCell(10), 10) <--- will return square of height of 10% of screen and exact width (of 10%*ratio)
        """
        self.path    = path
        self.imgname = file
        self.load    = self.reload()
        self.rawpos  = pos
        self.fpos    = len(pos) == 4           # tells if position given is rectangular (will disable optional size argument + resizing)
        self.pos     = self.pos_unpacker(pos)

        # shorteners for functions
        self.res     = self.resize

    @Callable
    def swap_alpha(self):
        """Swaps alpha of the image"""
        self.alpha = not self.alpha
        self.load  = self.reload()

    @Callable
    def resize(self, size: tuple, variation: str = ""):
        """Resizes the image, creating a copy in _temp folder. Uses px values, so returnCells() method in arguments is required to get cell% values"""
        dir_cleaner(self.path)
        image = PILImage.open(f"{self.path}{self.imgname}")

        self.path    = f"_temp/img/{self.path}"         # changing path to _temp
        self.imgname = f"{variation}{self.imgname}"     # changing img name to include variation
        image        = image.resize(size); image.save(f"{self.path}{self.imgname}")
        self.load    = self.reload()

    @Callable
    def put(self, screen):
        if not self.fpos: screen.blit(self.load, self.pos)
        else:
            self.resize(tuple(map(sub, self.pos[1], self.pos[0]))) # resizes the image to match the rectangle given
            screen.blit(self.load, self.pos[0])

    @HelperMethod
    def reload(self):
        """Main updating method after working on image file, reloads image"""
        try:
            surface = pygame.image.load(f"{gpath}/{self.path}{self.imgname}")
            if self.alpha is False: return surface.convert()
            else:                   return surface.convert_alpha()
        except pygame.error:      log.error(f"Error occured during loading texture from path [{gpath}/{self.path}{self.imgname}].")
        except FileNotFoundError: log.error(f"Texture from path [{gpath}/{self.path}{self.imgname}] not found.")

    @HelperMethod
    def pos_unpacker(self, dest_tp: tuple):
        if len(dest_tp)   == 4: return returnCells(dest_tp[0], dest_tp[1]), returnCells(dest_tp[2], dest_tp[3])
        elif len(dest_tp) == 2: return returnCells(dest_tp[0], dest_tp[1])
        else:                   raise ValueError(f"Invalid value amount for -pos- argument of Image object (should be 2 or 4). Values given: {len(dest_tp)}.")