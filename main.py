import speech_recognition as sr
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
# import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os  # to remove created audio files


class person:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

# get string and make a audio file to be played


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = f'audio-{str(r)}.mp3'
    tts.save(audio_file)  # save as mp3
    print(f'Jarvis: {audio_string}')  # print what app said

    playsound.playsound(audio_file)  # play the audio file
    os.remove(audio_file)  # remove audio file


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('sorry whats that?')
        except sr.RequestError:
            print('Sorry, the service is down')
        print(f'>> {voice_data.lower()}')  # print what user said
        return voice_data.lower()


def respond(voice_data):
    # 2: name
    if there_exists(['what is your name', 'what is your name', 'tell me your name']):
        if person_obj.name:
            speak('My name is Jarvis')
        else:
            speak('My name is Jarvis. what is your name?')
    if there_exists(['my name is']):
        person_name = voice_data.split('is')[-1].strip()
        speak(f'okay, i will remember that {person_name}')
        person_obj.setName(person_name)  # remember name in person object
    # 4: time
    if there_exists(['what is the time', 'tell me the time', 'what time is it']):
        time = ctime().split(' ')[3].split(':')[0:2]
        if time[0] == '00':
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)
    # 5: search google
    if there_exists(['search for']) and 'youtube' not in voice_data:
        search_term = voice_data.split('for')[-1]
        url = f'https://google.com/search?q={search_term}'
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("goodbye sir")
        exit()


time.sleep(1)

person_obj = person()
speak('hello, how can i help you sir')
while(1):
    voice_data = record_audio()  # get the voice input
    respond(voice_data)  # respond
