#!/usr/bin/python
#Author      : Mycroft92
#Description : This is for the new integrated interface, it's a class that has various functions over cardData(iteration,search,dump the json etc..)

import json
import urllib2
import logging

class data(object):
    def __init__(self,url,debug=True):
        self.data       = url
        self.debug      = debug
        try:
            self.cards = json.loads(urllib2.urlopen(
                self.data).read())['cardData']
            self.index  = 0
            self.max    = len(self.cards)
            logging.info("[*]Completed reading card data from from "+self.data)
        except Exception as e:
            logging.error(str(e))
            raise (type(e),e.args)
    
    def __getitem__(self,index):
        return self.cards[index]

    def __iter__(self):
        return self

    def next(self):
        ##This is a python 2.7 method
        self.index += 1
        if self.debug:
            logging.debug(
                "[*]Returning Card data for:" + self.cards[self.index - 1]
                ['name'] + " index:" + str(self.index - 1))
        if self.index == self.max:
            if self.debug:
                logging.debug(
                    "[*]Successfully returned all " + str(self.max) + " cards")
            raise StopIteration
        return self.cards[self.index - 1]
    
    def dump(self,filename=""):
        pass

    def __next__(self):
        ##This makes it works for python 3+ too
        self.index     += 1
        if self.debug:
            logging.debug("[*]Returning Card data for:"+self.cards[self.index-1]['name']+" index:"+str(self.index-1))
        if self.index ==self.max :
            if self.debug:
                logging.debug("[*]Successfully returned all "+str(self.max)+ " cards")
            raise StopIteration
        return self.cards[self.index - 1]


class collection(data):
    #this class is an iterable for collection only data(Data you see in collectuon manager)
    def __init__(self,url="https://duelyststats.info/scripts/carddata/cardData.json"):
        super(collection,self).__init__(url)

class fullCollection(data):
    #this class is an iterable for all cards the game uses.
    def __init__(
            self,
            url="https://duelyststats.info/scripts/carddata/fullCardData.json"):
        super(fullCollection, self).__init__(url)
