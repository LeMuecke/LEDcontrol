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
    color = extractColor()
    l.setRGBWAllObj(color)
    return redirect("http://192.168.2.37:5000/")

@app.route("/colorwipe", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/wipesnake", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/strobe", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/rgbstrobe", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/rainbowcycle", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/theaterrainbowchase", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/rainbowfull", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randomledskeepon", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randomleds", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/randommultiple", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/firemode", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")

@app.route("/fadein", methods=['GET'])
def setAllColor():
    return redirect("http://192.168.2.37:5000/")