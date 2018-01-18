from LightControl import LightControl
from RGBW import RGBW

class StateWatcher:

    current_color = RGBW(0,0,0,0)
    l = LightControl()

    def fadeToColor(self, color):
        diff_red = self.current_color.red - color.red
        diff_green = self.current_color.green - color.green
        diff_blue = self.current_color.blue - color.blue
        diff_white = self.current_color.white - color.white

        for i in range(0,255):
            if self.current_color.red < color.red:
                self.current_color.red += 1
            elif self.current_color.red > color.red:
                self.current_color.red -= 1
            if self.current_color.green < color.green:
                self.current_color.green += 1
            elif self.current_color.green > color.green:
                self.current_color.green -= 1
            if self.current_color.blue < color.blue:
                self.current_color.blue += 1
            elif self.current_color.blue > color.blue:
                self.current_color.blue -= 1
            if self.current_color.white < color.white:
                self.current_color.white += 1
            elif self.current_color.white> color.white:
                self.current_color.white -= 1

            self.l.setRGBWAllObj(self.current_color)

    def dim(self):
        new_red = self.current_color.red - 50
        new_green = self.current_color.green - 50
        new_blue = self.current_color.blue - 50
        new_white = self.current_color.white - 50
        if new_red < 0:
            new_red = 0
        if new_green < 0:
            new_green = 0
        if new_blue < 0:
            new_blue = 0
        if new_white < 0:
            new_white = 0

        self.fadeToColor(RGBW(new_red, new_green, new_blue, new_white))