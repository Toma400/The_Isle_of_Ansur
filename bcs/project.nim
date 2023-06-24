import std/strutils
import std/logging
import std/re
import results
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

type R = Result[int, string]

proc lpe* (pj: var IoaProject, lvl: Level, text: string)
#[-----------------------------------------------------]#
#[ MAIN BODY                                           ]#
#[-----------------------------------------------------]#
#[ --- IDs --- ]#
proc loadIDs (pj_name: string): seq[string] =
    var ids = newSeq[string]()
    for kind, path in walkDir("bcs/projects/" & pj_name, true):
      case kind:
        of pcDir: ids.add(path)
        else:     discard
    return ids

#[ Creates new project ID ]#
proc newID* (pj: var IoaProject, id: string): R =
    for l in id:
      if l notin Letters + {'_'}:
        return err("Couldn't create new ID [" & id & "] as it contained forbidden characters.")
    createDir("bcs/projects/" & pj.name & "/" & id)
    pj.lpe(lvlInfo, "Created ID [" & id & "] successfully.")
    pj.ids.add(id)
    ok(0)

#[ Syntactic sugar function to ease logging system ]#
proc lge* (pj: var IoaProject, lvl: Level, text: string) =
    pj.log.log(lvl, text)

#[ Project-dependent variant ]#
proc lpe* (pj: var IoaProject, lvl: Level, text: string) =
    pj.lge(lvl, "[" & pj.name & "] " & text)

#[ Constructor for IoaProject ]#
proc buildProject* (pj_name: string, log: FileLogger): IoaProject =
    return IoaProject(name: pj_name,
                      ids:  loadIDs(pj_name),
                      log:  log)