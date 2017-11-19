from RGBW import RGBW
import time
from neopixel import *
import random


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
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                  self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        self.strip.begin()


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
        color = rgbw_obj.getColor()
        strip = self.strip
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
        rgbw = RGBW().setColors(red, green, blue, white)

        self.setRGBWLedObj(led_number, rgbw)

    def setRGBWLedObj(self, led_number, rgbw_obj):
        """Set color for one LED using rgbw object

        :param led_number: int
        :param rgbw_obj: RGBW
        :return:
        """

        strip = self.strip
        color = rgbw_obj.getColor()
        strip.setPixelColor(led_number, color)
        strip.show()

    def colorWipe(self, rgbw_obj, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        strip = self.strip

        color = rgbw_obj.getColor()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def strobe(self, rgbw_obj, rate_ms=100):
        strip = self.strip

        color = rgbw_obj.getColor()
        off = RGBW()
        off.setColors(0,0,0,0)
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
        strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                  self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        strip.begin()
        red = RGBW()
        red.setNaturalColor("red")
        red = red.getColor()
        green = RGBW()
        green.setNaturalColor("green")
        green = green.getColor()
        blue = RGBW()
        blue.setNaturalColor("blue")
        blue = blue.getColor()

        while True:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, red)
            strip.show()
            time.sleep(rate_ms / 1000.0)

            for i in range(strip.numPixels()):
                strip.setPixelColor(i, green)
            strip.show()
            time.sleep(rate_ms / 1000.0)

            for i in range(strip.numPixels()):
                strip.setPixelColor(i, blue)
            strip.show()
            time.sleep(rate_ms / 1000.0)

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        strip = self.strip
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel(((i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        strip = self.strip
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, self.wheel((i + j) % 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    def rainbowAll(self, rate_ms):
        strip = self.strip
        while True:
            for i in range(255):
                for j in range(strip.numPixels()):
                    strip.setPixelColor(j, self.wheel(i))
                strip.show()
                time.sleep(rate_ms / 1000.0)

    def randomKeepOn(self, rgbw_obj, wait_ms):
        strip = self.strip
        color = rgbw_obj.getColor()

        while True:
            strip.setPixelColor(random.randint(0,254), color)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def randomJustOne(self, rgbw_obj, wait_ms):
        strip = self.strip
        color = rgbw_obj.getColor()
        off = Color(0,0,0,0)

        while True:
            rnd = random.randint(0,254)
            for i in range(strip.numPixels()):
                if i == rnd:
                    strip.setPixelColor(i, color)
                else:
                    strip.setPixelColor(i, off)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def fadeIn(self, rgbw_obj, time_to_full):
        strip = self.strip
        step = time_to_full / 255.0

        for i in range(256):
            color = rgbw_obj.getLowerBrightness(i)
            color = color.getColor()
            for j in range(strip.numPixels()):
                strip.setPixelColor(j, color)
            strip.show()
            time.sleep(step / 1000.0)