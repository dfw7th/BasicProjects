import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the API key
API_KEY = os.getenv("API_KEY")

# User Input for city
city_name = input("Enter your City: ")

# The API endpoint
url = (
    f"http://api.openweathermap.org/data/2.5/weather"
    f"?q={city_name}"
    f"&appid={API_KEY}"
    f"&units=metric"
)

# A GET request to the API
response = requests.get(url, timeout=20)

# Print the response
data = response.json()

try:
    # Check if the request was successful
    response.raise_for_status()
    if response.content:
        # Parse the JSON data
        data = response.json()
        if response.status_code == 404:
            print(
                """Error: City not found.
            Please check the spelling and try again."""
            )
    else:
        print("Error: Empty response from the server.")
    # Handle other errors
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
except requests.ConnectionError:
    print("There was a ConnectionError")
except KeyError:
    print("Invalid API key or missing data in the response")
except requests.exceptions.JSONDecodeError:
    print("Error: Failed to decode JSON from the response.")
except ValueError:
    print("No such city exists")
except Exception as e:
    print(f"An error occurred: {e}")

# We extract the data from out JSON file and
# print the output in a user-friendly way
city = data["name"]
temp = data["main"]["temp"]
weather = data["weather"][0]["description"]
temp_feel = data["main"]["feels_like"]
print(f"Weather in {city}:")
print(f"Temperature is: {temp}°C, but feels like {temp_feel}")
print(f"Description: {weather}")
