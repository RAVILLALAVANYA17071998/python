import speech_recognition
import pyttsx3 as p
from selenium import webdriver

r1 = sr.Recognizer()
engine = p.init()
engine.says("hello sire,how are you today?")
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("Hello sire,how are you today?")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("unkonwn value")
    except sr.RequestError as e:
        print("Request error")

r2=sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    engine.say("Do You Want to check out hindi songs?")
    engine.runAndWait()
    audio2=r2.listen(source)
    try:
        text2= r2.recoginize_google(audio2)
        print(text2)
    except sr.unknownvalueError:
        print("unknown value")
    except sr.RequestError as e:
        print("Request error")

engine.say("I will not take no for an answer anyway")
engine.runAndWait()

engine.say("What do play .")
engine.runAndWait()

engine.say("I am going to play the hindi songs playlist for you, sit back and enjoy.")
engine.runAndWait()


class Music:
    def __init__(selfself):
        self.driver = webdriver.chrome(r"C:\Users\ravillalavanya\Desktop\chromedriver.exe")

    def play(self):
        self.driver.get("https://www.youtube.com/c/T-series/playlists?view=50&sort=dd&shelf_id=21")
        a=self.driver.find_element_by_xpath('//*[@id="thumbnail"]')
        a.click()
