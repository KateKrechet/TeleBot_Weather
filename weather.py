import requests

key = '0cf93f9cb36b53f4a87202e164714f72'
city = 571476


def weather(key=key, city=city):
    zapros = 'https://api.openweathermap.org/data/2.5/weather'
    try:
        result = requests.get(zapros, params={'id': city, 'lang': 'ru', 'units': 'metric', 'appid': key})
        # print(result)
        data = result.json()
        # print(data)
        # k1 = data['name']
        k1 = data.get('name')
        k2 = str(round(data['main']['temp'], 0)) + ' C'
        k3 = str(data['wind']['speed']) + ' м/с'
        k4 = data['weather'][0]['description']
        # print(k1, k2, k3, k4)
        prognoz = k1 + ' ' + k2 + ' ' + k3 + ' ' + k4
        return prognoz
    except:
        print('neok')


def weather_five(key=key, city=city):
    zapros = 'https://api.openweathermap.org/data/2.5/forecast'
    try:
        result = requests.get(zapros, params={'id': city, 'lang': 'ru', 'units': 'metric', 'appid': key})
        # print(result)
        data = result.json()
        # print(data)
        city = data['city']['name']
        prognoz = ''
        for i in data['list']:
            if i['dt_txt'][11:13] == '15':
                # print(city, i['main']['temp'], i['weather'][0]['description'], i['dt_txt'])
                prognoz += city + ' ' + str(i['main']['temp']) + 'C ' + i['weather'][0]['description'] + ' ' + i[
                    'dt_txt'] + '\n'
        return prognoz
    except:
        print('neok')
