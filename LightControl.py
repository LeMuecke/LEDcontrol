from RGBW import RGBW


class LightControl():

    def setColorAll(self, color):
        """Set a specific color for all LEDs

        :param color: String
        :return:
        """
        self.setRGBWAll(RGBW().setNaturalColor(color))

    def setRGBWAll(self, red, green, blue, white):
        """Set color for all LEDs using rgb notation

        :param red: int
        :param green: int
        :param blue: int
        :return:
        """
        rgbw = RGBW()
        rgbw.red = red
        rgbw.green = green
        rgbw.blue = blue
        rgbw.white = white

        self.setRGBWAll(rgbw)

    def setRGBWAll(self, rgb_obj):
        """Set color for all LEDs using rgbw object

        :param rgb_obj: RGBW
        :return:
        """
        pass

    def setColorLed(self, led_number, color):
        """Set a specific color for one LED"

        :param led_number: int
        :param color: String
        :return:
        """
        self.setRGBWLed(led_number, RGBW().setNaturalColor(color))

    def setRGBLed(self, led_number, red, green, blue, white):
        """Set color for one LED using rgbw notation

        :param led_number: int
        :param red: int
        :param green: int
        :param blue: int
        :return:
        """
        rgbw = RGBW()
        rgbw.red = red
        rgbw.green = green
        rgbw.blue = blue
        rgbw.white = white

        self.setRGBWLed(led_number, rgbw)

    def setRGBWLed(self, led_number, rgb_obj):
        """Set color for one LED using rgbw object

        :param led_number: int
        :param rgb_obj: RGBW
        :return:
        """
        pass