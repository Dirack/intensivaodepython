# coding: utf-8
#
# aula01.py (Python)
# 
# Objetivo: Aula 01 - Automação de tarefas com Python.
# Baixar base de dados e enviar relatório por email.
# 
# Site: https://dirack.github.io
# 
# Versão 1.0
# 
# Programador: Rodolfo A C Neves (Dirack) 09/08/2021
# 
# Email: rodolfo_profissional@hotmail.com
# 
# Licença: GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.txt>.

import pyautogui as pya
import pyperclip as pc
import time
import pandas as pd

# Abrir google chrome no link do google drive
pya.PAUSE = 3
pya.hotkey("win","8")
pc.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pya.hotkey("Ctrl","v")
pya.press("enter")
time.sleep(5)

# Baixar a tabela de vendas
pya.click(x=545,y=403,clicks=2)
time.sleep(3)
pya.click(x=455,y=439)
pya.click(x=1713,y=223)
pya.click(x=1617,y=654)

time.sleep(5)

# Processar tabela de vendas
tabela = pd.read_excel(r'~/Downloads/Vendas - Dez.xlsx')
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Abrir email em nova aba do navegador
pya.hotkey("Ctrl","t")
pc.copy("https://mail.google.com/")
pya.hotkey("Ctrl","v")
pya.press("enter")

# clicar no botão escrever
time.sleep(5)
pya.click(x=177,y=235)
pya.write("rodolfo_profissional@hotmail.com")
pya.press("tab") # escolher email
pya.press("tab") # passar pro campo assunto

# escrever o assunto
pya.write("Estudo Python")
pya.press("tab") # passar para o corpo do email

texto = f"""
Eu quero dizer uma coisa...
uma coisa!
E, além do mais, só te digo isso...

faturamento = {faturamento:,.2f}
quantidade = {quantidade:,.2f}

Att.,

Dirack"""

# Escrever e enviar email
pya.write(texto)
pya.hotkey("Ctrl","enter")
