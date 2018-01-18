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

    #PRESET COLORS
    red = RGBW(255,0,0,0)
    green = RGBW(0,255,0,0)
    blue = RGBW(0,0,255,0)
    white = RGBW(0,0,0,255)
    full_white = RGBW(255,255,255,255)
    yellow = RGBW(255,255,0,0)
    off = RGBW(0,0,0,0)

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
        rgbw = RGBW(red, green, blue, white)

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
        rgbw = RGBW(red,green,blue,white)

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

    def wipeSnake(self, rgbw_obj, pixels_number=1 ,wait_ms=50):
        #TODO: Seems a bit slow
        strip = self.strip

        color = rgbw_obj.getColor()
        while True:
            for start in range(strip.numPixels()):
                for i in range(strip.numPixels()):
                    if i in range(start, start+pixels_number):
                        strip.setPixelColor(i, color)
                    else:
                        strip.setPixelColor(i, self.off.getColor())
                strip.show()
                time.sleep(wait_ms / 1000.0)



    def strobe(self, rgbw_obj, rate_ms=100):
        strip = self.strip

        color = rgbw_obj.getColor()
        off = self.off.getColor()

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
        strip = self.strip

        red = self.red
        red = red.getColor()
        green = self.green
        green = green.getColor()
        blue = self.blue
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

    def rainbowFull(self, rate_ms):
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

    def randomMultiple(self, rgbw_obj, wait_ms, quantity):
        #TODO: Somehow when stopping this with STRG+C, Python crashes with segfault, implement a way to safely shut this down
        strip = self.strip
        color = rgbw_obj.getColor()
        off = Color(0,0,0,0)

        while True:
            rnd = random.randint(0,254)
            for i in range(strip.numPixels()):
                if i == rnd:
                    for j in range(0,quantity - 1):
                        strip.setPixelColor(i-j, color)
                else:
                    strip.setPixelColor(i, off)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def fireMode(self, wait_ms, red=240, green=80, blue=10, flicker=150):
        strip = self.strip
        while True:
            for i in range(strip.numPixels()):
                flickerr = random.randint(0,flicker)
                flickerg = random.randint(0,flicker)
                flickerb = random.randint(0,flicker)
                r = red-flickerr
                g = green-flickerg
                b = blue-flickerb

                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                color = RGBW(r,g,b,0)
                color = color.getColor()
                strip.setPixelColor(i,color)
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