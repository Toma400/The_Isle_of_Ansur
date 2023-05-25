import parsetoml

proc jsonread* () =
  echo "."

proc jsonwrite* () =
  echo "."

#
proc tomlread* (path: string): TomlValueRef =
  return parsetoml.parseFile(path)

proc tomlread* (path: string, key: string): string =
  let file = parsetoml.parseFile(path)
  return file[key].getStr()
