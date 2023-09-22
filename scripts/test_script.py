from core.scripts import ioaScript
from core.graphics.gh_manag import rendPut, imgPutRes, returnCell, revCell, ratioCell, Image, NestedImage
from core.graphics.text_manag import put_rectext, put_text, Text
from core.graphics.lb_manag import put_listbox, preset_list, ListBox, ListBoxPattern
from core.utils import refunc as rei
from core.utils import scx
#=======================================
# Script has to import ioaScript class ^
# and use it for parenting V
#=======================================
class TestScript(ioaScript):

    event = "MENU" # name of the event when script should be run

    #====================================================================
    # run() function is where IoA will search for code when event is run
    #-----------------------------
    # Arguments for run() can be:
    #-----------------------------
    # *args - put it always, even if arguments below are used:
    #---
    # screen    - if you want to interfere with screen
    # pg_events - if you want to use PyGame events
    # fg_events - if you want to access IoA events
    #====================================================================
    def run(self, screen, pg_events, fg_events, fg_core, *args, **kwargs):

        pass

        #list_of_data = [
        #    {"left_pic":  "skill_1.jpg",
        #     "right_pic": "logo.png"},
        #
        #    {"left_pic":  "skill_2.jpg",
        #     "right_pic": "logo.png"},
        #
        #    {"left_pic":  "skill_3.jpg",
        #     "right_pic": "logo.png"}
        #]

        #for i in list_of_data:
        #    idict = list_of_data[i]
        #    ij = idict["left_pic"]
        #    ik = idict["right_pic"]
        #    example_pattern = [
        #    #   pattern_builder(PatternType.IMAGE, path="core/assets/visuals/", file=ij, pos=(0, 0, 20, 100))   # <--- needs "ratio" type of positioning (but for nested stuff)
        #    #   pattern_builder(PatternType.IMAGE, path="core/assets/visuals/", file=ik, pos=(20, 0, 100, 100))
        #    ]

        #aldt = ListBoxPattern(None).build_element(None, None)

            # alv = fg_core.gui("menu__gh_test").put(screen)
            # alv.pressed(screen)
            # print(alv.selected)
        # print(f"""
        # MATH COMPARISON:
        #
        # Screen resolution: ({scx('svx')}, {scx('svy')})
        # Elements limit:    ({scx('lbam')}
        #
        # ===============================
        # EXPECTED VALUES
        # Rect given (%)  = (10%:x, 10%:y, 30%:x, 50%:y) [x/y = resolution]
        # Rect given (px) = (100  , 70   , 300  , 350  )
        #
        # ACHIEVED VALUES
        # Rect given (px) = {alv.mnrect}
        #
        # ===============================
        # EXPECTED SIZE VALUES
        # Rect size (px) = (200, 280)                    [substr: 2-1, 4-3]
        #
        # ACHIEVED SIZE VALUES
        # Rect size (px) = {alv.mnrectsize}
        #
        # ===============================
        # EXPECTED RATIO
        # Ratio size (%)  = (10%:RSx)   (10%:RSy)
        # Ratio size (px) = (20)        (28)
        #
        # ACHIEVED RATIO
        # Ratio size (px) = {alv.lb_ratio(10, 0)} | {alv.lb_ratio(10, 1)}
        #
        # ===============================
        # EXPECTED ENTRY VALUES
        # Rect requested (%)  = (RSx <> RSy / {scx('lbam')})
        # Rect requested (px) = (200 <> 280 / {scx('lbam')})
        #                              ({280 // scx('lbam')})
        #
        # ACHIEVED ENTRY VALUES
        # Rect requested (px) = {alv.enrectsize}
        # """)
        #print(alv.collision(screen))
        #print(alv.elements)

        #i = [NestedImage("core/assets/visuals/", "skill_1.jpg", (0, 0, ratioCell(10), 10)),
        #     NestedImage("core/assets/visuals/", "skill_1.jpg", (ratioCell(10), 10, ratioCell(20), 20)),
        #     NestedImage("core/assets/visuals/", "skill_1.jpg", (ratioCell(20), 20, ratioCell(30), 30))]


        #i = [NestedImage("core/assets/visuals/", "skill_1.jpg", (10, 10, 20, 20))]
        #for j in i:
        #   print (j.__init__.__doc__)
        #   print (j.__dict__)
        #   j.nest(nestpos=(0+5, 0+5, 10+5, 10+5)).sup()
        #   print (j.__dict__)
        #   j.inspect()
        #   print ("----------")


        #   j.put(screen)

        #i = ListBox(main_rect=(0, 0, 50, 100))
        #i.inspect()
        #i.build_pattern(PatternType.IMAGE, pos=(0, 0, 0, 0))

        # CELL POSITIONING
        # MOVE SHOULD ALSO USE RELATIVE (+/-) FORMS
        # COLLIDER
        # RESIZE

        # LANGSTRINGS NEED TO UPDATE RECTS? (COLLISION)

    #====================================================================
    # You need to create __init__() function and make it return super()
    def __init__(self):
        super().__init__()