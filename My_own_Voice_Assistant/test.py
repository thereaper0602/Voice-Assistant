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

# pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello!I'm your assistant")
# engine.runAndWait()

# microphone = sr.Microphone()
# recognizer = sr.Recognizer()

# # Ghi âm giọng nói từ microphone
# with microphone as source:
#     print("Hãy nói gì đó...")
#     audio = recognizer.listen(source)

# # Nhận dạng giọng nói từ âm thanh đã ghi âm
# try:
#     text = recognizer.recognize_google(audio, language='vi-VN')
#     print("Bạn đã nói:", text)
# except sr.UnknownValueError:
#     print("Không thể nhận dạng giọng nói!")
# except sr.RequestError as e:
#     print("Lỗi trong quá trình gửi yêu cầu tới Google API;", str(e))
time = datetime.datetime.now()
print(time.strftime("%H%p:%M minute"))