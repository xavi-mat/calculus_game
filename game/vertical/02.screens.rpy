screen ver_main_bars():
    hbox:
        xalign 0.5
        spacing 20
        ypos 500
        for barr in v_bars:
            add barr.bar

    timer 0.1 action Function(change_bars) repeat True
