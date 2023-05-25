import std/typeinfo
import std/sequtils
import system/io
import std/os
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
  case pt:
    of PT.MODS:     return toSeq(walkFiles("mods/"))
    of PT.PROJECTS: return toSeq(walkDirs("bcs/projects/"))