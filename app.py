import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

import pyjokes as jokes
from googletrans import Translator

from commands.cotacao import cotacao


def command():

    microfone = sr.Recognizer()
    translator = Translator(service_urls=['translate.googleapis.com'])

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa...")

        audio = microfone.listen(source)

        frase = microfone.recognize_google(audio, language='pt-BR')

        #print("Voce disse: " + frase)

        if frase == "Olá assistente":
            playsound("ouvindo.mp3")

        if frase == "assistente conte-me uma piada":
            piada = jokes.get_joke(language='en')
            result = translator.translate(piada, src="en", dest="pt")

            print(result.text)
            tts = gTTS(result.text, lang='pt-BR')
            tts.save("piada.mp3")
            playsound("piada.mp3")

        if frase == "cotação do dólar para real":
            ret_cotacao = cotacao()
            print(ret_cotacao)
            cria_audio(ret_cotacao, "cotacao")

        if frase == "encerrar":
            print("encerrando...")
            tchau()
            exit()

        return frase


def tchau():
    print("byee!")
    playsound("gatinho.mp3")


def cria_audio(texto, nome):
    tts = gTTS(texto, lang='pt-BR')
    tts.save(nome + ".mp3")
    playsound(nome + ".mp3")


def execute():
    while True:
        p = command()

        print(p)

execute()