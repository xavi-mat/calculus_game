v_bonus = 0
v_points = 0
renpy = None
Solid = None
v_bars = []
v_ok = True

"""renpy
init python:
"""

V_MAX_VALUE = 400
COLORS = [
    "#800", "#080", "#008", "#880", "#808", "#088",
    "#F00", "#0F0", "#00F", "#FF0", "#F0F", "#0FF",
]
V_MAX_RAND = 3

# CLASSES
class Ver_bar:
    def __init__(self, ide):
        self.ide = ide
        self.letter = "QWERTYUI"[ide]
        self.letter2 = "ASDFGHJK"[ide]
        self.value = 0
        self.variation = 0
        self.color = "#FFF"

    @property
    def abs_value(self):
        return abs(self.value)

    @property
    def bar(self):
        value = self.abs_value
        if value == 0:
            value = 1
        yoffset = 0
        if self.value > 0:
            yoffset = -value
        return Solid(self.color, xsize=100, ysize=value, yoffset=yoffset)

    def change(self):
        self.value += self.variation

    def go_up(self):
        self.variation += 1

    def go_down(self):
        self.variation -= 1


# FUNCTIONS
def change_bars():
    global v_ok
    for vb in v_bars:
        vb.change()
        if abs(vb.value) > V_MAX_VALUE:
            v_ok = False
            break

def change_variations():
    for vb in v_bars:
        vb.variation = renpy.random.randint(-V_MAX_RAND, V_MAX_RAND)
        vb.color = COLORS[renpy.random.randrange(len(COLORS))]

def add_points():
    global v_points, v_bonus
    v_bonus = 0
    for vb in v_bars:
        if vb.abs_value < 10:
            v_bonus += 2
        elif vb.abs_value < 50:
            v_bonus += 1
    v_points += v_bonus
