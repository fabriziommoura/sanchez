import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Pode falar..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Sanchez' in comando:
                comando = comando.replace('Sanchez', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Não consigo te escutar')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('São' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando essa pedrada!')
        maquina.runAndWait()
    
    elif 'quem foi' in comando:
        quemfoi = comando.replace('quem foi', '')
        wikipedia.set_lang('PT')
        resultado = wikipedia.summary(quemfoi,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'quem é' in comando:
        queme = comando.replace('quem é', '')
        wikipedia.set_lang('PT')
        resultado = wikipedia.summary(queme,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
comando_voz_usuario()
#Made by @fabriziommoura