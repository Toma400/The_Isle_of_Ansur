# ------- NIM BCSET -------
import bcs/menus/entry
import bcs/operators
import bcs/img_manag
import std/strutils
import std/sequtils
import std/logging
import std/tables
import std/times
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
if fileExists("settings.json"): log.log(lvlDebug, "Integrity check: Settings file found!")   else: log.log(lvlError, "Integrity check: Failed to find settings file.")
if dirExists("bcs/assets"):     log.log(lvlDebug, "Integrity check: Assets folder found!")   else: log.log(lvlError, "Integrity check: Failed to find assets folder.")
if dirExists("bcs/themes"):     log.log(lvlDebug, "Integrity check: Themes folder found!")   else: log.log(lvlError, "Integrity check: Failed to find themes folder.")
if dirExists("bcs/lang"):       log.log(lvlDebug, "Integrity check: Language folder found!") else: log.log(lvlError, "Integrity check: Failed to find language folder.")
if dirExists("bcs"):            log.log(lvlDebug, "Integrity check: Main BCS folder found!") else: log.log(lvlError, "Integrity check: Failed to find main BCS folder.")

try:

  for i in get_mods(PT.MODS):
    log.log(lvlInfo, "Mods browsing: [" & $i & "] found.")
  for j in get_mods(PT.PROJECTS):
    log.log(lvlInfo, "Projects browsing: [" & $j & "] found.")

  # --- BCS MAIN RUN ---
  app.init()

  var window = newWindow(bcs_name)
  var images = getGuiImages()
  block:
    window.update() # updating resolution
    entryScreen(window, images, log) # initial screen run

    window.show()
    app.run()

except Exception:
  log.log(lvlFatal, $getCurrentExceptionMsg())