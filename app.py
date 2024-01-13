import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Временно: переменные хранятся здесь
WEATHER_API_KEY = "f50b7f6ae44f8a3ca4f85e88307e6560"

@app.route('/')
def welcome_page():
    title = "WELCOME"
    return render_template('welcome/welcome.html', title=title)

@app.route('/dashboard')
def main():
    return render_template('settings/settings.html')

@app.route('/settings', methods=['POST'])
def process_form():
    param1 = request.form['param1']
    param2 = request.form['param2']

    # Здесь вы можете использовать параметры, как вам нужно
    # Например, вы можете сохранить их в базу данных или выполнить другие действия
    # В этом примере просто выведем их на экран

    return f'Получены параметры: Параметр 1 - {param1}, Параметр 2 - {param2}'

@app.route('/get_weather', methods=['POST'])
def get_weather():
    #city = request.form.get('city')
    city = 'Rostov-on-Don'
    if not city:
        return jsonify({'status': 'error', 'message': 'Please provide a city name'})

    # Запрос к OpenWeatherMap API для получения текущей погоды
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # TODO: Температура по Фаренгейту, необходимо менять на цельсии . Дескрипшн тоже нужно править
        return jsonify({'status': 'success', 'temperature': temperature, 'description': description})
    else:
        return jsonify({'status': 'error', 'message': 'Failed to retrieve weather data'})



if __name__ == "__main__":
    #app.run(debug=True)
    get_weather()