label ver_start:
    # Initialize
    python:
        for ide in range(8):
            v_bars.append(Ver_bar(ide))
        change_variations()

    jump ver_main_loop


label ver_main_loop:
    $ v_ok = True
    call screen ver_main_bars
    "POF!"
    python:
        for vb in v_bars:
            vb.value = 0
        change_variations()

    jump ver_main_loop
