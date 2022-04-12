import system.cache.cache_manag as i

try:
    i.cache_brutedel()
    print("Cache clearing succeed!")
except:
    print ("Cache clearing failed!")