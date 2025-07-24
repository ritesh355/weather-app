from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = os.environ.get('WEATHER_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return render_template('index.html', error="City not found.")
    
    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

