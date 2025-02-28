import requests
from tkinter import *

# Create the Tkinter window
window = Tk()
window.title("Weather App")

# Label and input for date and city
label = Label(window, text='Hello, insert date (YYYY-MM-DD):')
label.pack()
input = Entry(window)
input.pack()

label2 = Label(window, text='Insert city:')
label2.pack()
input2 = Entry(window)
input2.pack()

# Function to fetch weather data and display temperature
def show_temp():
    city = input2.get()  # Get the city from the input field
    date = input.get()   # Get the date from the input field

    if not city or not date:
        print("Please enter both city and date.")
        return

    # Make the API request
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key=LKXHK7F6D2QE6DAXJBBHTS2B7&contentType=json"
    response = requests.get(url)

    if response.status_code == 200:
        final_response = response.json()
        temperature = find_temp(final_response, date)
        if temperature is not None:
            result_label = Label(window, text=f"Temperature in {city.capitalize()} on {date}: {temperature}°C")
            result_label.pack()
        else:
            error_label = Label(window, text=f"No data found for {date} in {city.capitalize()}")
            error_label.pack()
    else:
        error_label = Label(window, text="Error fetching weather data. Please check the city name.")
        error_label.pack()

# Function to find temperature for a specific date
def find_temp(data, date):
    for day in data["days"]:
        if day["datetime"] == date:
            return convert_to_celsius(day["temp"])
    return None

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(temp):
    return round((temp - 32) * 5 / 9)

# Button to trigger the search
button = Button(window, text='Search', command=show_temp)
button.pack()

# Run the Tkinter main loop
window.mainloop()