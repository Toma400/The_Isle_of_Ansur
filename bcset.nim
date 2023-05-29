# ------- NIM BCSET -------
import bcs/operators
import bcs/gh_manag
import std/strutils
import std/sequtils
import std/logging
import std/times
import system
import nigui
import lapis
import os

# --- UTIL ELEMENTS ---
let bcs_name = "Baedoor Creation Set"
let bcs_ver  = "1.0.0-pre"
# BCS Versioning (IoA cycles)
# 1.x - 0
# 2.x - 1..3
# 3.x - 4..5
# 4.x - 6..7..

# --- LOGGING & CHECKING INTEGRITY ---
if not dirExists("mods"):         createDir("mods")
if not dirExists("bcs/logs"):     createDir("bcs/logs")
if not dirExists("bcs/projects"): createDir("bcs/projects")
var lnm = "bcs/logs/" & format(now(), "yyyy MM dd HH mm").replace(" ", "_") & ".log"
var log = newFileLogger(lnm,
                        fmtStr="[$time] - $levelname: ")
log.log(lvlInfo, "Providing log for Baedoor Creation Set. Starting the software...")
log.log(lvlInfo, "Running " & bcs_name & ", version: " & bcs_ver)
# Integrity checking
if fileExists("settings.json"): log.log(lvlDebug, "Integrity check: Settings file found!") else: log.log(lvlError, "Integrity check: Failed to find settings file.")
if dirExists("bcs/assets"): log.log(lvlDebug, "Integrity check: Assets folder found!") else: log.log(lvlError, "Integrity check: Failed to find assets folder.")
if dirExists("bcs/themes"): log.log(lvlDebug, "Integrity check: Themes folder found!") else: log.log(lvlError, "Integrity check: Failed to find themes folder.")
if dirExists("bcs/lang"): log.log(lvlDebug, "Integrity check: Language folder found!") else: log.log(lvlError, "Integrity check: Failed to find language folder.")
if dirExists("bcs"): log.log(lvlDebug, "Integrity check: Main BCS folder found!") else: log.log(lvlError, "Integrity check: Failed to find main BCS folder.")

try:

  for i in get_mods(PT.MODS):
    log.log(lvlInfo, "Mods browsing: [" & $i & "] found.")
  for j in get_mods(PT.PROJECTS):
    log.log(lvlInfo, "Projects browsing: [" & $j & "] found.")

  # --- BCS MAIN RUN ---
  app.init()

  var window   = newWindow(bcs_name)
  var logo     = newImage()
  block bI: # basicInitialisation
    block aI: # assetsInitialisation
      logo.loadFromFile("bcs/assets/graphical/bcs.png") # loading the logo
    window_update(window)                             # updating resolution

  # screens
  var startScreen = newLayoutContainer(Layout_Horizontal)
  var landScreen  = newLayoutContainer(Layout_Vertical)
  var projScreen  = newLayoutContainer(Layout_Vertical)
  var logoScreen  = newLayoutContainer(Layout_Vertical)
  block sN: # screenNavigation
    block screenSettings:
      block landScreenSettings:
        landScreen.padding = 35
        landScreen.spacing = 3
      block projScreenSettings:
        projScreen.padding = 25
        projScreen.spacing = 3
      block logoScreenSettings:
        logoScreen.padding = 500
        logoScreen.spacing = 3
    block screenAdding:
      window.add(startScreen)     # main screen
      startScreen.add(landScreen)   # buttons
      startScreen.add(projScreen)   # project list
      startScreen.add(logoScreen)   # logo image

  var projLabel  = newLabel(langstr("login__listbox"))
  block lB: # labelsBoard
    projScreen.add(projLabel)
    projLabel.yTextAlign = YTextAlign_Center

  var projList = newComboBox(get_mods(PT.PROJECTS))
  projScreen.add(projList)

  var enterButton  = newButton(langstr("login__open"))
  var addButton    = newButton(langstr("login__add"))
  var removeButton = newButton(langstr("login__remove"))
  block bB: # buttonsBoard
    landScreen.add(enterButton)
    landScreen.add(addButton)
    landScreen.add(removeButton)

  logoScreen.onDraw = proc (event: DrawEvent) =
    let canvas = event.control.canvas
    block cO: # canvasOperations
      # canvas.areaColor = rgb(30, 30, 30) # dark grey
      # canvas.fill()
      canvas.drawImage(logo, 0, 30)

  window.show()
  app.run()

except Exception:
  log.log(lvlFatal, $getCurrentExceptionMsg())