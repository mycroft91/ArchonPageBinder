#!/usr/bin/python
#Author      : Mycroft92
#Description : This is for the new integrated interface, it's a class that has various functions over cardData(iteration,search,dump the json etc..)

import json
import urllib2
import logging
from defines import unlimited_exp, exception_list
from helper import replace
logger = logging.getLogger("__main__")

class data(object):
    def __init__(self,url,debug=True):
        self.data       = url
        self.debug      = debug
        try:
            self.cards = json.loads(urllib2.urlopen(
                self.data).read())['cardData']
            self.index  = 0
            self.max    = len(self.cards)
            self.cards = [i for i in self.cards if not(
                i['name'] in exception_list)] #removes cards from exception_list
            self._link_info()
            self._rotation_info()
            logger.info("[*]Completed reading card data from from "+self.data)
        except Exception as e:
            logger.error(str(e))
            raise (type(e),e.args)
    
    def _link_info(self):
        #add the wikilink for each card
        for card in self.cards:
            card["link"] = replace(card['name'])
    
    def _rotation_info(self):
        #this should not be called from outside this class
        #adds the rotation info for a card
        for card in self.cards:
            if (card['isLegacy']) or (card['cardSetName'] in unlimited_exp):
                card['isStandard'] = "false"
            else:
                card['isStandard'] = "true"
    
    def organize(self,index="name"):
        if not (index in self.cards[0].keys()):
            logger.warning("[!]Invalid organize index -%s defaulting to name\n "%index)
            index  = "name"
        self.cards = sorted(self.cards,key=lambda k:k[index])
        return self.cards
    
    def getData(self):
        return self.cards
    
    def dump(self,filename=""):
        if(filename==""):
            logger.error("[!]Filename for dumping card info cannot be empty!")
            raise Exception(
                "[!]Filename for dumping card info cannot be empty!")
        with open(filename, 'w') as outfile:
            json.dump(self.cards, outfile)
    
    def filter(self,myfilter={},index="name"):
        #filter data with keys in cardData (look at raw data on T2k5's website)        
        logger.debug("[*]Filtering cards with %s\n"%str(myfilter))
        temp   = self.organize(index)
        warned = False
        for key in myfilter.keys():
            if key in self.cards[0].keys():
                temp = [i for i in temp if i[key]==myfilter[key]]
            else:
                if not warned:
                    logger.warning("[!]key: %s not found in cardlist! Skipping from filter\n"%key)
                    warned = true
        return temp
    


class collectionURL(data):
    #this class is an iterable for collection only data(Data you see in collectuon manager)
    def __init__(self,url="https://duelyststats.info/scripts/carddata/cardData.json"):
        super(collectionURL,self).__init__(url)

class fullCollectionURL(data):
    #this class is an iterable for all cards the game uses.
    def __init__(
            self,
            url="https://duelyststats.info/scripts/carddata/fullCardData.json"):
        super(fullCollectionURL, self).__init__(url)

#in future will implement data generation from JSON dump
