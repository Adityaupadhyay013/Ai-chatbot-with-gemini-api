# Python project of ai powered chatbot(gemini api)
from google import genai
from Queries import my_api
import speech_recognition as sr
import pygame
import io
from gtts import gTTS
recognizer = sr.Recognizer()
def gpt(ask , my_api):
 try:
  global response
  client = genai.Client(api_key = my_api)
  response = client.models.generate_content(
    model = "gemini-2.0-flash" , contents = ask
 )
 except:
  print("Output is unable to generate....")
def voice(text):
 tts = gTTS(text = text , lang = "hi" , slow = False)
 audio = io.BytesIO()
 tts.write_to_fp(audio)
 audio.seek(0)
 pygame.mixer.init()
 pygame.mixer.music.load(audio , "mp3")
 pygame.mixer.music.play()
 while pygame.mixer.music.get_busy():
    continue
print("-------------------------------------WELCOME TO AI CHATBOT-----------------------------------------------")
while True:
 print("If you want to ask your question by texting it enter 1.")
 print("If you want to ask your question by voice enter 2.")
 print("If you want to exit the chatbot enter 3.")
 choice = input("Enter your choice: ")
 if(choice == "1"): 
   question = input("Ask anything: ")
   gpt(question , my_api)
   print("If you want your answer in text format enter 1.")
   print("If you want your answer in voice enter 2.")
   wish = input("Enter your choice: ")
   if(wish == "1"):
    mod_response =  response.text.replace("*" , " ")
    print(mod_response)
   elif(wish == "2"):
    mod_response =  response.text.replace("*" , " ")
    voice(mod_response)
 elif(choice == "2"):
  with sr.Microphone() as source:
   print("Ask somthing...")
   recognizer.adjust_for_ambient_noise(source)
   audio = recognizer.listen(source)
   try:
    text = recognizer.recognize_google(audio)
    print("you said " , text)
    gpt(text , my_api)
    print("If you want your answer in text format enter 1.")
    print("If you want your answer in voice enter 2.")
    wish = input("Enter your choice: ")
    if(wish == "1"):
     print(response.text)
    elif(wish == "2"):
     mod_response =  response.text.replace("*" , " ")
     print("....")
     voice(mod_response)
   except:
    print('Please speak loudly.Not any voice captured.')
 elif(choice == "3"):
  print("Thanks for using this chatbot.")
  print("Hope you use us again......")
  print("Exiting....")
  break
 else:
  print("Please enter a valid choice!!")