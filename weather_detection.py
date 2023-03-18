import pip._vendor.requests
import tkinter as tk

api_key = '05efb9dba7fa862da7748eaec9d33544'
url = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):

    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = pip._vendor.requests.get(url, params=params)
    weather_data = response.json()

    description = weather_data['weather'][0]['description'].capitalize()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    weather_str = f'Climate: {description}\n Temperature: {temperature:.2f}°C\n Humidity: {humidity}%'
    return weather_str


def display_weather():
    city = entry.get()
    weather_str = get_weather(city)
    label.config(text=weather_str)


root = tk.Tk()
root.configure(background="light sea green")
root.title('Weather Detection')
root.geometry("400x375")
root.minsize(250, 250)
root.maxsize(600, 500)

label = tk.Label(root, text='Enter the location:', bg="black",
                 fg="white", font="arial 15 bold", borderwidth=5, relief='groove')
label.pack(side='top', pady=6)

entry = tk.Entry(root, bg="black",
                 fg="white", font="arial 15 bold", borderwidth=5, relief='groove')
entry.pack()

button = tk.Button(root, text='Search', bg="black",
                   fg="black", padx=10, pady=10, font="arial 15 bold", borderwidth=5, relief='groove', command=display_weather)
button.pack(side='bottom', pady=6)

label = tk.Label(root, text='', bg="black",
                 fg="white", font="arial 15 bold", borderwidth=5, relief='groove')
label.pack(side='bottom', pady=6)

root.mainloop()