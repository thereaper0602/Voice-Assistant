# import library
import speech_recognition as sr
import pywin32_system32
import datetime
import pyttsx3
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

os.system("cls")

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetUser():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    hour = datetime.datetime.now().hour
    if hour>=4 and hour<12:
        print("Good morning!!")
        speak("Good morning")
    elif hour >=12 and hour < 17:
        print("Good afternoon!!")
        speak("Good afternoon!!")
    elif hour >=17 and hour < 24:
        speak("Good evening!!")
        print("Good evening!!")
    else:
        speak("Good Night Sir,see you tomorow")
        print("Good Night Sir,see you tomorow")
    
    speak("How can I help you ?")
    print("How can I help you ?")

#def dateTime():

def takeCommand():
    r = sr.Recognizer() # create an object from sr to recognize voice from many source like voice , micro,audio,...
    
    # ghi Ă¢m giá»ng nĂ³i tá»« microphone
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # thiáº¿t láº­p má»™t ngÆ°á»¡ng táº¡m dá»«ng cho Ä‘á»‘i tÆ°á»£ng Recognizer, náº¿u khoáº£ng thá»i gian táº¡m dá»«ng vĂ  báº¯t Ä‘áº§u quĂ¡ trĂ¬nh nháº­n dáº¡ng
        # lá»›n hÆ¡n hoáº·c báº±ng n giĂ¢y thĂ¬ thÆ° viá»‡n sr sáº½ coi Ä‘Ă³ lĂ  táº¡m dá»«ng vĂ  báº¯t Ä‘áº§u quĂ¡ trĂ¬nh nháº­n dáº¡ng giá»ng nĂ³i .
        audio = r.listen(source) # audio sáº½ cĂ³ kiá»ƒu dá»¯ liá»‡u audio data -> lÆ°u trá»¯ Ă¢m thanh


    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = "en-in")
        # nháº­n dáº¡ng giá»ng nĂ³i tá»« dá»¯ liá»‡u audio chuyá»ƒn sang dáº¡ng string(query)
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try again"
    return query

def time():
    time = datetime.datetime.now().strftime("%I%p:%M minute")
    speak("The current time is")
    speak(time)
    print("The current time is : ",time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current day is")
    speak(day)
    speak(month)
    speak(year)
    print("The current day is "+str(day)+"/"+str(month)+"/"+str(year))

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\ADMIN\\OneDrive\\Hì€nh à‰nh\\À‰nh chù£p mà€n hì€nh")

if __name__ == "__main__":
    # greeting
    greetUser()

    while True:
        print("What type of control do you want to use \n1 . Using keyboard \n2. Using voice")
        choose = int(input("You choose : "))
        query = ""
        if(choose == 1):
            query = input("Input the prompt : ")
        elif choose == 2:
            query = takeCommand().lower()
        # tell datetime
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        #telling about you
        elif 'who are you' in query:
            speak("I'm JARVIS created by Quang and I'm a desktop assistant")
            print("I'm JARVIS created by Quang and I'm a desktop assistant")
        # wikipedia
        elif 'wikipedia' in query:
            try:
                speak("Ok wait sir,I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences = 2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
                
        elif 'youtube' in query:
            wb.open("https://www.youtube.com/")

        elif 'chrome' in query or 'google' in query or 'gg' in query:
            wb.open("google.com")
        
        elif 'lms' in query:
            wb.open("https://lms.ou.edu.vn/")

        elif 'tien ich' in query or 'tisv' in query:
            wb.open("https://tienichsv.ou.edu.vn/")
        
        elif 'sis' in query:
            wb.open("https://sis.ou.edu.vn/")

        elif 'github' in query: 
            wb.open("https://github.com/")

        elif 'stack overflow' in query or 'stk' in query:
            wb.open("https://stackoverflow.co/")

        elif 'chat GPT' in query or 'gpt' in query:
            wb.open("https://chat.openai.com/")

        elif 'facebook'in query or 'fb' in query:
            wb.open("https://www.facebook.com/")

        elif 'messenger' in query or 'msg' in query:
            os.startfile("C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Messenger.lnk")

        elif 'notion' in query:
            notionPath = "C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Notion.lnk"
            os.startfile(notionPath)

        elif 'visual studio' in query or 'vs' in query:
            visualStudio = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(visualStudio)

        elif 'code' in query:
            vsCode = "C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(vsCode)

        elif 'Sublime Text' in query:
            sublimePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text.lnk"
            os.startfile(sublimePath)
        
        elif "visual studio" in query:
            visualPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio 2022.lnk"
            os.startfile(visualPath)

        elif "screenshot" in query or 'scr' in query:
            screenshot()
            speak("I have taken the screenshot , please check it")
            
        elif "bing" in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")

        elif "offline" in query or "quit" in query or 'off' in query:
            quit()
        
