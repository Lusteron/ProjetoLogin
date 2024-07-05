import pyautogui
#alerta
pyautogui.alert(text='Iniciando o programa', title='MegaBot', button='ok')
#como pedir informação
email = pyautogui.prompt(text='Digite seu email:', title='Informações obrigatorias')
print(email)

#confirmar se algo deve ou não acontecer 
resposta = pyautogui.confirm(text='Você confirma?', title='AutoBot', buttons=['sim', 'não', 'cancelar'])

pyautogui.alert(resposta)

# senha
senha = pyautogui.password(text='digite sua senha:', title='AutoBot', mask='*')
print(senha)