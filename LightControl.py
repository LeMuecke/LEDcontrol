
class LightControl():

    def setColorAll(self, color):
        """Set a specific color for all LEDs

        :param color: String
        :return:
        """
        pass

    def setRGBAll(self, red, green, blue):
        """Set color for all LEDs using rgb notation

        :param red: int
        :param green: int
        :param blue: int
        :return:
        """
        pass

    def setRGBAll(self, rgb_obj):
        """Set color for all LEDs using rgb object

        :param rgb_obj: RGB
        :return:
        """

    def setColorLed(self, led_number, color):
        """Set a specific color for one LED"

        :param led_number: int
        :param color: String
        :return:
        """
        pass

    def setRGBLed(self, led_number, red, green, blue):
        """Set color for one LED using rgb notation

        :param led_number: int
        :param red: int
        :param green: int
        :param blue: int
        :return:
        """
        pass

    def setRGBLed(self, led_number, rgb_obj):
        """Set color for one LED using rgb object

        :param led_number: int
        :param rgb_obj: RGB
        :return:
        """
        pass