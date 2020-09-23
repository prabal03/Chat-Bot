import os
import pyttsx3
import calendar as c
import time as t
import speech_recognition as sr
import wikipedia as wp
import smtplib as sm
import getpass as gp

engine = pyttsx3.init()
print("\n\t\t\t WELCOME TO CHATBOT")
print('\n# U Can Try In This Way:\n1.Try "Run any player."\n2.Try "I want to paint."'
      '\n3.Try "can u please open writing pad for me."\n4 You Can Also Open Browser.\n'
      '5.Try "Excel,Word,PowerPoint,Control panel,Photoshop,Pdf reader.\n'
      '6.You can also take your picture or record anything. \n7.If you want to calculate can perform.'
      '\n8.You can check calendar or date or month or time or Day.\n9.If you want to exit simply write exit.\n'
      '10.You can also shutdown ,restart, sleep, hibernate. ')
print(
    "\n'Help' - If In Output You Get An Error Name Related To Input Or Output Command.This Means Your Path Is Not Set "
    "Which you Want To Open")
engine.setProperty('rate', 170)
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
time = int(t.strftime("%H"))
if 5 <= time < 12:
    engine.say("Good Morning")
    engine.runAndWait()
elif 12 <= time < 18:
    engine.say("Good Afternoon")
    engine.runAndWait()
elif 18 <= time < 24 or 0 <= time < 5:
    engine.say("Good Evening")
    engine.runAndWait()
engine.say(" I am your ChatBot ")
engine.say(" What Can I Do For You ")
engine.runAndWait()

