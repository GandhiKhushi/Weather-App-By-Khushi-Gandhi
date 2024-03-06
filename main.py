import requests
import json
import pyttsx3
print("Enter The Name of City that You Want To Find Its Weather \n")
while True:
    city = input("Enter City : ")
    url=f"http://api.weatherapi.com/v1/current.json?key={add Your Weather API Key Here}={city}"
    r=requests.get(url)
    wdic=json.loads(r.text)
    w=wdic["current"]["temp_c"]
    w1=wdic["location"]["region"]
    w2=wdic["location"]["country"]
    print(w)
    print(w1)
    print(w2)
    engine = pyttsx3.init()
    x=f"'{city} is located in {w1},{w2} and The Current Temperature of {city} is {w}."
    engine.say(x)
    engine.runAndWait()
    if x=="q":
        print("Thank You")
        break
