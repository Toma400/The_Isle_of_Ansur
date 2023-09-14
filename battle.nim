from nimfire/utils import getScreenRes
import nimfire/colors
import nimfire/image
import nimfire/draw
import nimfire_utils
import nimfire
import entity
import items

var w = initWindow((1200, 800), "Isle of Ansur: Battle Test", bg_colour=MORNING_BLUE)

var pick_menu   = newSection(newRect((0, 0), (1200, 800), MORNING_BLUE))
var battle_menu = newSection(newRect((0, 0), (1200, 800), MORNING_BLUE))
var player = newPlayer(100, Gender.M)
var cmenu  = pick_menu      # current menu being used
# var c = newItem()
# equip(p, c)
# echo $p
var img_fem = newImage("assets/female.png")

w.drawSection(cmenu) # initial drawing (will need redrawing only when action is done)

while w.tick():
  if cmenu == pick_menu:
    w.drawImage(img_fem)
  elif cmenu == battle_menu:
    break
  else:
    break

  w.update(true)

w.finish()