# Updates all .pyd files by running them
import std/strformat
import std/strutils
import std/sequtils
import std/os

for f in toSeq(walkFiles("*.nim")):
  if f != "update.nim":
    let pyd_name = f.replace("nim", "pyd")
    let pyd_arguments = fmt"--app:lib --out:{pyd_name} --threads:on --tlsEmulation:off --passL:-static"
    discard execShellCmd("nim c " & pyd_arguments & " " & f)
    echo fmt"Generated Python-DLL library: {pyd_name}"