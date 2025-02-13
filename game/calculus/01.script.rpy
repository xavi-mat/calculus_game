label calc_start:
    # Initialize
    $ calc_level = 1
    $ streak = 0
    $ points = 0
    $ streak_bonus = 0
    $ feedback = ""
    $ xp = 0

    jump calc_main_loop


label calc_main_loop:

    $ operation, result = calc_get_operation(calc_level)
    $ bonus_points = calc_level

    call screen calculus
    $ answer = _return

    if str(result) == answer:
        $ feedback = f"Correct! {operation} = {result}"
        $ feedback_color = "#00FF00"
        $ calc_add_xp(1)
        $ points += bonus_points
        $ log.append(f"+{bonus_points}. {feedback}")
        $ log = log[-25:]
        $ streak += 1
        $ streak_bonus = calc_get_streak_bonus(streak)
        $ points += streak_bonus

    else:
        $ feedback = f"Wrong! {operation} = {result}, not {answer}"
        $ feedback_color = "#FF0000"

    jump calc_main_loop
