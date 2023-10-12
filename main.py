import pyautogui as py
import time
import os
from functions import mensagem

def main():
    py.alert('Pressione Ok para continuar! Enquanto o bot estiver rodando não mexa no teclado/Mouse até a finalização do mesmo!')
    time.sleep(1)
    images = os.path.join('images/pesquisa.png')
    py.press('win')
    time.sleep(1)
    py.write('whatsapp')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    barra = py.locateOnScreen(images, confidence=0.7)                   
    time.sleep(1)
    py.click(barra)
    time.sleep(1)
    mensagem()
    
main()