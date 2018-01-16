#!/usr/bin/python
#Author      : Mycroft92
#Description : This is to generate list of tokens from full card data,uses the new interface

from src.card_data import *
import logging
from data import *

logging.basicConfig(
    filename="token_extractor.log", level=logging.DEBUG, filemode='w')

try:
    token_list = open("tokens.txt", 'w')
except Exception as e:
    logging.error(str(e))
    raise (type(e),e.args)

tokens  = []
for card in fullCollection():
    if card['rarityName'] == 'Token' :
        key = card['factionName']+":"+card['name']+'\n'
        if not key in tokens:
            token_list.write(key)
            tokens.append(key)


