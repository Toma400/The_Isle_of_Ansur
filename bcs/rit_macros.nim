import std/strutils
import std/macros
import std/tables
import system/io
#[-------------------------------------------------------------]#
#[ RIT MACROS & UTILS                                          ]#
#[-------------------------------------------------------------]#
#[ Rit Macros                                                  ]#
#[--------------                                               ]#
#[ whisper(str) - prints into termina. Alias for echo()        ]#
#[ scribe(str)  - returns terminal input. Alias for readLine() ]#
#[ to!bool(T)   - returns bool value of uncommonly used type   ]#
#[ to!int(T)    - returns int value of uncommonly used type    ]#
#[-------------------------------------------------------------]#
#[ lore aliases ]#
proc whisper* (text: string) =
    echo(text)
proc scribe* (text: string = ""): string =
    if text != "": echo(text)
    return readLine(stdin)
#[ conversions ]#
# proc `to!bool`* (i: int): bool =
#     case i:
#       of 0: return false
#       else: return true
# proc `to!bool`* (f: float): bool =
#     case f.int:
#       of 0: return false
#       else: return true
# proc `to!bool`* (s: string): bool =
#     case s:
#       of "": return false
#       else:  return true
# proc `to!bool`* (i: seq[any]): bool =
#     return i.len() > 0
# proc `to!bool`* (i: array[any, any]): bool =
#     return i.len() > 0
# proc `to!bool`* (i: Table[any]): bool =
#     return i.len() > 0
# proc `to!bool`* (i: OrderedTable[any]): bool =
#     return i.len() > 0
# proc `to!bool`* (i: CountTable[any]): bool =
#     return i.len() > 0
# proc `to!int`* (b: bool): int =
#     case b:
#       of true:  return 1
#       of false: return 0
# proc `to!int`* (s: string): int =
#     return parseInt(s)

# type #[ simple generic type ]#
#   T = string or int or float or bool or seq[any]
#
# type
#   pair* = tuple
#     first:  T
#     second: T
#   triad* = tuple
#     first:  T
#     second: T
#     third:  T


#[ checks iterables for T ]#
proc `contains?`* (): bool =
  discard

# macro myAssert(arg: untyped): untyped =
#   echo arg.treeRepr
#
# myAssert(" " & a & b & " ")
# macro `eternal`(arg: untyped): untyped =
#   let t = nnkStmtList(true)
#
#   result = quote do:
#     while `t`:
#       `ntyEmpty`
#
# var i = 1
# eternal:
#   if i < 5:
#     echo $i
#     i += 1
#   else:
#     break

dumpTree:
  while true:
    discard
  #[
  eternal:
    void
  ]#

  var a = 5
  #[
  a << 5
  ]#

  some_list.add(element)
  #[
  some_list <! element
  ]#
  #[
  in a way it is also:
  add() <: some list, element
  ]#

  proc a (i: string, j: string): string =
    return i & j
  #[
  town a (i: string, j: string) >> string =
    i & j >>

  or

  town a (i: string, j: string) >> string {
    i & j >>
  }
  ]#

  `???`
  #[
  |: documentation
  ]#

  {. Deprecated .}
  #[
  @Deprecated
  ]#

  "test" & $n & $m & "concat"
  #[
  "{n}{m}"     |> to get '{' and '}', you need to use escape sign
  ]#