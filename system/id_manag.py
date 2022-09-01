import system.json_manag as json_manag
import logging as log
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
    if ":" not in wid: log.warning (f"Requested WID: [{wid}] has incorrect value") #ID has wrong syntax
    else:
      wid_list = wid.split(":") #wid splitting list
      wid1 = wid_list[0] #id of workspace
      wid2 = wid_list[1] #id of object
      if wid1 == "" or wid2 == "": log.warning (f"Requested WID: [{wid}] has incorrect value") #ID has no workspace or object
      else:
        pass
        #path = "worlds/" + wid1 + #path of object (unfinished)
        #import/return values from path
  else:
    pass
    #theoretically it can be used for some general world checking material
    #it would just check "id of workspace", therefore it is separate condition

#=============|=====================================================
# CONVERTERS  | Returns either whole item with all attributes to be
#             | referenced, or value of specific attribute.
#=============|
# First takes only one value (ID), whereas second - two
# (ID and Element).
# 'ID' needs to be Ansur ID type of string (mod_id:item_id)
# 'Element' is string, contains attribute being referred to.
#===================================================================
def iid_conv (iid, element=None):
  if ":" not in iid: log.warning (f"Requested IID: [{iid}] has incorrect value") #ID has wrong syntax
  else:
    iid_list = iid.split(":") #cid splitting list
    iid1 = iid_list[0] #id of workspace
    iid2 = iid_list[1] #id of object
    if iid1 == "" or iid2 == "": log.warning (f"Requested IID: [{iid}] has incorrect value") #ID has no workspace or object
    else:
      if element is None:
        return json_manag.json_keyread (f"stats/{iid1}/items.json", iid2) #returns values used by object as dict
      else:
        return json_manag.json_subread (f"stats/{iid1}/items.json", iid2, element) #returns selected value of object

def cid_conv (cid, element=None):
  if ":" not in cid: log.warning (f"Requested CID: [{cid}] has incorrect value") #ID has wrong syntax
  else:
    cid_list = cid.split(":") #cid splitting list
    cid1 = cid_list[0] #id of workspace
    cid2 = cid_list[1] #id of object
    if cid1 == "" or cid2 == "": log.warning (f"Requested CID: [{cid}] has incorrect value") #ID has no workspace or object
    else:
      if element is None:
        return json_manag.json_keyread (f"stats/{cid1}/classes.json", cid2) #returns values used by object as dict
      else:
        return json_manag.json_subread (f"stats/{cid1}/classes.json", cid2, element) #returns selected value of object

def rid_conv (rid, element=None):
  if ":" not in rid: log.warning (f"Requested RID: [{rid}] has incorrect value") #ID has wrong syntax
  else:
    rid_list = rid.split(":") #rid splitting list
    rid1 = rid_list[0] #id of workspace
    rid2 = rid_list[1] #id of object
    if rid1 == "" or rid2 == "": log.warning (f"Requested RID: [{rid}] has incorrect value") #ID has no workspace or object
    else:
      if element is None:
        return json_manag.json_keyread (f"stats/{rid1}/races.json", rid2) #returns values used by object as dict
      else:
        return json_manag.json_subread (f"stats/{rid1}/races.json", rid2, element) #returns selected value of object

def id_splitter (id_to_split, position: int = None):
  '''Position let you choose either mod id [0] or element of id [1]'''
  id_list = id_to_split.split(":")
  if position is None: return id_list #returns full ID [mod_id:item_id]
  else: return id_list[position] #returns either mod ID [pos=0] or item ID [pos=1]