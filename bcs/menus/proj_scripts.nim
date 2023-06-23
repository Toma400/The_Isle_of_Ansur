import ../../bcs/operators
import std/logging
import std/tables
import nigui

const fu_formats = {"Ruby":   "rb",          #[Future formats that may be used]#
                    "Lua":    "lua",
                    "Nim":    "nims",
                    "Tribal": "rin",
                    "Elixir": "exs"}.toTable
const formats    = {"Python": "py"}.toTable  #[Script formats available with their extensions]#

proc scriptScreen* (skylight: Skylight, images: Table[string, Image], log: FileLogger, pj_name: string) =
    discard

proc scriptSettings* () =
    discard

proc scriptReg* () =
    discard

proc scriptDraw* () =
    discard

proc scriptEvents* () =
    discard