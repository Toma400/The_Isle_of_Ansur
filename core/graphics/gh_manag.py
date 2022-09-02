from core.utils import *
import logging as log
import pygame
from PIL import Image

#========|===========================================================
# IMAGE  | General functions to work with images, such as loading
# MANAG  | them and resizing.
#========|===========================================================
# Basic:
def imgLoad(path, name="", alpha=False): #name is optional, if you want to separate folder path from file for some reason
    try:
        surface = pygame.image.load(f"{gpath}/{path}{name}")
        if alpha is False: return surface.convert()
        return surface.convert().convert_alpha()  # for transparent textures (alpha=True)
    except pygame.error: log.error(f"Error occured during loading texture from path [{gpath}/{path}{name}].")
    except FileNotFoundError: log.error(f"Texture from path [{gpath}/{path}{name}] not found.")

def imgRes(path, name, dest_x, dest_y): #path should be folder path, written like so: [stats/]
    image = Image.open(f"{gpath}/{path}{name}")
    image = image.resize((dest_x, dest_y)); image.save(f"{gpath}/{path}tmp_{name}")

# Blits:
def imgIter(screen, image):
    for x in range(svx // image.get_width() + 1):
        for y in range(svy // image.get_height() + 1):
            screen.blit(image, (x*image.get_width(), y*image.get_height()))

def imgFull(screen, folderpath, imgname): #folderpath should be written like so: [stats/]
    imgRes(folderpath, imgname, svx, svy)
    screen.blit(imgLoad(f"{folderpath}tmp_{imgname}"), (0, 0))

def imgPut(screen, folderpath, imgname, size_x, size_y, pos_x, pos_y): #size-pos should be cell%
    # folderpath should be written like so: [stats/]
    fs_x, fs_y = returnCell(size_x, size_y)
    fpos_x, fpos_y = returnCell(pos_x, pos_y)
    imgRes(folderpath, imgname, int(fs_x), int(fs_y))
    screen.blit(imgLoad(f"{folderpath}tmp_{imgname}"), (fpos_x, fpos_y))

#===========|========================================================
# CELLS     | Cell system is made to place precisely elements on the
#-----------┘ screen and adjust their size depending on resolution
# settings. It does that by separating window to 100 "cells" and
# using multiplier to percentage given, it will return proper pixel
# length for current resolution.
#===========|========================================================
# Single element:
def returnCell(pos, type):
    if type == "x": svc = svx / 100
    else: svc = svy / 100
    return pos * svc

# Double element:
def returnCells(pos_x, pos_y):
    '''Works for both positions and length/height values'''
    svxc = svx / 100; svyc = svy / 100 #finds out cell size
    return pos_x * svxc, pos_y * svyc  #returns %posi into pixel posi