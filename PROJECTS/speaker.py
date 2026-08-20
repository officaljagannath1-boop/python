# text to speech in windows   
import pyttsx3
import os
engine = pyttsx3.init()
if __name__ == '__main__':
    
 x = input("Enter the text you want to convert to speech: ")
 engine.say(x)
 engine.runAndWait()
 engine.runAndWait()
    