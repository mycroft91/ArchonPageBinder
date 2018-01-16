#!/usr/bin/python
#Author      : Mycroft92
#Description : Extracts gifs from bagoum.com, by default downloads all gifs for collection cards

import urllib, urllib2
import os
import shutil
import logging
import re
from bs4 import BeautifulSoup
from src.card_data import *
logging.basicConfig(
    filename="gif_extractor.log", level=logging.DEBUG, filemode='w')


def bagoum_name(cardName):
    #For a card name generates bagoum card name
    pattern = "[a-zA-Z]+"
    name = ''.join(re.findall(pattern, cardName)).lower()
    logging.debug("[*]Found card: " + cardName + " as " + name)
    return name


class gifExtract():
    def __init__(self, cardList):
        #Takes a list of card names(strings) and dumps their gif animations into a folder named "gifs"
        #The card names must be compativle with T2k5's card naming
        self.cards = cardList
        self.baseName = "http://bagoum.com"
        self.cardBase = "http://bagoum.com/cards/"
        #Directory check for removal
        try:
            shutil.rmtree("gifs")
        except Exception as e:
            logging.warning(str(e))

        try:
            os.mkdir("gifs")
        except Exception as e:
            logging.warning(str(e))
            raise (type(e), e.args)

        for card in self.cards:
            try:
                url = self.cardBase + bagoum_name(card)
                soup = BeautifulSoup(urllib2.urlopen(url))
                imgs = soup.findAll("div", {"class": "cardanimhold"})
                for img in imgs:
                    #extracts the exact url for each animation image
                    imgUrl = img.img['src']
                    #downloads it to local folder gifs
                    urllib.urlretrieve(self.baseName + imgUrl,
                                       os.path.join("gifs",os.path.basename(imgUrl)))
            except Exception as e:
                logging.error(str(e))
                raise (type(e), e.args)

#example usage of above class
cards     = collection()
#cardNames = [card['name'] for card in cards]
cardNames = [cards[i]['name'] for i in range(0,100)]
print cardNames
gifExtract(cardNames)