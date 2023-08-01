import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None

def get_temperature(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['main']['temp']

def get_wind_speed(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['wind']['speed']

def get_pressure(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['main']['pressure']

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            date = input("Enter the date (YYYY-MM-DD format): ")
            temperature = get_temperature(weather_data, date)
            print(f"Temperature on {date}: {temperature} °C")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD format): ")
            wind_speed = get_wind_speed(weather_data, date)
            print(f"Wind speed on {date}: {wind_speed} m/s")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD format): ")
            pressure = get_pressure(weather_data, date)
            print(f"Pressure on {date}: {pressure} hPa")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()