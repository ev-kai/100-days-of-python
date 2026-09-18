
import requests  # Import the requests library so the script can make HTTP API calls.
from datetime import datetime  # Import datetime to compare the current local time with sunrise and sunset.
import smtplib  # Import SMTP to send an email alert.
import time  # Import time so the program can pause and loop repeatedly.

 # Store your longitude so the code can compare it with the ISS location.
parameters = {  # Create a dictionary with the coordinates used in the API requests.
    "lat": my_lat,  # Set the latitude parameter to your location latitude.
    "lng": my_lng,  # Set the longitude parameter to your location longitude.
    "formatted": 0,  # Ask the API for the time in raw ISO format instead of a formatted local string.
}



def is_iss_overhead():  # Define a function that checks whether the ISS is near your location.
    response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)  # Send a request to the API using your latitude and longitude.
    response.raise_for_status()  # Raise an error if the HTTP request fails.
    data = response.json()  # Convert the JSON response from the API into a Python dictionary.

    iss_latitude = float(data["iss_position"]["latitude"])  # Extract the ISS latitude and convert it to a float.
    iss_longitude = float(data["iss_position"]["longitude"])  # Extract the ISS longitude and convert it to a float.

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_lng - 5 <= iss_longitude <= my_lng + 5:  # Check if the ISS is within 5 degrees of your location.
        return True  # Return True only when the ISS is close enough to your position.


def is_night():  # Define a function that checks if it is currently nighttime at your location.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)  # Request sunrise/sunset data for your location.
    response.raise_for_status()  # Stop the program if the API request fails.
    data = response.json()  # Save the API response as a dictionary.
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Extract the sunrise hour from the JSON response.
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # Extract the sunset hour from the JSON response.
    time_now = datetime.now()  # Get the current local time.

    if time_now.hour >= sunset or time_now.hour <= sunrise:  # Check if the current hour is after sunset or before sunrise.
        return True  # Return True when it is night at your location.


while True:  # Start an infinite loop so the script keeps checking repeatedly.
    time.sleep(60)  # Wait 60 seconds before checking again.
    if is_iss_overhead() and is_night():  # Only continue if the ISS is overhead and it is nighttime.

        connection = smtplib.SMTP("smtp.gmail.com")  # Connect to Gmail's SMTP server.
        connection.starttls()  # Encrypt the connection with TLS.
        connection.login(user=my_email, password=my_password)  # Log in to the Gmail account.
        connection.sendmail(  # Send an email alert to the target recipient.
            from_addr=my_email,  # Set the sender email address.
            to_addrs="evkairas@gmail.com",  # Set the destination email address.
            msg="Subject:Look Up👆\n\nThe ISS is above you in the"  # Compose the email body and subject.
        )
  
# Overall logic:
# This program keeps checking the sky and the time every 60 seconds.
# First, it tries to determine whether the International Space Station is close to the user's location.
# Then, it checks whether it is nighttime at that location.
# If both conditions are true, the script logs into an email account and sends a warning email.
# The goal is to notify the user when the ISS is visible overhead at night, so they can look up and see it.
# In simple terms: repeated API checks + time comparison + email alert when conditions are met.

# 1. Swap the email for a Webhook
        
