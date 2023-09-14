import random

randomize()

type
  Quality* = enum
    Crushed, Weak, Average, Solid, Hardened, Forged
  Material* = enum
    Bronze, Iron, Golden, Steel, Diamond, Cirtain
  ItemType* = enum
    Sword, Axe, Spear
  Item* = object
    name     : string
    quality  : Quality
    material : Material
    kind     : ItemType

proc newItem* (): Item =
  result.quality  = rand(Quality.low..Quality.high)
  result.material = rand(Material.low..Material.high)
  result.kind     = rand(ItemType.low..ItemType.high)
  result.name = $result.quality & " " & $result.material & " " & $result.kind

proc `$`* (i: Item): string =
  return i.name