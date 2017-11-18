import time
from neopixel import *

class Adresser():

    #DEFINITIONS
    LED_COUNT       = 240  # Number of LED pixels.
    LED_PIN         = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA         = 5  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS  = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT      = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL     = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP       = ws.SK6812_STRIP_RGBW  # Strip type and colour ordering

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

    def rainbowCycle(self, strip, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def theaterChaseRainbow(self, strip, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, wheel((i + j) % 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    def colorWipe(self, strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        strip.begin()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)

#if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
		# Color wipe animations.
		#this.colorWipe(strip, Color(255, 0, 0), 0)  # Red wipe
		#time.sleep(2)
		#colorWipe(strip, Color(0, 255, 0), 0)  # Blue wipe
		#time.sleep(2)
		#colorWipe(strip, Color(0, 0, 255), 0)  # Green wipe
		#time.sleep(2)
		#colorWipe(strip, Color(0, 0, 0, 255), 0)  # White wipe
		#time.sleep(2)
		#colorWipe(strip, Color(255, 255, 255), 0)  # Composite White wipe
		#time.sleep(2)
		#colorWipe(strip, Color(255, 255, 255, 255), 0)  # Composite White + White LED wipe
		#time.sleep(2)