from core.decorators import Deprecated
from core.utils import *
from enum import Enum

class Axis(Enum):
    X = 0,
    Y = 1

def toPx(pc: int, context: int) -> int:
    """Agnostic function that returns % -> px conversion from specific context"""
    svc = context / 100
    return int(pc * svc)

def toPxX(pc: int) -> int:
    """Returns % -> px conversion from X axis"""
    return toPx(pc, scx("svx"))

def toPxY(pc: int) -> int:
    """Returns % -> px conversion from Y axis"""
    return toPx(pc, scx("svy"))

def toPxXY(pc_x: int, pc_y: int) -> (int, int):
    """Returns pixels of specific % of screen passed. Prefer use of toPxX/toPxY if used repeatedly, for performance reasons"""
    return toPxX(pc_x), toPxY(pc_y)

@Deprecated("toPxX/toPxY")
def returnCell(pos: int, axis: Axis) -> int:
    """Returns pixels of specific % of screen passed. Legacy-compatibile, but should be set to toPxX/toPxY"""
    match axis:
        case Axis.X: svc = scx("svx") / 100
        case Axis.Y: svc = scx("svy") / 100
    return int(pos * svc)

@Deprecated("toPxXY")
def returnCells(pos_x: int, pos_y: int) -> (int, int):
    """Returns pixels of specific % of screen passed. Legacy-compatibile, but should be set to toPxXY to match naming"""
    return toPxX(pos_x), toPxY(pos_y)
