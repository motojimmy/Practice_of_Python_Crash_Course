import requests
import json
import time

url = "http://www.pm25.in/api/querys/all_cities.json?city=beijing&token=5j1znBVAsnSf5xQyNQyq"
r = requests.get(url)

print("StatusCode:", r.status_code)

response_dict = r.json()
filename = "PM2.5_Beijing.json"
now = time.ctime()
with open(filename, 'a') as f_obj:
    json.dump(now + "\n", f_obj)
    json.dump(response_dict, f_obj)
    json.dump("\n******************************\n", f_obj)


print(response_dict)