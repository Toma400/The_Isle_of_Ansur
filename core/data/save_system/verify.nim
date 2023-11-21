import std/strformat
import std/strutils
import std/os
import nimpy

proc verifySave* (name: string): bool {.exportpy.} =
  let root = getCurrentDir().replace(r"\core\data\save_system", "")
  let svfl = fmt"{root}\saves\{name}"
  return true