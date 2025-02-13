renpy = None
Solid = None
v_bars = []

"""renpy
init python:
"""


# CLASSES
class Ver_bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.variation = renpy.random.randint(-4, 4)

    @property
    def bar(self):
        value = abs(self.value)
        if value == 0:
            value = 1
        yoffset = 0
        if self.value > 0:
            yoffset = -value
        return Solid("#FCC", xsize=100, ysize=value, yoffset=yoffset)

    def change(self):
        self.value += self.variation

# FUNCTIONS
def change_bars():
    for vb in v_bars:
        vb.change()

