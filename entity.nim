import items

type
  Gender* = enum
    M, F

type
  Entity = object
    hp*       : int
    backpack* : seq[Item]

  Player = object
    hp*       : int
    gender*   : Gender
    backpack* : seq[Item]

  EntityType = Entity | Player

proc newEntity* (hp: int): Entity =
  result.hp       = hp
  result.backpack = newSeq[Item]()

proc newPlayer* (hp: int, gn: Gender): Player =
  result.hp       = hp
  result.gender   = gn
  result.backpack = newSeq[Item]()

proc equip* (e: var EntityType, item: Item) =
  e.backpack.add(item)

proc `$`* (e: EntityType): string =
  result = $e.type & " | hp: " & $e.hp & " | equipment: " & $e.backpack