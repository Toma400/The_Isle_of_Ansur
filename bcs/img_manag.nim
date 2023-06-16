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

# Calculates percents depending on context (nestedCell, kind of)
proc parseCell (pos: int, context: int): int =
  var svc = context / 100
  return (pos.float * svc).int

# Returns pixels of specific % of screen passed
proc returnCell* (pos: int, axis: AXES, context = 0): int =
  var svc: float
  if context == 0:
    if axis == AXES.X: svc = parseInt(settings("res_x")) / 100
    else:              svc = parseInt(settings("res_y")) / 100
    return (pos.float * svc).int
  else:
    return parseCell(pos, context)

proc returnCell* (pos: float, axis: AXES, context = 0): int =
  var svc: float
  if context == 0:
    if axis == AXES.X: svc = parseInt(settings("res_x")) / 100
    else:              svc = parseInt(settings("res_y")) / 100
    return (pos * svc).int
  else:
    return parseCell(pos.int, context)

# Returns pixels of specific % of screen passed
proc returnCells* (pos_x: int, pos_y: int): seq[int] =
    return @[returnCell(pos_x, AXES.X),
             returnCell(pos_y, AXES.Y)]

# Performs adjustment of container elements; 'it' shortens
proc returnAdjCell* (pos: int, axis: AXES, it = 1, context = 0): int =
  returnCell(pos-(1*it), axis, context)