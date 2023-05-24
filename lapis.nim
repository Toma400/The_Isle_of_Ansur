import std/sequtils
import std/tables
import strutils
import sugar
import os

#-------------------------------------------------------------
# FILE OPERATIONS
#-------------------------------------------------------------
# allows for simpler getting of directiories names from folder
proc get_files* (path: string): seq[string] =
  let fs = toSeq(walkDir(path, relative=true))
  let files = collect(newSeq):
    for item in fs:
      item[1]
  return files

#-------------------------------------------------------------
# TYPE OPERATIONS & QOL
#-------------------------------------------------------------
# allows for easy, table-driven concaternation of strings
proc conc* (cont: OrderedTable): string =
  var clean_table: seq[string] = @[]
  var ret_str: string = ""
  for i in cont.keys:
    if i.type() is int:
      clean_table.add(cont[i])
  for j in clean_table:
    ret_str.add(j)
  return ret_str

# shortened function name for 'intToStr'
proc ts* (i: int): string =
  return intToStr(i)

# shortened function name for 'parseInt'
proc ti* (s: string): int =
  return parseInt(s)