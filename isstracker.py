import requests
import datetime


url = "http://api.open-notify.org/iss-now.json"

def main():

    response = requests.get(url)

    jsonresp = response.json()
    
    x = jsonresp['timestamp']
    
    timestamp = datetime.datetime.fromtimestamp(x)
    time = timestamp.strftime('%Y-%m-%d %H:%M:%S') 

    print("Current Location of the ISS:")
    print("Lon:", jsonresp['iss_position']['longitude'])
    print("Lat:", jsonresp['iss_position']['latitude'])
    print("Timestamp", time)
if __name__ == "__main__":
    main()
