import std/logging
import os
#[ BEAUTIFUL MODULES ]#
# https://github.com/jjv360/nim-classes
# https://github.com/status-im/questionable
# https://github.com/arnetheduck/nim-results

type
  IoaProject* = object
    name*: string       #[ Name of the project ]#
    ids*:  seq[string]  #[ IDs used by project ]#
    log*:  FileLogger   #[ Logger utility ]#

proc loadIDs (pj_name: string): seq[string] =
  var ids = newSeq[string]()
  for kind, path in walkDir("bcs/projects/" & pj_name, true):
    case kind:
      of pcDir: ids.add(path)
      else:     discard
  return ids

proc newID (pj: var IoaProject, id: string) =
  if not " " in id:
    createDir("bcs/projects/" & pj.name & "/" & id)
    pj.ids.add(id)

#[ syntactic sugar function to ease logging system ]#
proc lge* (pj: var IoaProject, lvl: Level, text: string) =
  pj.log.log(lvl, text)

proc buildProject* (pj_name: string, log: FileLogger): IoaProject =
  return IoaProject(name: pj_name,
                    ids:  loadIDs(pj_name),
                    log:  log)