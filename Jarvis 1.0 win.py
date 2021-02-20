import os
import webbrowser
import requests
import ctypes  # For pop-ups
import subprocess
import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import datetime
import smtplib
import time
import configparser

# Defining key variables to customize the voice assistant
config = configparser.ConfigParser()
config.read('config.ini')

name = config['Jarvis']['name']
email = config['Jarvis']['email']
password = config['Jarvis']['password']
assname = config['Jarvis']['assname']  # assistant name for example: Jarvis
version = config['Jarvis']['version']


# Defining current time function

def currenttime():
    now = datetime.datetime.now()
    log.write('\n' + 'Current date and time : ')
    log.write(now.strftime('%Y-%m-%d %H:%M:%S' + '\t' + '\t'))


# Making a log file for the voice assistant

log = open(f'{assname}_log.txt', 'a')

# Separates each log with 3 enters

if os.path.exists(f'{assname}_log.txt'):
    log.write('\n')
    log.write('\n')
    log.write('\n')


# Add your daily apps for startup


def startup():
    # Example: os.startfile('<app path>')

    currenttime()
    log.write('I opened your daily apps Sir !' + '\n')


# Pop-up message for info

def popup_basic(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)


# Pop-up message with prompt for daily startup

def popup_choice(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 4)


# Fetch daily pages for you on startup

def fetch_pages():
    # As an example i put gmail which is the page that I'd like to have on my startup

    currenttime()
    log.write('I opened your daily pages Sir !' + '\n')


# Building the core engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

currenttime()
log.write('Voice engine was built successfully Sir !' + '\n')
popup_basic(f'{assname}', 'Voice engine was built successfully Sir !')


# Defining the basic function of the voice assistant


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am your Assistant")
    speak(assname)


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        currenttime()
        log.write('Listenning...' + '\n')

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        currenttime()
        log.write('Recognizing...' + '\n')

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        currenttime()

        log.write(f'User said: {query}\n')

        print(f"User said: {query}\n")

    except Exception as e:

        currenttime()
        log.write(str(e) + '\n')

        currenttime()
        log.write("Unable to Recognize your voice." + '\n')

        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def usrname():

    print("#####################")
    print(f"Welcome Mr. {name}")
    print("#####################")

    currenttime()
    log.write("#####################" + '\n')

    currenttime()
    log.write("Welcome Mr." + name + '\n')

    currenttime()
    log.write("#####################" + '\n')

    speak("How can i Help you Sir ?")

    currenttime()
    log.write('How can i Help you Sir ?' + '\n')


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail

    server.login(f'{email}', f'{password}')
    server.sendmail(f'{email}', to, content)
    server.close()


# Main functions


