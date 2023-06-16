import std/strutils
import std/tables
import operators
import nigui

#[-----------------------------------------------------------
 REGISTRY MANAGERS
-----------------------------------------------------------]#
const imgp_list = {
    "logo": "bcs/assets/graphical/bcs.png"
}.toTable

proc getGuiImages* (): Table[string, Image] =
  var imgl = initTable[string, Image]()
  for imgi, imgp in imgp_list:
    let img = newImage()
    img.loadFromFile(imgp)
    imgl[imgi] = img
  return imgl

#[-----------------------------------------------------------
 GRAPHIC SUPPLIERS
-----------------------------------------------------------]#
type
  AXES* = enum
    X, Y

# Returns pixels of specific % of screen passed
proc returnCell* (pos: int, axis: AXES): int =
  var svc: float
  if axis == AXES.X: svc = parseInt(settings("res_x")) / 100
  else:              svc = parseInt(settings("res_y")) / 100
  return (pos.float * svc).int

proc returnCell* (pos: float, axis: AXES): int =
  var svc: float
  if axis == AXES.X: svc = parseInt(settings("res_x")) / 100
  else:              svc = parseInt(settings("res_y")) / 100
  return (pos * svc).int

# Returns pixels of specific % of screen passed
proc returnCells* (pos_x: int, pos_y: int): seq[int] =
    return @[returnCell(pos_x, AXES.X),
             returnCell(pos_y, AXES.Y)]