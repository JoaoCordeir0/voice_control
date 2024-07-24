import speech_recognition as sr
from playsound import playsound
import threading
import PySimpleGUI as sg
import pyautogui
import subprocess
import re
import os

def listen_to_user() -> None | bool:
    try:
        microphone = sr.Recognizer()
        
        with sr.Microphone() as source:        
            microphone.adjust_for_ambient_noise(source)        
            print("Diga 'Controle' para acionar o controle")

            audio = microphone.listen(source)
            try:        
                string = microphone.recognize_google(audio, language='pt-BR')                            
                print(string)
                if string.lower() == 'controle':
                    start_control()
                if string.lower() == 'fechar':
                    return True
            except sr.UnkownValueError:                  
                threading.Thread(target=playsound, args=('audios/understand.mp3', )).start()
    except Exception:  
        ...

def start_control() -> None:
    try:        
        threading.Thread(target=playsound, args=('audios/hello.mp3', )).start()                

        microphone = sr.Recognizer()
        
        with sr.Microphone() as source:        
            microphone.adjust_for_ambient_noise(source)
            audio = microphone.listen(source)
            try:        
                string = microphone.recognize_google(audio, language='pt-BR')     

                if string.lower() == 'pausar':
                    pause()
                
                elif string.lower() == 'despausar':
                    unpause()
                
                elif 'volume' in string.lower():
                    set_volume(string)
                
                elif string.lower() == 'desligar pc':
                    shutdown_now()
                
                elif string.lower() == 'programar desligamento':
                    schedule_shutdown()

                elif string.lower() == 'sair':
                    return

                else:
                    threading.Thread(target=playsound, args=('audios/understand.mp3', )).start()
                
            except sr.UnkownValueError:  
                threading.Thread(target=playsound, args=('audios/understand.mp3', )).start()
    except Exception:  
        ...

def show_screnn() -> None:
    #sg.theme('DarkTeal12')    
    sg.theme('DarkTeal9')    
    #sg.theme_previewer()
        
    layout = [  
        [sg.Frame('Comandos',
            [   
                [sg.Text(' ')],
                [sg.Text('"Controle" para ativar', font=('Arial', 25))],
                [sg.Text(' ')],
                [sg.Text('- Pausar', font=('Arial', 25))],
                [sg.Text('- Despausar', font=('Arial', 25))],
                [sg.Text('- Volume em ...%', font=('Arial', 25))],      
                [sg.Text('- Desligar pc', font=('Arial', 25))],      
                [sg.Text('- Programar desligamento', font=('Arial', 25))],                
            ],
            pad=(5, 10),            
            size=(600, 400),
            font=('Arial', 30)
        )],   
    ]
    
    window = sg.Window('Voice Control', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break        

    window.close() 

def pause() -> None:
    threading.Thread(target=playsound, args=('audios/pause.mp3', )).start()
    pyautogui.moveTo(2850, 600)    
    pyautogui.click()

def unpause() -> None:
    threading.Thread(target=playsound, args=('audios/unpause.mp3', )).start()
    pyautogui.moveTo(2850, 500)    
    pyautogui.click()

def set_volume(string):        
    threading.Thread(target=playsound, args=('audios/volume.mp3', )).start()
    volume = int(re.findall(r'\d+', string)[0])    
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])

def shutdown_now():    
    os.system('shutdown now')

def schedule_shutdown():
    threading.Thread(target=playsound, args=('audios/shutdonw.mp3', )).start()
    os.system('shutdown 01:00')

if __name__ == '__main__':    
    threading.Thread(target=show_screnn).start()
    while (True):
        if listen_to_user():
            break