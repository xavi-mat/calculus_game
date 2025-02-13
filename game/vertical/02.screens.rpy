screen ver_main_bars():
    vbox:
        text "Points: [v_points]"
        text "Bonus: +[v_bonus]"

    add Solid("#888", xysize=(1920, 2), ypos=140)
    add Solid("#888", xysize=(1920, 2), ypos=490)
    add Solid("#888", xysize=(1920, 2), ypos=590)
    add Solid("#888", xysize=(1920, 2), ypos=940)

    hbox:
        xalign 0.5
        spacing 20
        ypos 540
        for barr in v_bars:
            fixed xsize 100:
                add barr.bar
                text "[barr.letter]\n[barr.letter2]":
                    ypos -40
                    xalign 0.5
                    text_align 0.5
                    outlines [(1, "#000000")]
                key barr.letter action Function(barr.go_up)
                key barr.letter2 action Function(barr.go_down)

    timer 0.1 action Function(change_bars) repeat True
    timer 2 action Function(add_points) repeat True
    timer 10 action Function(change_variations) repeat True

    if not v_ok:
        timer 0.01 action Return()

