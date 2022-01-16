from filecmp import cmp
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

import pyjokes as jokes
from googletrans import Translator

from commands.cotacao import cotacao
from commands.playMusic import youtube_search


def command():

    microfone = sr.Recognizer()
    translator = Translator(service_urls=['translate.googleapis.com'])

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa...")

        audio = microfone.listen(source)

        frase = microfone.recognize_google(audio, language='pt-BR')

        # print("Voce disse: " + frase)


        if frase == "Olá Natasha":
            playsound("ouvindo.mp3")

        if frase == "Como você se chama":
            playsound("natasha.mp3")

        if youtube_search(frase):
            fr = youtube_search(frase)
            fr = str(fr)
            cria_audio(fr, "youtube")

        if frase == "Natasha conte-me uma piada":
            piada = jokes.get_joke(language='en')
            result = translator.translate(piada, src="en", dest="pt")

            print(result.text)
            tts = gTTS(result.text, lang='pt-BR')
            tts.save("piada.mp3")
            playsound("piada.mp3")


        if frase == "Natasha cotação do dólar":
            ret_cotacao = cotacao("USD-BRL")
            cria_audio(ret_cotacao, "cotacao")

        if frase == "Natasha encerrar":
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


def teste(texto):

    texto = texto
    moedas = {"dólar": "USDBRL", "real": "BRLUSD"}

    texto = texto.split(" ")

    b = dict((k,2) for k in texto)

    # print(b)

    shared = set(moedas.keys()) & set(b.keys())
    shared = str(shared)
    shared = shared.strip("{''}")
    # ke = moedas.get(shared)

    l = ["dólar", "real"]
    i = l.index(shared)
    frase = "Natasha cotação do {}".format(l[i])

    print(frase)

execute()
# cria_audio("Meu nome é Natasha, sou sua assistente virtual.", "natasha")
# teste("Natasha cotação do dólar")