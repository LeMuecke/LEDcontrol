from neopixel import *

class RGBW():
    red = 0
    green = 0
    blue = 0
    white = 0

    def setColors(self, red, green, blue, white):
        self.red = red
        self.green = green
        self.blue = blue
        self.white = white

    def setNaturalColor(self, color):
        """Sets the according natural color to it's rgbw value

        :param color: int
        :return:
        """

        if(color == "red"):
            red = 255
            green = 0
            blue = 0
            white = 0
        elif(color == "green"):
            red = 0
            green = 255
            blue = 0
            white = 0
        elif(color == "blue"):
            red = 0
            green = 0
            blue = 255
            white = 0
        elif(color == "white"):
            red = 0
            green = 0
            blue = 0
            white = 255

    def getColor(self):
        return Color(self.green, self.red, self.blue, self.white)