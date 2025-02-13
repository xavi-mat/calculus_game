screen calculus():
    vbox:
        align (0.5, 0.4)
        spacing 20
        text "level: [level] (xp: [xp])" xalign 0.5
        text "points: [points] bonus points:+[bonus_points]" xalign 0.5
        hbox:
            xalign 0.5
            text "[operation] = "
            input
        null height 20
        text "[feedback]" xalign 0.5 color feedback_color
        if streak_bonus > 0:
            text "Streak bonus: +[streak_bonus]" xalign 0.5

    if bonus_points > 1:
        timer 1:
            repeat True
            action SetVariable("bonus_points", bonus_points - 1)


    vbox:
        xalign 1.0
        for lin in log:
            text lin xalign 1.0 size 16
