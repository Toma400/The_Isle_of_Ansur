# ------- NIM BCSET -------
import bcs/menus/entry
import bcs/operators
import bcs/img_manag
import std/strutils
import std/sequtils
import std/logging
import std/tables
import system
import nigui
import init
import os
# TODO:
# - make text under logo
# - set all widths properly, so containers take space that they are meant to take (not-context-dependent)
# - resizable elements, so as window resizes, elements resize too
# - make logo smaller
# - make "create new project" element show small box that allow you to create new project (dir) and update project list
# - make list of projects and "entering" segment that - for the time listboxes are not a thing - always enter first project
#
# - update checker (?) and button that allows you to update files?

var log = bcsInit()

try:

  for i in get_mods(PT.MODS):
    log.log(lvlInfo, "Mods browsing: [" & $i & "] found.")
  for j in get_mods(PT.PROJECTS):
    log.log(lvlInfo, "Projects browsing: [" & $j & "] found.")

  # --- BCS MAIN RUN ---
  app.init()

  var screen   = newLayoutContainer(Layout_Horizontal)
  var window   = newWindow(bcs_name)
  var skylight = Skylight(win: window, con: screen).init()
  var images   = getGuiImages()
  block:
    entryScreen(skylight, images, log) # initial screen run

    skylight.win.show()
    app.run()

except Exception:
  log.log(lvlFatal, $getCurrentExceptionMsg())

finally:
  bcsFinalisation()