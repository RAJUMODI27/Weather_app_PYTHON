import requests
import json
import pyttsx3
engine=pyttsx3.init()
engine.say("hello. you are using  the ,free weather Api")
engine.say("Let me know the name of city , i am glad to tell its temperature  ")
engine.runAndWait()
def speak(x):
    engine.say(f"The temperature at {city} is {x}")
    engine.runAndWait()
    return

city=input("Enter the name of any city")
url=f"https://api.weatherapi.com/v1/current.json?key=2fc4dbaae48b444b91c114604230206&q={city}" #YOU NEED TO write your weather api key  inside key="HERE" 
r=requests.get(url)

weatherd=json.loads(r.text)
x=weatherd["current"]["temp_c"]
speak(x)


