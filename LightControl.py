from RGBW import RGBW
import time
from neopixel import *


class LightControl():

    # DEFINITIONS
    LED_COUNT = 240  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 5  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.SK6812_STRIP_RGBW  # Strip type and colour ordering

    def __init__(self):
        global strip
        strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                  self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        strip.begin()


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

        self.setRGBWAllObj(rgbw)

    def setRGBWAllObj(self, rgbw_obj):
        """Set color for all LEDs using rgbw object

        :param rgbw_obj: RGBW
        :return:
        """

        strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                  self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        strip.begin()

        color = rgbw_obj.getColor()
        #strip = self.strip
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

    def setColorLed(self, led_number, color):
        """Set a specific color for one LED"

        :param led_number: int
        :param color: String
        :return:
        """
        self.setRGBWLed(led_number, RGBW().setNaturalColor(color))

    def setRGBWLed(self, led_number, red, green, blue, white):
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

        self.setRGBWLedObj(led_number, rgbw)

    def setRGBWLedObj(self, led_number, rgbw_obj):
        """Set color for one LED using rgbw object

        :param led_number: int
        :param rgbw_obj: RGBW
        :return:
        """
        color = rgbw_obj.getColor()
        strip = self.strip
        strip.setPixelColor(led_number, color)
        strip.show()

    def colorWipe(self, rgbw_obj, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        color = rgbw_obj.getColor()
        strip = self.strip
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def strobe(self, rgbw_obj, rate_ms=100):
        strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                  self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        strip.begin()
        color = rgbw_obj.getColor()
        off = RGBW()
        off.red = 0
        off.green = 0
        off.blue = 0
        off.white = 0
        off = off.getColor()

        while True:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
            strip.show()
            time.sleep(rate_ms / 1000.0)
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, off)
            strip.show()
            time.sleep(rate_ms / 1000.0)

    def RGBstrobe(self, rate_ms=100):
        pass