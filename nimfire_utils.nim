import nimfire/draw
import nimfire/types
import std/tables

type
  Section = object
    mr: Rect                # main Rect (background)
    lr: Table[string, Rect] # seq of Rects

proc newSection* (r: Rect): Section =
    result.mr = r
    result.lr = initTable[string, Rect]()

proc registerRect* (s: var Section, id: string, r: Rect) =
    s.lr[id] = r

proc drawSection* (w: var Window, s: Section) =
    w.drawRect(s.mr)
    for rk in s.lr.keys:
      w.drawRect(s.lr[rk])