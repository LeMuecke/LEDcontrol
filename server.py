from flask import Flask, redirect, request, render_template
from LightControl import LightControl
from RGBW import RGBW

app = Flask(__name__)
l = LightControl()

def extractColor():
    red = request.args.get('red', 0)
    green = request.args.get('green', 0)
    blue = request.args.get('blue', 0)
    white = request.args.get('white', 0)
    color = RGBW(red, green, blue, white)
    return color

@app.route("/")
def hello():
    return render_template('InterfaceLinks.html')

@app.route("/setallcolor", methods=['GET'])
def setAllColor():
    red = request.args.get('red', 0)
    green = request.args.get('green', 0)
    blue = request.args.get('blue', 0)
    white = request.args.get('white', 0)
    l.setRGBWAll(int(red), int(green), int(blue), int(white))
    return redirect("http://192.168.2.37:5000/")

@app.route("/colorwipe", methods=['GET'])
def colorWipe():
    color = extractColor()
    wait_ms = request.args.get('waitms_colorwipe', 0)
    l.colorWipe(color, wait_ms)
    return redirect("http://192.168.2.37:5000/")

@app.route("/wipesnake", methods=['GET'])
def wipeSnake():
    color = extractColor()
    pixel_number = request.args.get('pixelnumers_wipesnake', 1)
    wait_ms = request.args.get('waitms_wipesnake', 0)
    l.wipeSnake(color, pixel_number, wait_ms)
    return redirect("http://192.168.2.37:5000/")

@app.route("/strobe", methods=['GET'])
def strobe():
    color = extractColor()
    wait_ms = request.args.get('waitms_strobe', 0)
    l.strobe(color, wait_ms)
    return redirect("http://192.168.2.37:5000/")

@app.route("/rgbstrobe", methods=['GET'])
def rgbstrobe():
    wait_ms = request.args.get('waitms_rgbstrobe', 0)
    l.RGBstrobe(wait_ms)
    return redirect("http://192.168.2.37:5000/")

@app.route("/rainbowcycle", methods=['GET'])
def rainbowcycle():
    return redirect("http://192.168.2.37:5000/")

@app.route("/theaterrainbowchase", methods=['GET'])
def theaterrainbowchase():
    return redirect("http://192.168.2.37:5000/")

@app.route("/rainbowfull", methods=['GET'])
def rainbowfull():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randomledskeepon", methods=['GET'])
def randomledskeepon():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randomleds", methods=['GET'])
def randomleds():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randommultiple", methods=['GET'])
def randommultiple():
    return redirect("http://192.168.2.37:5000/")

@app.route("/firemode", methods=['GET'])
def firemode():
    return redirect("http://192.168.2.37:5000/")

@app.route("/fadein", methods=['GET'])
def fadein():
    return redirect("http://192.168.2.37:5000/")

if __name__ == '__main__':
    app.run(debug=True, host='192.168.2.37')