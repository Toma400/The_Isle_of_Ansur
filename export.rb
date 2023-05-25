# Temporary Ruby script until we get more precise Elixir ones
require 'zip'

root = Dir.pwd
out  = "bcs.zip"

fileset = [
  "settings.json",
  "bcset.exe"
]
folderset = [
  "bcs/assets",
  "bcs/themes",
  "bcs/lang"
]

def full_folder(zf, path)
    puts "|D: #{path}"
    zf.add(path, path)
    for item in Dir["#{path}/*"]
        if File.file?(item)
            puts "|F: #{item}"
            zf.get_output_stream(item) { |i| i.puts File.open(item) }
        else
            full_folder(zf, item)
        end
    end
end

if File.file?(out)
    puts "Proceeding to remove old .zip file"
    File.delete(out)
end

puts "Proceeding to pack BCS files into zip..."

begin
    zipfile = Zip::File.open("#{out}", create: true)

    puts "Preceeding to zip files and directories:"

    for item in fileset
        puts "|F: #{item}"
        zipfile.get_output_stream(item) { |i| i.puts File.open(item); }
    end
    for folder in folderset
        full_folder(zipfile, folder)
    end

    puts "Successfully zipped all BCS files!"

rescue => exception
    puts exception.backtrace
    raise
ensure
    zipfile.close()
end