def main():
    os.system('cls')

    # This Function will clean any
    # command before execution of this python file

    popup_var = popup_choice(f'{assname}', 'Do you want to run startup Sir ?')

    # This means you select yes

    if popup_var == 6:
        startup()
        fetch_pages()

    wishme()
    usrname()

    speak('Main function works fine and basic function were built Sir !')

    currenttime()
    log.write('Main function works fine and basic function were built Sir !' + '\n')

    while True:
        query = takecommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            currenttime()
            log.write('According to Wikipedia' + '\n')
            currenttime()
            log.write(results + '\n')

        elif 'youtube' in query:
            speak('Here you go to Youtube')
            webbrowser.open('https://www.youtube.com')

            currenttime()
            log.write('Here you go to Youtube' + '\n')

        elif 'google' in query:
            speak('Here you go to Google')
            webbrowser.open('https://www.google.com')

            currenttime()
            log.write('Here you go to Google' + '\n')

        elif 'stackoverflow' in query:
            speak('Here you go to Stack Over flow, Happy coding')
            webbrowser.open('https://www.stackoverflow.com')

            currenttime()
            log.write('Here you go to Stack Over flow, Happy coding' + '\n')

        elif 'time' in query:
            now = datetime.datetime.now()

            strtime = now.strftime('%H:%M:%S')

            speak(f'Sir !, the time is {strtime}')

            currenttime()

            log.write(f'Sir !, the time is {strtime}' + '\n')

        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("whome should i send")
                to = takecommand().lower()
                sendemail(to, content)
                speak("Email has been sent !")

                currenttime()
                log.write('Email has been sent !' + '\n')

            except Exception as e:
                print(e)
                speak("I am not able to send this email")

                currenttime()
                log.write(str(e) + '\n')
                currenttime()
                log.write('I am not able to send this email' + '\n')

        elif 'how are you' in query:
            jarvis_responses_list = ["I'm great", "I'm fine", "I'm doing good", "Not Bad"]
            jarvis_responses_result = random.choice(jarvis_responses_list)
            speak(jarvis_responses_result)

            currenttime()
            log.write(jarvis_responses_result + '\n')

            jarvis_questions_list = ["How was your day Sir ?", "How about you Sir ?", "How are you Sir ?"]
            jarvis_questions_result = random.choice(jarvis_questions_list)
            speak(jarvis_questions_result)

            currenttime()
            log.write(jarvis_questions_result + '\n')

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(f'{assname}')

            currenttime()
            log.write(f"My friends call me {assname}" + '\n')

        elif 'exit' in query:
            speak("Thanks for giving me your time")

            currenttime()
            log.write('Thanks for giving me your time' + '\n')
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Alireza Safari")

            currenttime()
            log.write('I have been created by Alireza Safari.' + '\n')

        elif 'flip a coin' in query:
            res = random.randint(1, 2)
            if res == 1:
                speak('Heads')

                currenttime()
                log.write('Heads' + '\n')

            elif res == 2:
                speak('Tails')

                currenttime()
                log.write('Tails' + '\n')

            else:
                popup_basic(f'{assname}', 'An Error Occurred')

                currenttime()
                log.write('An Error Occurred while flipping a coin' + '\n')

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

            currenttime()
            log.write('The answer is' + answer + '\n')

        elif "who am i" in query:
            speak("If you talk then definitely your human")

            currenttime()
            log.write('If you talk then definitely your human' + '\n')

        elif "why you came to world" in query:
            speak("Thanks to Alireza Safari. further It's a secret")

            currenttime()
            log.write("Thanks to Alireza Safari. further It's a secret" + '\n')

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

            currenttime()
            log.write("It is 7th sense that destroy all other senses" + '\n')

        elif "who are you" in query:
            speak("I am your virtual assistant created by Alireza Safari")

            currenttime()
            log.write('I am your virtual assistant created by Alireza Safari' + '\n')

        elif 'reason for you' in query:
            speak("I was created as a Fun project by Mister Alireza Safari")

            currenttime()
            log.write('I was created as a Fun project by Mister Alireza Safari' + '\n')

        elif 'lock window' in query:
            speak("locking the device")

            currenttime()
            log.write('Locking the device' + '\n')

            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")

            currenttime()
            log.write("Hold On a Sec ! Your system is on its way to shut down" + '\n')

            subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop listening" in query:
            speak(f"for how much time you want to stop {assname} from listening commands")
            a = int(takecommand())

            currenttime()
            log.write(f'{assname} is gonna be locked for {a} minute(s)' + '\n')

            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate")
            speak(location)

            currenttime()
            log.write('User asked to locate' + location + '\n')

            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "restart" in query:
            speak('Restarting the system in a sec Sir !')

            currenttime()
            log.write('Restarting the system in a sec Sir !' + '\n')

            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak('Hibernating the system in a sec Sir !')

            currenttime()
            log.write('Hibernating the system in a sec Sir !' + '\n')
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak('Logging off the system in a sec Sir !')

            currenttime()
            log.write('Logging off the system in a sec Sir !' + '\n')

            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write Sir ?")

            currenttime()
            log.write('What should i write Sir ?' + '\n')

            note = takecommand()

            file = open(f'{assname}.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strtime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strtime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

            currenttime()
            log.write('Note file created successfully' + '\n')

        elif "show note" in query:

            speak("Showing Notes Sir !")

            currenttime()
            log.write('Showing notes Sir !' + '\n')

            file = open(f"{assname}.txt", "r")
            print(file.readlines())
            speak(file.readline())

        elif "jarvis" or f'{assname}' in query:

            wishme()
            speak(f"{assname} {version} in your service Mister")

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather

            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidity) + "\n description = " + str(weather_description))

                currenttime()

                log.write(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidity) + "\n description = " + str(weather_description) + '\n')

            else:
                speak(" City Not Found ")

                currenttime()
                log.write('City Not Found' + '\n')

        elif "Good Morning" in query:

            speak('Have a nice day Sir !')

            currenttime()
            log.write('Have a nice day Sir !' + '\n')

        # most asked question from google Assistant

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

            currenttime()
            log.write("I'm not sure about, may be you should give me some time" + '\n')

        elif 'search' in query:
            speak('What should i search for Sir !')
            ask_search = takecommand()

            try:
                webbrowser.open(ask_search)

                currenttime()
                log.write('Searched the results successfully Sir !' + '\n')

            except:
                speak("Sorry Sir !, Couldn't search what you asked for")

                currenttime()
                log.write("Sorry Sir !, Couldn't search what you asked for" + '\n')

        # Gives $ price to Rials

        elif 'dollar price' in query:
            json_data = requests.get('http://api.navasan.tech/latest/?api_key=Q7qZLgqv1jmtBDu0dgF6lw9TMpc1QfRN').json()
            json_usd = json_data['mex_usd_sell']
            value = json_usd['value']
            speak(f'Good Morning Sir ! $ price of today is {value} Tomans')

            currenttime()
            log.write(f'Good Morning Sir ! $ price of today is {value} Tomans' + '\n')


        elif not query or query == '':
            speak("Hmmm, You didn't say anything Sir !")

            currenttime()
            log.write("Hmmm, You didn't say anything Sir !" + '\n')

        else:
            speak("Sorry Sir !, Your Command is not in my database wait for further updates, Thanks")

            currenttime()

            log.write("Sorry Sir !, Your Command is not in my database wait for further updates, Thanks")


main()
