# - ETAPAS DO PROJETO DE BOT DE AUTOMAÇÃO, RPA - 

# ETAPA 1 - ACESSAR NO SISTEMA DA EMPRESA
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

#importação da biblioteca PyAutoGui
import pyautogui

import time

# Legenda de alguns comandos

# [clicar] -> pyautogui.click
# [escrever] -> pyautogui.write
# [apertar determinada tecla] -> pyautogui.press
# [apertar] -> pyautogui.hotkey
#[rolar página] -> pyautogui.scroll

#define o tempo de espera dos comandos do pyautogui
pyautogui.PAUSE = 0.5


#abre o sistema(usando o chrome)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar carregar a página
time.sleep(3)

# ETAPA 2 - FAZER O LOGIN




#fazer o login
pyautogui.click(x=832, y=477)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=788, y=595)
pyautogui.press("enter")



# ETAPA 3 - IMPORTAR A BD
#instalação do pandas pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # ETAPA 4 - CADASTRAR UM PRODUTO

    pyautogui.click(x=823, y=320)

    #código
    # codigo = tabela.loc[linha, "codigo"]
    pyautogui.write (tabela.loc[(linha, "codigo")])
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"])) #ou pyautogui.write("1")
    pyautogui.press("tab")
    #preço_unitário
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"])) #ou pyautogui.write(srt(25.95))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
      pyautogui.write(obs)


    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    #rolagem de tela
    pyautogui.scroll(5000)

# ETAPA 5 - REPETIR O PROCESSO ATÉ ACABAR A BD
