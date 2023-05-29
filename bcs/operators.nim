import std/typeinfo
import std/sequtils
import system/io
import strutils
import std/os
import nigui
import utils
import json

type
  PT* = enum
    MODS, PROJECTS

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

proc window_update* (window: Window) =
  window.width    = parseInt(settings("res_x"))
  window.height   = parseInt(settings("res_y"))
  window.iconPath = bcsd() & "/bcs/assets/graphical/bcs.png"