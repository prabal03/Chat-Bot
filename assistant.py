import os
import pyttsx3
import calendar as c
import time as t

engine = pyttsx3.init()
print("\n\t\t\t WELCOME TO CHATBOT")
print("Hii\nTo Chat With Male Tap 0 Or To Chat With Female Tap 1 : ", end="")
p = int(input())
print('\n# U Can Try In This Way:\n1.Try "Run any player."\n2.Try "I want to paint."'
      '\n3.Try "can u please open writing pad for me."\n4 You Can Also Open Browser.\n'
      '5.Try "Excel,Word,PowerPoint,Control panel,Photoshop,Pdf reader.\n'
      '6.You can also take your picture or record anything. \n7.If you want to calculate can perform.'
      '\n8.You can check calendar or date or month or time or Day.\n9.If you want to exit simply write exit.\n'
      '10.You can also shutdown ,restart, sleep, hibernate. ')
print(
    "\n'Help' - If In Output You Get An Error Name Related To Input Or Output Command.This Means Your Path Is Not Set "
    "Which you Want To Open.")
if p == 1:
    engine.setProperty('rate', 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say("Hey I am your ChatBot ")
    engine.say("What Can I Do For You")
    engine.runAndWait()
else:
    engine.setProperty('rate', 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
    engine.say("HEY I am your ChatBot ")
    engine.say("What Can I Do For You")
    engine.runAndWait()

while True:
    Input = input("\nHow Can I Help U:").lower()
    if "exit" in Input or "quit" in Input or "stop" in Input:
        engine.setProperty("rate", 150)
        engine.say("see you soon")
        engine.runAndWait()
        print("\nBYE")
        exit()
    elif "don't" in Input or "dont" in Input or "do not" in Input:
        engine.setProperty("rate", 150)
        engine.say("okay Iam not opening this file")
        engine.runAndWait()
        print("\nokay I am not opening this file")
    elif ("wmplayer" in Input) or ("player" in Input) or ("media" in Input) or ('wmplayer' in Input) or (
            'window media player' in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening result")
        engine.runAndWait()
        os.system("wmplayer")
    elif ("vlc" in Input) or ("vlc player" in Input) or (" vlc media" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening vlc")
        engine.runAndWait()
        os.system("vlc")
    elif ("notepad" in Input) or ("notes" in Input) or ("writing pad" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening notepad")
        engine.runAndWait()
        os.system("notepad")
    elif ("browser" in Input) or ("web" in Input) or ("explorer" in Input) or ("internet" in Input) or \
            ("chrome" in Input) or ("edge" in Input) or ('msedge' in Input) or ('microsoft edge' in Input) or \
            ("firefox" in Input):
        if ('edge' in Input) or ('msedge' in Input) or ('microsoft edge' in Input):
            def restart():
                engine.say("Can I search for You press Y for Yes, N for No")
                engine.runAndWait()
                print("\nCan I search for You  press Y for Yes, N for No :", end="")
                s = input().lower()
                if s == "y":
                    def restart1():
                        z = input("\nGive the name of a website that you want to open:")
                        print("\nIf U Want To Search Inside This Then\npress Y for Yes, N for No:", end="")
                        b = input().lower()
                        if b == "y":
                            y = input("\nWhat u want to search:")
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge www.' + z + '.com/search?q=' + y1)
                        elif b == "n":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge www.' + z1 + '.com')
                        else:
                            engine.say("Sorry, I Cant Catch It")
                            engine.runAndWait()
                            restart1()

                    restart1()

                elif s == "n":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('msedge')
                else:
                    engine.say("Sorry, I Cant Catch It")
                    engine.runAndWait()
                    restart()


            restart()

        elif ('chrome' in Input) or ('chrome browser' in Input) or ('chrome web' in Input):
            def again():
                engine.say("Can I search for You press Y for Yes, N for No")
                engine.runAndWait()
                print("\nCan I search for You   press Y for Yes, N for No:", end="")
                s = input().lower()
                if s == "y":
                    def again1():
                        z = input("\nGive the name of a website that you want to open:")
                        print("\nIf U Want To Search Inside This Then\npress Y for yes, N for no:", end="")
                        b = input().lower()
                        if b == "y":
                            y = input("\nWhat u want to search:")
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start chrome www.' + z + '.com/search?q=' + y1)
                        elif b == "n":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start chrome www.' + z1 + '.com')
                        else:
                            engine.say("Sorry, I Cant Catch It")
                            engine.runAndWait()
                            again1()

                    again1()
                elif s == "n":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('chrome')
                else:
                    engine.say("Sorry, I Cant Catch It")
                    engine.runAndWait()
                    again()


            again()

        elif ('firefox' in Input) or ('firefox browser' in Input) or ('firefox web' in Input):
            def repeat():
                engine.say("Can I search for You press Y for Yes, N for No")
                engine.runAndWait()
                print("\nCan I search for You   press Y for Yes, N for No:", end="")
                s = input().lower()
                if s == "y":
                    def repeat1():
                        z = input("\nGive the name of a website that you want to open:")
                        print("\nIf U Want To Search Inside This Then\npress Y for yes, N for no:", end="")
                        b = input().lower()
                        if b == "y":
                            y = input("\nWhat u want to search:")
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start firefox www.' + z + '.com/search?q=' + y1)
                        elif b == "n":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start firefox www.' + z1 + '.com')
                        else:
                            engine.say("Sorry, I Cant Catch It")
                            engine.runAndWait()
                            repeat1()

                    repeat1()
                elif s == "n":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('firefox')
                else:
                    engine.say("Sorry, I Cant Catch It")
                    engine.runAndWait()
                    repeat()


            repeat()
        else:
            def reopen():
                engine.say("Can I search for You press Y for Yes, N for No")
                engine.runAndWait()
                print("\nCan I search for You   press Y for Yes, N for No :", end="")
                s = input().lower()
                if s == "y":
                    def reopen1():
                        z = input("\nGive the name of a website that you want to open:")
                        print("\nIf U Want To Search Inside This Then\npress Y for Yes, N for No. ", end="")
                        b = input().lower()
                        if b == "y":
                            y = input("\nWhat you want to search:")
                            y1 = y.replace(" ", '+')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge  www.' + z + '.com/search?q=' + y1)
                        elif b == "n":
                            z1 = z.replace(" ", '')
                            engine.say("wait a second opening result")
                            engine.runAndWait()
                            os.system('start msedge  www.' + z1 + '.com')
                        else:
                            engine.say("Sorry, I Cant Catch It")
                            engine.runAndWait()
                            reopen1()

                    reopen1()
                elif s == "n":
                    engine.say("wait a second opening browser")
                    engine.runAndWait()
                    os.system('start msedge')
                else:
                    engine.say("Sorry, I Cant Catch It")
                    engine.runAndWait()
                    reopen()


            reopen()
    elif (("paint" in Input) or ("drawing pad" in Input) or ("white board" in Input) or ("draw" in Input) or (
            "drwaing" in Input) or ("sketch" in Input)):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening paint")
        engine.runAndWait()
        os.system("mspaint")
    elif ("adobe" in Input) or ("reader" in Input) or ("pdf" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening reader")
        engine.runAndWait()
        os.system("acrord32")
    elif ("ppt" in Input) or ("presentation" in Input) or ("power point" in Input) or ("slide" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening result")
        engine.runAndWait()
        os.system("powerpnt")
    elif ("photoshop" in Input) or ("adobe photoshop" in Input) or ("photo editor" in Input) or (
            "image editor" in Input) or \
            ("photo maker" in Input) or ("image maker" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening result")
        engine.runAndWait()
        os.system("photoshop")
    elif ("control panel" in Input) or ("panel" in Input) or ("settings" in Input) or ("system" in Input) or \
            ("window setting" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening settings")
        engine.runAndWait()
        os.system("control")
    elif ("word" in Input) or ("wordpad" in Input) or ("word file" in Input) or ("microsoft word" in Input) or \
            ("msword" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening word")
        engine.runAndWait()
        os.system("winword")
    elif ("excel" in Input) or ("exel" in Input) or ("sheet" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening excel")
        engine.runAndWait()
        os.system("excel")
    elif ("camera" in Input) or ("webcam" in Input) or ("photo" in Input) or \
            ("record video" in Input) or ("selfie" in Input):
        engine.setProperty("rate", 150)
        engine.say("wait a second opening camera")
        engine.runAndWait()
        os.system("start microsoft.windows.camera:")
    elif ("calculator" in Input) or ("calculate" in Input) or ("operations" in Input) or \
            ("maths" in Input) or ("mathematical" in Input) or ("calc" in Input) or ("sum" in Input) \
            or ("add" in Input) or ("addition" in Input) or ("subtraction" in Input) or ("minus" in Input) \
            or ("sub" in Input) or ("difference" in Input) or ("multiply" in Input) or ("multiplication" in Input) \
            or ("divide" in Input) or ("division" in Input):
        engine.setProperty("rate", 150)
        engine.say("opening calculator")
        engine.runAndWait()
        os.system("start calc.exe")
    elif "calendar" in Input:
        engine.setProperty("rate", 150)
        engine.say("which year do you want:")
        engine.runAndWait()
        p = int(input("\nWhich year do you want:"))
        engine.setProperty("rate", 150)
        engine.say("wait a second opening calendar")
        engine.runAndWait()
        print("\n", c.calendar(p))
    elif "time" in Input:
        time = int(t.strftime("%H"))
        if 5 <= time < 12:
            print(t.strftime("%I:%M:%S %p"))
            engine.say("Good Morning" + t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
        elif 12 <= time < 18:
            print(t.strftime("%I:%M:%S %p"))
            engine.say("Good Afternoon" + t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
        elif 18 <= time < 24 or 0 <= time < 5:
            print(t.strftime("%I:%M:%S %p"))
            engine.say("Good Evening" + t.strftime("%IHour%MMinute%SSeconds %p"))
            engine.runAndWait()
    elif "date" in Input:
        print(t.strftime("%x"))
        engine.say(t.strftime("%x"))
        engine.runAndWait()
    elif "month" in Input:
        print(t.strftime("%B"))
        engine.say(t.strftime("%B"))
        engine.runAndWait()
    elif "year" in Input:
        print(t.strftime("%Y"))
        engine.say(t.strftime("%Y"))
        engine.runAndWait()
    elif "day" in Input:
        print(t.strftime("%A"))
        engine.say(t.strftime("%A"))
        engine.runAndWait()
    elif ("shutdown" in Input) or ("shutoff" in Input):
        engine.setProperty("rate", 150)
        engine.say("shutting down")
        engine.runAndWait()
        os.system("shutdown/s")
    elif ("restart" in Input) or ("reopen" in Input):
        engine.setProperty("rate", 150)
        engine.say("restarting")
        engine.runAndWait()
        os.system("shutdown/r")
    elif ("logoff" in Input) or ("lock" in Input) or ("sign out" in Input) or ("sleep" in Input):
        engine.setProperty("rate", 150)
        engine.say("siging off ")
        engine.runAndWait()
        os.system("shutdown/l")
    elif "hibernate" in Input:
        engine.setProperty("rate", 150)
        engine.say("hibernating ")
        engine.runAndWait()
        os.system("shutdown/h")
    elif "reboot" in Input:
        engine.setProperty("rate", 150)
        engine.say("rebooting ")
        engine.runAndWait()
        os.system("shutdown/g")

    else:
        engine.setProperty("rate", 160)
        engine.say("Sorry, I Didn't Get It")
        engine.runAndWait()
        print("\nSorry, I Didn't Get It ")

