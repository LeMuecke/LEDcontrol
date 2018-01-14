from flask import Flask, redirect, request, render_template
from LightControl import LightControl
from RGBW import RGBW

address = "http://192.168.0.6:5432"     #also change address on the bottom

app = Flask(__name__)
l = LightControl()

def extractColor():
    red = request.args.get('red', 0)
    green = request.args.get('green', 0)
    blue = request.args.get('blue', 0)
    white = request.args.get('white', 0)
    color = RGBW(int(red), int(green), int(blue), int(white))
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
    return redirect(address)

@app.route("/colorwipe", methods=['GET'])
def colorWipe():
    color = extractColor()
    wait_ms = request.args.get('waitms_colorwipe', 0)
    l.colorWipe(color, int(wait_ms))
    return redirect(address)

@app.route("/wipesnake", methods=['GET'])
def wipeSnake():
    color = extractColor()
    pixel_number = request.args.get('pixelnumers_wipesnake', 1)
    wait_ms = request.args.get('waitms_wipesnake', 0)
    l.wipeSnake(color, pixel_number, int(wait_ms))
    return redirect(address)

@app.route("/strobe", methods=['GET'])
def strobe():
    color = extractColor()
    wait_ms = request.args.get('waitms_strobe', 0)
    l.strobe(color, int(wait_ms))
    return redirect(address)

@app.route("/rgbstrobe", methods=['GET'])
def rgbstrobe():
    wait_ms = request.args.get('waitms_rgbstrobe', 0)
    l.RGBstrobe(int(wait_ms))
    return redirect(address)

@app.route("/rainbowcycle", methods=['GET'])
def rainbowcycle():
    wait_ms = request.args.get('waitms_rainbowcycle', 0)
    iterations = request.args.get('iterations_rainbowcycle', 0)
    l.rainbowCycle(int(wait_ms), int(iterations))
    return redirect(address)

@app.route("/theaterrainbowchase", methods=['GET'])
def theaterrainbowchase():
    return redirect(address)

@app.route("/rainbowfull", methods=['GET'])
def rainbowfull():
    return redirect(address)

@app.route("/randomledskeepon", methods=['GET'])
def randomledskeepon():
    return redirect(address)

@app.route("/randomleds", methods=['GET'])
def randomleds():
    return redirect(address)

@app.route("/randommultiple", methods=['GET'])
def randommultiple():
    return redirect(address)

@app.route("/firemode", methods=['GET'])
def firemode():
    wait_ms = request.args.get('waitms_firemode', 0)
    l.fireMode(wait_ms=int(wait_ms))
    return redirect(address)

@app.route("/fadein", methods=['GET'])
def fadein():
    return redirect(address)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.6', port=5432)