
class RGBW():
    red = 0
    green = 0
    blue = 0
    white = 0

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