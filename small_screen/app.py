from flask import Flask, render_template
from static.pyfiles import weather, calendar, room_stuff
import json
import uptime

CALANDER_EVENT_START = calendar.get_events()["start"][:5]
CALANDER_EVENT = calendar.get_events()["event"]
CALANDER_EVENT_END = calendar.get_events()["end"][:5]
CALANDER_EVENT_DT = calendar.get_events()["event_dt"]
PERIOD = f"{CALANDER_EVENT_START} - {CALANDER_EVENT_END}"

with open("../config.json") as fp:
    file = json.load(fp)
    location = file["city"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calendar")
def calendar_route():
    return render_template("calendar.html",
                            event_date = CALANDER_EVENT_DT,
                            period = PERIOD,
                            event = calendar.get_events()["event"]
                            )

@app.route("/weather")
def weather_route():
    return render_template("weather.html", location=location, temp=weather.get_temp())

@app.route("/animation")
def animation():
    return render_template("animation.html")

@app.route("/news")
def news_route():
    # todo: return news from TAGESSCHUA ?? read out rss feed: http://www.tagesschau.de/xml/rss2
    return render_template("news.html")

@app.route("room")
def room():
    return render_template("room.html", hum=room_stuff.get_roomstuff()["hum"] ,temp=room_stuff.get_roomstuff()["temp"])

@app.route("/system_info")
def system_info():
    return render_template("system.html", system_uptime=uptime.uptime())

@app.route("/config")
def config_route():
    return render_template("config.html")
    # todo: show config - extra page

if __name__ == "__main__":
    app.run(port=8080, debug=True)