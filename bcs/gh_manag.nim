import std/strutils
import operators

type
  AXES* = enum
    X, Y

# Returns pixels of specific % of screen passed
proc returnCell* (pos: int, axis: AXES): float =
  var svc: float
  if axis == AXES.X: svc = parseInt(settings("res_x")) / 100
  else:              svc = parseInt(settings("res_y")) / 100
  return pos.float * svc

# Returns pixels of specific % of screen passed
proc returnCells* (pos_x: int, pos_y: int): seq[float] =
    return @[returnCell(pos_x, AXES.X),
             returnCell(pos_y, AXES.Y)]