# ------- NIM BCSET -------
import bcs/operators
import std/strutils
import std/sequtils
import std/logging
import std/times
import system
import nigui # either this
import lapis
import os

# --- LOGGING & CHECKING INTEGRITY ---
if not dirExists("mods"):         createDir("mods")
if not dirExists("bcs/logs"):     createDir("bcs/logs")
if not dirExists("bcs/projects"): createDir("bcs/projects")
var lnm = "bcs/logs/" & format(now(), "yyyy MM dd HH mm").replace(" ", "_") & ".log"
var log = newFileLogger(lnm,
                        fmtStr="[$time] - $levelname: ")
log.log(lvlInfo, "Providing log for Baedoor Creation Set. Starting the software...")
# Integrity checking
if fileExists("settings.json"): log.log(lvlDebug, "Integrity check: Settings file found!") else: log.log(lvlError, "Integrity check: Failed to find settings file.")
if dirExists("bcs/assets"): log.log(lvlDebug, "Integrity check: Assets folder found!") else: log.log(lvlError, "Integrity check: Failed to find assets folder.")
if dirExists("bcs/themes"): log.log(lvlDebug, "Integrity check: Themes folder found!") else: log.log(lvlError, "Integrity check: Failed to find themes folder.")
if dirExists("bcs/lang"): log.log(lvlDebug, "Integrity check: Language folder found!") else: log.log(lvlError, "Integrity check: Failed to find language folder.")
if dirExists("bcs"): log.log(lvlDebug, "Integrity check: Main BCS folder found!") else: log.log(lvlError, "Integrity check: Failed to find main BCS folder.")

try:
  # --- UTIL ELEMENTS ---
  let bcs_name = "Baedoor Creation Set"

  for i in get_mods(PT.MODS):
    log.log(lvlInfo, "Mod overview: <" & $i & "> found.")
  for j in get_mods(PT.PROJECTS):
    log.log(lvlInfo, "Project overview: <" & $j & "> found.")

  # --- BCS MAIN RUN ---
  app.init()

  var window = newWindow(bcs_name)
  block wS: # windowScreen
    window.width    = ti(settings("res_x"))
    window.height   = ti(settings("res_y"))
    window.iconPath = bcsd() & "/bcs/assets/graphical/bcs.png"

  var landScreen = newLayoutContainer(Layout_Vertical)
  # var logoScreen = newLayoutContainer(Layout_Vertical)
  block pLS: # projectListScreen
    landScreen.padding = 6
    # logoScreen.padding = 6
    window.add(landScreen)
    # projScreen.add(logoScreen)

  var projsLabel  = newLabel(langstr("login__listbox"))
  block lB: # labelsBoard
    landScreen.add(projsLabel)
    projsLabel.minHeight = 50

  var enterButton  = newButton(langstr("login__open"))
  var addButton    = newButton(langstr("login__add"))
  var removeButton = newButton(langstr("login__remove"))
  block bB: # buttonsBoard
    landScreen.add(enterButton)
    landScreen.add(addButton)
    landScreen.add(removeButton)

  # var logoCnv = newCanvas()
  # var logoImg = newImage()
  # block lI:
  #   logoImg.loadFromFile(bcsd() & "bcs/assets/graphical/bcsx.png")
  #   logoCnv.drawImage(logoImg)
  #   window.add(logoCnv)

  window.show()
  app.run()

except Exception:
  log.log(lvlFatal, $getCurrentExceptionMsg())