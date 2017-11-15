
class RGB():
    red = 0
    green = 0
    blue = 0

    def setNaturalColor(self, color):
        """Sets the according natural color to it's rgb value

        :param color: int
        :return:
        """

        if(color == "red"):
            red = 255
            green = 0
            blue = 0
        elif(color == "green"):
            red = 0
            green = 255
            blue = 0
        elif(color == "blue"):
            red = 0
            green = 0
            blue = 255