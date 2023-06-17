import std/typeinfo
import std/sequtils
import std/logging
import std/tables
import system/io
import strutils
import std/os
import nigui
import utils
import json

# --- UTIL ELEMENTS ---
const bcs_name* = "Baedoor Creation Set"
const bcs_ver*  = "1.0.0-pre"
# BCS Versioning (IoA cycles)
# 1.x - 0
# 2.x - 1..3
# 3.x - 4..5
# 4.x - 6..7..

type
  PT* = enum
    MODS, PROJECTS
  Skylight* = object
    win*: Window
    con*: LayoutContainer
proc init* (s: Skylight): Skylight =
  s.win.add(s.con)
  s.con.setSize(s.win.width, s.win.height)
  return s

# --- here starts
proc bcsd* (): string =
  return getCurrentDir()

proc settings* (key: string): string =
  let file = readFile(bcsd() & "/settings.json")
  let keyr = parseJson(file)[key]
  case keyr.kind:
    of JString: return getStr(keyr)
    of JInt:    return $getInt(keyr)
    of JBool:   return $getBool(keyr)
    of JFloat:  return $getFloat(keyr)
    else:       return ""
# --- here ends

proc langstr* (key: string): string =
  proc langlist (keyword: string): string =
    case keyword:
      of "english": return "en_us"
      of "polish":  return "pl_pl"

  let lang = langlist(settings("language"))
  return tomlread(bcsd() & "/bcs/lang/" & lang & ".toml", key)

proc get_mods* (pt: PT): seq[string] =
  proc rm_tail (sq: seq[string], tail: string): seq[string] = # removes "tail" from every item from sequence
    var sq_wt: seq[string]
    for ti in sq:
      sq_wt.add(ti.replace(tail, ""))
    return sq_wt

  case pt:
    of PT.MODS:     return rm_tail(toSeq(walkFiles("mods/*")),        tail=r"mods\")
    of PT.PROJECTS: return rm_tail(toSeq(walkDirs("bcs/projects/*")), tail=r"bcs\projects\")

proc windowInit* (window: Window, res = (0, 0)) =
  if res == (0, 0):
    window.width    = parseInt(settings("res_x"))
    window.height   = parseInt(settings("res_y"))
  else:
    window.width    = res[0]
    window.height   = res[1]
  window.iconPath = bcsd() & "/bcs/assets/graphical/bcs.png"

proc windowUpdate* (skylight: Skylight, name = bcs_name) =
  for sub in skylight.con.childControls:
    skylight.con.remove(sub)
  skylight.win.title = name