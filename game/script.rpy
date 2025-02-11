label start:
    if config.developer:
        $ _confirm_quit = False

    scene black

    # Initialize
    $ level = 1


    jump main_loop


label main_loop:

    $ result = None
    $ operation, result = get_operation(level)
    $ bonus_points = level

    call screen calculus
    $ answer = _return

    if str(result) == answer:
        $ feedback = f"Correct! {operation} = {result}"
        $ feedback_color = "#00FF00"
        $ add_xp(1)
        $ points += bonus_points
        $ log.append(f"+{bonus_points}. {feedback}")
        $ log = log[-25:]

    else:
        $ feedback = f"Wrong! {operation} = {result}, not {answer}"
        $ feedback_color = "#FF0000"

    jump main_loop
