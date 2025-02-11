screen calculus():
    vbox:
        align (0.5, 0.4)
        spacing 20
        text "level: [level] (xp: [xp])" xalign 0.5
        hbox:
            xalign 0.5
            text "[operation] = "
            input
        null height 20
        text "[feedback]" xalign 0.5 color feedback_color
