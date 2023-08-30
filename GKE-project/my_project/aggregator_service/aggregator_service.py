from flask import Flask, render_template
import requests

app = Flask(__name__)

# URLs of the datetime and random number services
DATETIME_SERVICE_URL = "http://datetime-service:5000/"
RANDOM_SERVICE_URL = "http://random-service:5001/"

@app.route('/')
def aggregator():
    # Fetch date and time from the datetime service
    datetime_response = requests.get(DATETIME_SERVICE_URL).json()
    date_time = datetime_response.get('date_time', '')

    # Fetch random number from the random number service
    random_response = requests.get(RANDOM_SERVICE_URL).json()
    random_number = random_response.get('random_number', 0)

    # Return the combined data
    return render_template("index.html", date_time=date_time, random_number=random_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
