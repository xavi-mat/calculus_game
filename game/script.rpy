label start:
    if config.developer:
        $ _confirm_quit = False
    scene black

    menu minigames_menu:
        "Calculus":
            call calc_start

        "- END -":
            $ renpy.full_restart()

    jump minigames_menu
