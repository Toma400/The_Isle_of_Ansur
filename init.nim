import bcs/operators
import std/algorithm
import std/strutils
import std/sequtils
import std/logging
import std/times
import os

# --- UTIL ELEMENTS ---
const bcs_name* = "Baedoor Creation Set"
const bcs_ver*  = "1.0.0-pre"
# BCS Versioning (IoA cycles)
# 1.x - 0
# 2.x - 1..3
# 3.x - 4..5
# 4.x - 6..7..
let lnm = "bcs/logs/" & format(now(), "yyyy MM dd HH mm").replace(" ", "_") & ".log"

proc bcsInit* (): FileLogger =
  # --- LOGGING & CHECKING INTEGRITY ---
  # Constructing base folders
  if not dirExists("mods"):         createDir("mods")
  if not dirExists("bcs/logs"):     createDir("bcs/logs")
  if not dirExists("bcs/projects"): createDir("bcs/projects")

  # Initialising log system
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

  return log

proc bcsFinalisation* (rm_all = false) =
  # --- Removing of redundant logs ---
  var logs = toSeq(walkFiles("bcs/logs/*.log")); logs.sort
  if rm_all == false:
    let lim  = parseInt(settings("log_limit"))
    if logs.len > lim:
      let del_num = logs.len - lim
      for ui in 0 ..< del_num:
        removeFile(logs[ui])
  else:
    for u in logs: removeFile(u)