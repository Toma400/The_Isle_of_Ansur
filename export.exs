# --- This module is made to .zip BCS contents into shareable container ---
#
# If you want to made BCS integrable with IoA, please use 'export_intg.exs'
# script instead.

root    = File.cwd!
out     = root <> "bcs.zip"
fileset = [
  "/settings.json",
  "/bcset.exe",
  "/bcs/assets",
  "/bcs/themes",
  "/bcs/lang"
]

"Proceeding to pack BCS files into zip..." |> IO.puts

# converting to charlist, Erlang compat with :zip.create
"Preceeding to zip files:" |> IO.puts
fileset.each
|> IO.puts
#|> Enum.map(&String.to_charlist/1)

# Enum.each(fileset, fn item -> "-" <> root <> item |> IO.puts end)

#{ok, filename} = :zip.create(out, [fileset], cwd: root)