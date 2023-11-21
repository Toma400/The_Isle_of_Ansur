# Updates all .pyd files by running them
import std/private/osdirs
import std/strformat
import std/strutils
import std/sequtils
import std/os

const custom = ["core/data/save_system/verify.nim"]
let   root   = getCurrentDir().replace(r"\core\libs", "")

proc generatePYD (fl: string) =
    let pyd_name      = fl.replace("nim", "pyd")
    let pyd_arguments = fmt"--app:lib --out:{pyd_name} --threads:on --tlsEmulation:off --passL:-static"
    try:
      discard execShellCmd(fmt"nim c {pyd_arguments} {fl}")
      echo fmt"Generated Python-DLL library: {pyd_name}"
    except:
      echo fmt"Couldn't generate Python-DLL library: {pyd_name}. Error stacktrace: {getCurrentException().msg}"

for f in toSeq(walkFiles("*.nim")):
    if f != "update.nim":
      generatePYD(f)

for c in custom:
    let c_path = "\"" & fmt"{root}\{c}" & "\""
    generatePYD(c_path)