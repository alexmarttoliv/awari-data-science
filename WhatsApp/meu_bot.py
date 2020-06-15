# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:17:27 2020

@author: alexm
"""
#importar pacotes necessários
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd

#inicializar whatsapp
wp = WhatsApp()

#esperar que ENTER seja pressionado
input('Pressione enter após escanear o QR Code')

#lista de nomes ou números de telefone a serem pesquisados
#o nome não deve ser ambiguo pois ele retornará o primeiro resultado
#nomes_palavras_chave = ['Felipe Abrantes', 'Lucas Bot', 'Jose Bot', 'João Bot']

msg = pd.read_excel('exemplo_mensagens.xlsx')

nomes_palavras_chave = list(msg['Contato'])

mensagens = list(msg['Mensagem'])

#lista dos nomes na mensagem
#primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chave]

#lista de produtos
#lista_produtos = ['açucar', 'feijão', 'abacate', 'cenoura']

#loop para mandar mensagens
for nome_pesquisar, mensagem in zip(nomes_palavras_chave, mensagens):
    wp.search_contact(nome_pesquisar)

    #mensagem = f'Olá {nome_pesquisar}! Obrigado por comprar o produto {produto}!'

    sleep(2)
    wp.send_message(mensagem)

#esperar 10 segundos e fechar
sleep(10)
wp.driver.close()
