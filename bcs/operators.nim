import std/typeinfo
import system/io
import std/os
import json

# --- here starts
proc bcsd* (): string =
  return getCurrentDir()

proc settings* (key: string): string =
  var file = readFile(bcsd() & "/settings.json")
  var keyr = parseJson(file)[key]
  case keyr.kind:
    of JString: return getStr(keyr)
    of JInt:    return $getInt(keyr)
    of JBool:   return $getBool(keyr)
    of JFloat:  return $getFloat(keyr)
    else:       return ""
# --- here ends

proc langstr* () =
  echo "."

proc jsonread* () =
  echo "."

proc jsonwrite* () =
  echo "."