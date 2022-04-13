import system.cache.cache_manag as i

from gui.menu import pack_unloader as p

#import climage
#i = climage.convert("utils/assets/icon.ico")
#print (i)

#from utils.text_manag import colour_formatter as format

#print(format("green", "███"))

#from PIL import Image
#i = Image.open("utils/assets/icon.ico")
#i.show()

import utils.repo_manag

name = input("Let's delete saves for: ")
utils.repo_manag.file_deleting("saves/" + name)
