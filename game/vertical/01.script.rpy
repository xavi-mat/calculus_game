label ver_start:
    # Initialize
    python:
        for y in range(2):
            for x in range(4):
                v_bars.append(Ver_bar(x, y))

    jump ver_main_loop


label ver_main_loop:
    show screen ver_main_bars
    "PAUSE"
    jump ver_main_loop
