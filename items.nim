import items_properties
import std/enumutils
import std/sequtils
import std/strutils
import std/os
import parsetoml
import random

randomize()

type
  Item* = object
    name     : string             # main
    origin   : Origin
    material : Material
    class    : seq[Class]
    subclass : Subclass
    attack_low     : int          # statistics
    attack_high    : int
    attack_type    : Attack
    attack_special : seq[AttackSpecial]
    quality_low  : Quality
    quality_high : Quality

proc loadItem* (file: string): Item =
    let f = parsetoml.parseFile(file)
    result.name     = f["main"]["name"].getStr("Undefined")
    result.origin   = parseEnum[Origin](f["main"]["origin"].getStr().cEnum)
    result.material = parseEnum[Material](f["main"]["material"].getStr().cEnum)
    result.subclass = parseEnum[Subclass](f["main"]["subclass"].getStr().cEnum)
    result.class    = getClasses(result.subclass)
    result.attack_low  = f["statistics"]["attack_low"].getInt()
    result.attack_high = f["statistics"]["attack_high"].getInt()
    result.attack_type = parseEnum[Attack](f["statistics"]["attack_type"].getStr().cEnum)
    result.attack_special = newSeq[AttackSpecial]() # temporarily as free
    result.quality_low  = parseEnum[Quality](f["crafting"]["quality_low"].getStr().cEnum)
    result.quality_high = parseEnum[Quality](f["crafting"]["quality_high"].getStr().cEnum)

proc gatherItems* (): OrderedTable[string, Item] =
    proc s(sta: string): string =
        return sta.toLowerAscii.replace(" ", "_")

    for f in toSeq(walkFiles("data/items/*.toml")):
        let i = loadItem(f)
        result[s(i.name)] = i

proc `$`* (i: Item): string =
    return i.name

proc debug* (i: Item): string =
    result = i.name
    result = result & "\n" & "------------------------"
    result = result & "\n" & "Origin: "   & $i.origin
    result = result & "\n" & "Material: " & $i.material
    result = result & "\n" & "Subclass: " & $i.subclass & " " & $i.class
    result = result & "\n" & "------ statistics ------"
    result = result & "\n" & "Attack: " & $i.attack_low & ".." & $i.attack_high & " [" & $i.attack_type & "]"
    result = result & "\n" & "------- crafting -------"
    result = result & "\n" & "Quality: " & $i.quality_low & ".." & $i.quality_high
    # recipe here?

proc debugEcho* (i: Item) =
    echo debug(i)
