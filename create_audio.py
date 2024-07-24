from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def create_audio(string, audio_name):
    tts = gTTS(string, lang='pt-br')
    tts.save(f'audios/{audio_name}.mp3')
    playsound(f'audios/{audio_name}.mp3')

create_audio('Fala direito porra! Não entendi', 'understand')
# create_audio('Ocorreu um erro, tente novamente', 'error')
# create_audio('Ok, estou pausando', 'pause')
# create_audio('Ok, estou pausando', 'unpause')
# create_audio('O que tu quer?', 'hello')
# create_audio('Volume ajustado', 'volume')
#create_audio('O pc será desligado as 01:00', 'shutdonw')