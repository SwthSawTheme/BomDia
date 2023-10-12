import os
import time
import pyautogui as py
import pyperclip

def pai():
    time.sleep(1)
    pai = os.path.join('images/pai.png')
    clique = py.locateOnScreen(pai, confidence=0.7)
    time.sleep(0.5)
    py.click(clique)
    time.sleep(1)
    pyperclip.copy('''Bom dia pai!
Bença''')
    time.sleep(0.5)
    py.hotkey('ctrl','v')
    time.sleep(1)
    py.press('enter')
    time.sleep(0.5)
    py.press('tab',presses=5)
    time.sleep(0.5)
    py.hotkey('ctrl','a')
    time.sleep(1)

def mae():
    time.sleep(1)
    mae = os.path.join('images/mae2.png')
    clique = py.locateOnScreen(mae, confidence=0.7)
    time.sleep(0.5)
    py.click(clique)
    time.sleep(1)
    pyperclip.copy('Bom dia mãe❤️')
    time.sleep(0.5)
    py.hotkey('ctrl','v')
    time.sleep(1)
    py.press('enter')
    time.sleep(0.5)
    py.press('tab',presses=5)
    time.sleep(0.5)
    py.hotkey('ctrl','a')
    time.sleep(1)

def anjo():
    time.sleep(1)
    anjo = os.path.join('images/meuAnjoDeLuz.png')
    clique = py.locateOnScreen(anjo, confidence=0.7)
    time.sleep(0.5)
    py.click(clique)
    time.sleep(1)
    pyperclip.copy('Bom dia minha vida❤️ Isso não é um robô, é apenas meu amor verdadeiro por você!!')
    time.sleep(0.5)
    py.hotkey('ctrl','v')
    time.sleep(1)
    py.press('enter')
    time.sleep(0.5)
    py.press('tab',presses=5)
    time.sleep(0.5)
    py.hotkey('ctrl','a')
    time.sleep(1)

def sandra():
    time.sleep(1)
    sandra = os.path.join('images/sandra.png')
    clique = py.locateOnScreen(sandra, confidence=0.7)
    time.sleep(0.5)
    py.click(clique)
    time.sleep(1)
    pyperclip.copy('''Bom diaa Mãe!
Bença❤️❤️❤️''')
    time.sleep(0.5)
    py.hotkey('ctrl','v')
    time.sleep(1)
    py.press('enter')
    time.sleep(0.5)
    py.press('tab',presses=5)
    time.sleep(0.5)
    py.hotkey('ctrl','a')
    time.sleep(1)
    py.press('backspace')
    time.sleep(1)
    py.alert('Fim da execução, pressione Ok para encerrar!')
    py.hotkey('alt','f4')

def mensagem():
    contatos = ['Pai','Mae2','Meu Anjo De Luz','Sandra']
    for i in contatos:
        time.sleep(1)
        py.write(i)
        if i == 'Pai':
            pai()
        elif i == 'Mae2':
            mae()
        elif i == 'Meu Anjo De Luz':
            anjo()
        elif i == 'Sandra':
            sandra()
        
    
