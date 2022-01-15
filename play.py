import os
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

import pyjokes as jokes
from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])

piada = jokes.get_joke(language='en')
result = translator.translate(piada, src="en", dest="pt")

print(result.text)
""" tts = gTTS(traduzir, lang='pt-BR')
            tts.save("piada.mp3")
            playsound("piada.mp3") """
