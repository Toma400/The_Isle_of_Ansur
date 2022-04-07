import system.json_manag as json_manag
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

#---------------------------------------------------------------
# IID_CONV
# --------
# Returns either whole item with all attributes to be referenced
# (as dict), or value of specific attribute. Default is latter.
#
# 'IID' needs to be IID type of string (mod_id:item_id)
# 'Element' is string, contains attribute being referred to
#
# 'Dict_Type' is boolean, if changed to True, redirects return
# value to dictionary. Element is no longer needed then.
#---------------------------------------------------------------
def iid_conv (iid, element, dict_type=False):
  if ":" not in iid:
    #ID has wrong syntax
    print ("Incorrect ID")
  else:
    iid_list = iid.split(":") #cid splitting list
    iid1 = iid_list[0] #id of workspace
    iid2 = iid_list[1] #id of object
    if iid1 == "" or iid2 == "":
      #ID has no workspace or object
      print ("Incorrect ID")
    else:
      if dict_type == True:
        #returns values used by object as dict
        return json_manag.json_keyread ("stats/" + iid1 + "/items.json", iid2)
      else:
        #returns values of object
        return json_manag.json_subread ("stats/" + iid1 + "/items.json", iid2, element)

def cid_conv (cid, element, dict_type=False):
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
      if dict_type == True:
        #returns values used by object as dict
        return json_manag.json_keyread ("stats/" + cid1 + "/classes.json", cid2)
      else:
        #returns values of object
        return json_manag.json_subread ("stats/" + cid1 + "/classes.json", cid2, element)

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
        #returns values used by object as dict
        return json_manag.json_keyread ("stats/" + rid1 + "/races.json", rid2)
      else:
        #returns values of object
        return json_manag.json_subread ("stats/" + rid1 + "/races.json", rid2, element)