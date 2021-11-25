import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('instr.html')




@app.route("/<name>")
def show_report(name):
    user_api = "[Your OpenWeather API KEY]"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    temp_city = "{:.2f}".format(((api_data['main']['temp']) - 273.15))
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M")

    return render_template("weather-card.html", temp=temp_city, desc=weather_desc.title(), hum=hmdt, speed=wind_spd,
                           locn=name.title(), dt=date_time)


if __name__ == "__main__":
    app.run(debug=True)
