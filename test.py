#import utils.repo_manag

# name = input("Let's delete saves for: ")
# utils.repo_manag.file_deleting("saves/" + name)

#import system.log_manag
#system.log_manag.run()

#import subprocess

#subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
#subprocess.Popen("C:\\Users\\Ryzen 5\\Desktop\\CMDer\\cmder.exe")

#print("Oh!")



######
# ABILITY / ATTRIBUTE NAMINGS
# + skills namings, as well as agility changed into that better version



####
#NEW STUFF:
#
# - toxin immunity is BOOLEAN
# - race_exclusive is LIST not STR

import pygame, sys
from pygame.locals import QUIT

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# i = 0
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     if (0, 0) < pygame.mouse.get_pos() < (10, 10):
#         i+= 1
#     print(i)
#     pygame.display.update()

import sys; sys.pycache_prefix = "_temp/cache"
from core.utils import temp_remover
temp_remover()