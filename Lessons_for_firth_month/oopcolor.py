class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def deHofx(self):
        return(self.red, self.green, self.blue)
grey = Color(80,255,255)


print(grey.deHofx())

