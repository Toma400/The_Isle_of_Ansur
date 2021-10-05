import system.json_manag
#NUID - Numerical User ID - used for rare user identification (also: NUID key)
#IID - Item ID - used for item identification (workspace:object)
#WID - World ID - used for world/location identification (workspace:location*)
#QID - Quest ID - used for quests (workspace:quest); stored in separate group in .json
#CID - Class ID - used for class identification (workspace:object)
#RID - Race ID - used for race identification (workspace:object)
#* - optional, but if not used, then world=True in wid_conv
#---------------------------
#this section uses a bit different namings that used in json_manag:
#(rid2) - "object", argument from surface
#(element) - "attribute of object", argument from depth
#---------------------------

def wid_conv (wid, element, world=False):
  if world == False:
    if ":" not in wid:
      #ID has wrong syntax
      print ("Incorrect ID")
    else:
      wid_list = wid.split(":") #wid splitting list
      wid1 = wid_list[0] #id of workspace
      wid2 = wid_list[1] #id of object
      if wid1 == "" or wid2 == "":
        #ID has no workspace or object
        print ("Incorrect ID")
      else:
        pass
        #path = "worlds/" + wid1 + #path of object (unfinished)
        #import/return values from path
  else:
    pass
    #theoretically it can be used for some general world checking material
    #it would just check "id of workspace", therefore it is separate condition

def cid_conv (cid, element):
  if ":" not in cid:
    #ID has wrong syntax
    print ("Incorrect ID")
  else:
    cid_list = cid.split(":") #cid splitting list
    cid1 = cid_list[0] #id of workspace
    cid2 = cid_list[1] #id of object
    if cid1 == "" or cid2 == "":
      #ID has no workspace or object
      print ("Incorrect ID")
    else:
      path = "stats/" + cid1 + "/classes.json" #path of object
      #import stats.cid1.classes
      #return stats.cid1.classes.cid2.element

def rid_conv (rid, element, dict_type=False):
  if ":" not in rid:
    #ID has wrong syntax
    print ("Incorrect ID")
  else:
    rid_list = rid.split(":") #rid splitting list
    rid1 = rid_list[0] #id of workspace
    rid2 = rid_list[1] #id of object
    if rid1 == "" or rid2 == "":
      #ID has no workspace or object
      print ("Incorrect ID")
    else:
      if dict_type == True:
        return system.json_manag.json_keyread ("stats/" + rid1 + "/races.json", rid2)
      else:
        return system.json_manag.json_subread ("stats/" + rid1 + "/races.json", rid2, element)