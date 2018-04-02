import mwclient
from mwclient import Site
import json
import urllib2
from data import *
import logging
import time
from itertools import islice

class wikiLogin():
    def __init__(self,config="config.txt"):
        try:
            #load user, pass file
            p               = open(config,'r').readlines()
            user            = p[0][5:].strip()
            password        = p[1][5:].strip()
        except Exception as e:
            logging.error(str(e))
            raise (type(e),e.args)
        try:
            self.site            = mwclient.Site('duelyst.gamepedia.com',path='/')
            logging.info("[*]Connected to  duelyst.gamepedia.com ")
            self.site.login(user,password)
            logging.info("[*]Logged in with bot credentials from %s"%config)
        except Exception as e:
            logging.error(str(e))
            raise (type(e),e.args)