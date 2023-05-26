# ------- NIM BCSET -------
import bcs/operators
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
    log.log(lvlInfo, "Mod overview: <" & $i & "> found.")
  for j in get_mods(PT.PROJECTS):
    log.log(lvlInfo, "Project overview: <" & $j & "> found.")

  # --- BCS MAIN RUN ---
  app.init()

  var window   = newWindow(bcs_name)
  var logo     = newImage()
  block bI: # basicInitialisation
    logo.loadFromFile("bcs/assets/graphical/bcs.png") # loading the logo
    window_update(window)                             # updating resolution

  # screens
  var landScreen = newLayoutContainer(Layout_Vertical)
  var logoScreen = newLayoutContainer(Layout_Vertical)
  block pLS: # projectListScreen
    landScreen.padding = 6      # setting screen settings
    logoScreen.padding = 6
    landScreen.add(logoScreen)  # adding screens
    window.add(landScreen)        # main screen

  var projsLabel  = newLabel(langstr("login__listbox"))
  block lB: # labelsBoard
    landScreen.add(projsLabel)
    projsLabel.yTextAlign = YTextAlign_Center
    projsLabel.minHeight   = 40

  var enterButton  = newButton(langstr("login__open"))
  var addButton    = newButton(langstr("login__add"))
  var removeButton = newButton(langstr("login__remove"))
  block bB: # buttonsBoard
    landScreen.add(enterButton)
    landScreen.add(addButton)
    landScreen.add(removeButton)

  window.show()
  app.run()

except Exception:
  log.log(lvlFatal, $getCurrentExceptionMsg())