while True:
    def speech():
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("start saying...")
                audio = r.listen(source)
                print("wait processing your input")
                data = r.recognize_google(audio).lower()
            return data
        except:
            exit()


    s = speech()
    print(s)
    if "exit" in s or "quit" in s or "stop" in s:
        engine.setProperty("rate", 150)
        engine.say("chatbot closing the service have a good day")
        engine.runAndWait()
        exit()
    elif ("wmplayer" in s) or ('wmplayer' in s) or (
            'window media player' in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening window media player")
        engine.runAndWait()
        os.system("wmplayer")
        exit()
    elif ("vlc" in s) or ("vlc player" in s) or (" vlc media" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening vlc")
        engine.runAndWait()
        os.system("vlc")
        exit()
    elif ("notepad" in s) or ("notes" in s) or ("writing pad" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening notepad")
        engine.runAndWait()
        os.system("notepad")
        exit()
    elif ("information" in s) or ("biography" in s) or ("about" in s) or ("wikipedia" in s):
        engine.say("whose information do you want")
        engine.runAndWait()
        x = speech()
        print(wp.summary(x))
        voices = engine.getProperty("voices")
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        engine.say(wp.summary(x, sentences=3))
        engine.runAndWait()
        exit()
    elif ("browser" in s) or ("web" in s) or ("explorer" in s) or ("internet" in s) or \
            ("chrome" in s) or ("edge" in s) or ('msedge' in s) or ('microsoft edge' in s) or \
            ("firefox" in s):
        if ('edge' in s) or ('msedge' in s) or ('microsoft edge' in s):
            def restart():
                engine.say("Can I search for You")
                engine.runAndWait()
                s1 = speech()
                if s1 == "yes" or s1 == "ok":
                    def restart1():
                        engine.say("give the name of website")
                        engine.runAndWait()
                        z = speech()
                        engine.say("can i search inside this")
                        engine.runAndWait()
                        b = speech()
                        if b == "yes" or b == "ok":
                            engine.say("what do you want to search")
                            engine.runAndWait()
                            y = speech()
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge www.' + z + '.com/search?q=' + y1)
                        elif b == "no":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge www.' + z1 + '.com')
                        else:
                            engine.say("I am not sure say it again")
                            engine.runAndWait()
                            restart1()

                    restart1()

                elif s1 == "no":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('msedge')
                else:
                    engine.say("I am not sure say it again")
                    engine.runAndWait()
                    restart()


            restart()
            exit()

        elif ('chrome' in s) or ('chrome browser' in s) or ('chrome web' in s):
            def again():
                engine.say("Can I search for You")
                engine.runAndWait()
                s1 = speech()
                if s1 == "yes" or s1 == "ok":
                    def again1():
                        engine.say("give the name of website")
                        engine.runAndWait()
                        z = speech()
                        engine.say("can i search  inside this")
                        engine.runAndWait()
                        b = speech()
                        if b == "yes" or b == "ok":
                            engine.say("what do you want to search")
                            engine.runAndWait()
                            y = speech()
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start chrome www.' + z + '.com/search?q=' + y1)
                        elif b == "no":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start chrome www.' + z1 + '.com')
                        else:
                            engine.say("I am not sure say it again")
                            engine.runAndWait()
                            again1()

                    again1()
                elif s1 == "no":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('chrome')
                else:
                    engine.say("I am not sure say it again")
                    engine.runAndWait()
                    again()


            again()
            exit()

        elif ('firefox' in s) or ('firefox browser' in s) or ('firefox web' in s):
            def repeat():
                engine.say("Can I search for You")
                engine.runAndWait()
                s1 = speech()
                if s1 == "yes" or s1 == "ok":
                    def repeat1():
                        engine.say("give the name of a website that you want to open")
                        engine.runAndWait()
                        z = speech()
                        engine.say("can i search inside this")
                        engine.runAndWait()
                        b = speech()
                        if b == "yes" or b == "ok":
                            engine.say("what do you want to search")
                            engine.runAndWait()
                            y = speech()
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start firefox www.' + z + '.com/search?q=' + y1)
                        elif b == "no":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start firefox www.' + z1 + '.com')
                        else:
                            engine.say("I am not sure say it again")
                            engine.runAndWait()
                            repeat1()

                    repeat1()
                elif s1 == "no":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('firefox')
                else:
                    engine.say("I am not sure say it again")
                    engine.runAndWait()
                    repeat()


            repeat()
            exit()
        else:
            def reopen():
                engine.say("Can I search for You")
                engine.runAndWait()
                s1 = speech()
                if s1 == "yes" or s1 == "ok":
                    def reopen1():
                        engine.say("give the name of website  that you want to open")
                        engine.runAndWait()
                        z = speech()
                        engine.say("Can I search inside this")
                        engine.runAndWait()
                        b = speech()

                        if b == "yes" or b == "ok":
                            engine.say("what do you want to search")
                            engine.runAndWait()
                            y = speech()
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge  www.' + z + '.com/search?q=' + y1)
                        elif b == "no":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge  www.' + z1 + '.com')
                        else:
                            engine.say("I am not sure say it again")
                            engine.runAndWait()
                            reopen1()

                    reopen1()
                elif s == "no":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('start msedge')
                else:
                    engine.say("I am not sure say it again")
                    engine.runAndWait()
                    reopen()


            reopen()
            exit()
    elif "mail" in s or "email" in s or "send" in s:
        gmail_user = input("\nEnter your user name: ")
        gmail_password = gp.getpass("\nEnter your password")
        engine.say("enter the email address you want to send")
        engine.runAndWait()
        to = input("\n")
        too = to.split()
        try:
            server = sm.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login(gmail_user, gmail_password)
            subject = input("\nenter the subject you want to add:")
            body = input("\ntype the message:")
            message = f"subject:{subject}\n\n{body}"
            server.sendmail(gmail_user, to, message)
            engine.say("email send scussefully")
            engine.runAndWait()
            print("\nemail send scussefully")
        except Exception as e:
            engine.say("something went wrong")
            engine.runAndWait()
            print('\nsomething went wrong',e)
    elif (("paint" in s) or ("drawing pad" in s) or ("white board" in s) or ("draw" in s) or (
            "drwaing" in s) or ("sketch" in s)):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening paint")
        engine.runAndWait()
        os.system("mspaint")
        exit()
    elif ("adobe" in s) or ("reader" in s) or ("pdf" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening reader")
        engine.runAndWait()
        os.system("acrord32")
        exit()
    elif ("ppt" in s) or ("presentation" in s) or ("power point" in s) or ("slide" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening result")
        engine.runAndWait()
        os.system("powerpnt")
        exit()
    elif ("photoshop" in s) or ("adobe photoshop" in s) or ("photo editor" in s) or (
            "image editor" in s) or \
            ("photo maker" in s) or ("image maker" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening result")
        engine.runAndWait()
        os.system("photoshop")
        exit()
    elif ("control panel" in s) or ("panel" in s) or ("settings" in s) or ("system" in s) or \
            ("window setting" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening settings")
        engine.runAndWait()
        os.system("control")
        exit()
    elif ("word" in s) or ("wordpad" in s) or ("word file" in s) or ("microsoft word" in s) or \
            ("msword" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening word")
        engine.runAndWait()
        os.system("winword")
        exit()
    elif ("excel" in s) or ("exel" in s) or ("sheet" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening excel")
        engine.runAndWait()
        os.system("excel")
        exit()
    elif ("camera" in s) or ("webcam" in s) or ("photo" in s) or \
            ("record video" in s) or ("selfie" in s):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening camera")
        engine.runAndWait()
        os.system("start microsoft.windows.camera:")
        exit()
    elif ("calculator" in s) or ("calculate" in s) or ("operations" in s) or \
            ("maths" in s) or ("mathematical" in s) or ("calc" in s) or ("sum" in s) \
            or ("add" in s) or ("addition" in s) or ("subtraction" in s) or ("minus" in s) \
            or ("sub" in s) or ("difference" in s) or ("multiply" in s) or ("multiplication" in s) \
            or ("divide" in s) or ("division" in s):
        engine.setProperty("rate", 150)
        engine.say("opening calculator")
        engine.runAndWait()
        os.system("start calc.exe")
        exit()
    elif "calendar" in s:
        engine.setProperty("rate", 150)
        engine.say("wait a second opening calendar")
        engine.runAndWait()
        print("\n", c.calendar(int(t.strftime("%Y"))))
        exit()
    elif "time" in s:
        time = int(t.strftime("%H"))
        if 5 <= time < 12:
            print(t.strftime("%I:%M:%S %p"))
            engine.say(t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
            exit()
        elif 12 <= time < 18:
            print(t.strftime("%I:%M:%S %p"))
            engine.say(t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
            exit()
        elif 18 <= time < 24 or 0 <= time < 5:
            print(t.strftime("%I:%M:%S %p"))
            engine.say(t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
            exit()
    elif "date" in s:
        print(t.strftime("%x"))
        engine.say(t.strftime("%x"))
        engine.runAndWait()
        exit()
    elif "month" in s:
        print(t.strftime("%B"))
        engine.say(t.strftime("%B"))
        engine.runAndWait()
        exit()
    elif "year" in s:
        print(t.strftime("%Y"))
        engine.say(t.strftime("%Y"))
        engine.runAndWait()
        exit()
    elif "day" in s:
        print(t.strftime("%A"))
        engine.say(t.strftime("%A"))
        engine.runAndWait()
        exit()
    elif ("shutdown" in s) or ("shutoff" in s):
        engine.setProperty("rate", 150)
        engine.say("shutting down")
        engine.runAndWait()
        os.system("shutdown/s")
        exit()
    elif ("restart" in s) or ("reopen" in s):
        engine.setProperty("rate", 150)
        engine.say("restarting")
        engine.runAndWait()
        os.system("shutdown/r")
        exit()
    elif ("logoff" in s) or ("lock" in s) or ("sign out" in s) or ("sleep" in s):
        engine.setProperty("rate", 150)
        engine.say("siging off ")
        engine.runAndWait()
        os.system("shutdown/l")
        exit()
    elif "hibernate" in s:
        engine.setProperty("rate", 150)
        engine.say("hibernating ")
        engine.runAndWait()
        os.system("shutdown/h")
        exit()
    elif "reboot" in s:
        engine.setProperty("rate", 150)
        engine.say("rebooting ")
        engine.runAndWait()
        os.system("shutdown/g")
        exit()

    else:
        engine.setProperty("rate", 160)
        engine.say("I am not sure say it again")
        engine.runAndWait()

