# Updates all .pyd files by running them
import std/sequtils
import std/os

const pyd_arguments = "--app:lib --out:example.pyd --threads:on --tlsEmulation:off --passL:-static"

for f in toSeq(walkFiles("*.nim")):
  if f != "update.nim":
    discard execShellCmd("nim c " & pyd_arguments & " " & f)