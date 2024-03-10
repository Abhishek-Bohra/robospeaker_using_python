import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Hacker_Abhisek")
    engine = pyttsx3.init()
    while True:
        x = input("Enter What You Want Me To Speak : ")
        if x.lower() == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
