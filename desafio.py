import pyautogui
import pyperclip
from time import sleep
pyautogui.alert(text='Bem-vindo ao programa AutoBot', title='AutoBot')
email = pyautogui.prompt(text='Email:', title='AutoBot')
senha = pyautogui.password(text='Senha:', title='AutoBot', mask='*')
confirmacao = pyautogui.confirm(text='Confirma os dados?', title='AutoBot', buttons=['Sim', 'Não','Cancela'])


if confirmacao == 'Sim':
    def copiar_texto(frase): 
        pyperclip.copy(frase)
        pyautogui.hotkey('ctrl', 'v')

pyautogui.click(1919, 1051, duration=2)
sleep(1)
pyautogui.doubleClick(1024,67, duration=2)
sleep(2)
copiar_texto(email)
sleep(1)
pyautogui.hotkey('enter')
sleep(1)
copiar_texto(senha)