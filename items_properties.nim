import std/strutils
import std/unicode
import std/tables

type
  Origin* = enum
    Baedoorian
    # foreign
    Desolatus
  Material* = enum
    Bronze
    Iron
    Golden
    Steel
    Diamond
    Cirtain
    # foreign
    Scarabia
  Quality* = enum
    Broken
    Weak
    Average
    Solid
    Sturdy
    Hardened
    Forged
  Class* = enum
    Sword
    Axe
    Spear
    Ranged
    Crossbow
    Bow
    Firearm
  Subclass* = enum
    Longsword
    Shortsword
    Battleaxe
    Javelin
    Shortbow
    Longbow
    HeavyCrossbow
    Revolver
    Shotgun
    Rifle
  Attack* = enum
    Slash
    Pierce
    Blunt
  AttackSpecial* = enum
    Fire
    Ice
    Thunder
    Water
    Earth
    Air
    Soul
    Void

proc getClasses* (sc: Subclass): seq[Class] =
    const valid = {
                    Battleaxe:     @[Axe],
                    Javelin:       @[Spear, Ranged],
                    Longsword:     @[Sword],
                    Shortsword:    @[Sword],
                    Shortbow:      @[Bow, Ranged],
                    Longbow:       @[Bow, Ranged],
                    HeavyCrossbow: @[Crossbow, Ranged],
                    Revolver:      @[Firearm, Ranged],
                    Shotgun:       @[Firearm, Ranged],
                    Rifle:         @[Firearm, Ranged]
                  }.toTable
    return valid[sc]

proc cEnum* (s: string): string =
    return s.capitalize().replace("_", "")