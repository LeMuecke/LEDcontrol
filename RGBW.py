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

        if color == "red":
            self.red = 255
            self.green = 0
            self.blue = 0
            self.white = 0
        elif color == "green":
            self.red = 0
            self.green = 255
            self.blue = 0
            self.white = 0
        elif color == "blue":
            self.red = 0
            self.green = 0
            self.blue = 255
            self.white = 0
        elif color == "white":
            self.red = 0
            self.green = 0
            self.blue = 0
            self.white = 255

    def getColor(self):
        return Color(self.green, self.red, self.blue, self.white)

    def getLowerBrightness(self, brightness):
        """
        Returns RGBW() with a lower overall brightness
        :param brightness: int, 255 is full brightness, 0 is darkness
        :return: RGBW
        """
        factor = brightness / 255
        scaledLight = RGBW()
        scaledLight.setColors(int(self.red * factor), int(self.green * factor), int(self.blue * factor), int(self.white * factor))
        return scaledLight