from core.utils import *
from PIL import Image
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

def imgRes(path, name, dest_x, dest_y): # path should be folder path, written like so: [stats/]
    dir_cleaner(path)
    image = Image.open(f"{gpath}/{path}{name}")
    image = image.resize((dest_x, dest_y)); image.save(f"{gpath}/_temp/{path}{name}")

# Blits:
def imgIter(screen, image):
    for x in range(svx // image.get_width() + 1):
        for y in range(svy // image.get_height() + 1):
            screen.blit(image, (x*image.get_width(), y*image.get_height()))

def imgFull(screen, folderpath, imgname, alpha=False): # folderpath should be written like so: [stats/]
    imgRes(folderpath, imgname, svx, svy)
    screen.blit(imgLoad(f"_temp/{folderpath}{imgname}", alpha=alpha), (0, 0))

def imgPut(screen, folderpath, imgname, size_x, size_y, pos_x, pos_y, alpha=False): # size-pos should be cell%
    # folderpath should be written like so: [stats/]
    fs_x, fs_y = returnCells(size_x, size_y)
    fpos_x, fpos_y = returnCells(pos_x, pos_y)
    imgRes(folderpath, imgname, int(fs_x), int(fs_y))
    screen.blit(imgLoad(f"_temp/{folderpath}{imgname}", alpha=alpha), (fpos_x, fpos_y))

def imgPutRes(screen, folderpath, imgname, pos_x, pos_y, endpos_x, endpos_y, alpha=False): # variation where size is based on start-end ratio
    # folderpath should be written like so: [stats/]
    spos_x, spos_y = returnCells(pos_x, pos_y)
    epos_x, epos_y = returnCells(endpos_x, endpos_y)
    vx, vy = epos_x - spos_x, epos_y - spos_y # resolution is based on rectangle corners
    imgRes(folderpath, imgname, int(vx), int(vy))
    screen.blit(imgLoad(f"_temp/{folderpath}{imgname}", alpha=alpha), (spos_x, spos_y))

#===========|========================================================
# CELLS     | Cell system is made to place precisely elements on the
#-----------┘ screen and adjust their size depending on resolution
# settings. It does that by separating window to 100 "cells" and
# using multiplier to percentage given, it will return proper pixel
# length for current resolution.
#===========|========================================================
# Single element:
def returnCell(pos, axis):
    if axis == "x": svc = svx / 100
    else: svc = svy / 100
    return pos * svc

# Double element:
def returnCells(pos_x, pos_y):
    # Works for both positions and length/height values
    svxc = svx / 100; svyc = svy / 100 # finds out cell size
    return pos_x * svxc, pos_y * svyc  # returns %posi into pixel posi


#========|===========================================================
# COLLIS | Checks whether element collides with another
#========|===========================================================
# Simple mouse collider using cells:
def mouseCollider(st_x, st_y, end_x, end_y):
    pos0 = tuple(returnCells(st_x, st_y))[0] <= pygame.mouse.get_pos()[0] <= tuple(returnCells(end_x, end_y))[0]
    pos1 = tuple(returnCells(st_x, st_y))[1] <= pygame.mouse.get_pos()[1] <= tuple(returnCells(end_x, end_y))[1]
    return pos0 and pos1

# Alternative mouse collider using pixels
def mouseColliderPx(st_x, st_y, end_x, end_y):
    pos0 = (st_x, st_y)[0] <= pygame.mouse.get_pos()[0] <= (end_x, end_y)[0]
    pos1 = (st_x, st_y)[1] <= pygame.mouse.get_pos()[1] <= (end_x, end_y)[1]
    return pos0 and pos1

#========|===========================================================
# HELPER | Some helping functions to keep code cleaner
#========|===========================================================
def dir_cleaner(path):
    if not os.path.isdir(f"{gpath}/_temp/{path}"):
        os.makedirs(f"{gpath}/_temp/{path}")