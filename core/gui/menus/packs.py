
def packMenu(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    pass

    # OLD RUBBISH:
    #
    # dyn_screen.gui("menu__gh_background").full().put(screen)
    #
    # put_text(screen, text=langstring("menu__button_packs"),       font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
    # #gt1 = put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#4E3510")
    # #gt2 = put_text(screen, text=langstring("menu__sett_tech"),    font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#4E3510")
    # gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    #
    # #==================================================
    # # hovering & clicking events
    # #if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
    # #    put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")
    # #    if mouseRec(pg_events):
    # #        guitype[1] = switch_gscr(dyn_screen, screen, "settings_general")
    #
    # #if mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
    # #    put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
    # #    if mouseRec(pg_events):
    # #        guitype[1] = switch_gscr(dyn_screen, screen, "settings_tech")
    #
    # if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
    #     put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
    #     if mouseRec(pg_events):
    #         guitype[0] = switch_gscr(dyn_screen, screen, "menu")
    #         guitype[1] = None