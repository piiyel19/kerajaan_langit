from flask import Flask, render_template, request

import requests, json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html")


@app.route('/get_weather')
def get_weather():
	city = request.args.get('city')
	api_key = "5ab84dafd0577def1a49f1ffc8c3b9be"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	city_name = city
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	x = response.json()
	return render_template("result.html",data=x)


if __name__ == "__main__":
    app.run(debug=True)