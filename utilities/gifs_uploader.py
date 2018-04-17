import mwclient
from mwclient import Site
import logging
import os

##logger settings
logging.basicConfig(level=logging.WARNING)

try:
    #load user, pass file
    p               = open("../config.txt",'r').readlines()
    user            = p[0][5:].strip()
    password        = p[1][5:].strip()

    ua = 'gifs_uploader/0.1 run by User:Explain truck'
    site = mwclient.Site('duelyst.gamepedia.com', clients_useragent=ua, path='/')
    site.login(user, password)

    files = os.listdir('gifs/')

    for filename in files:
        print filename
        page = site.pages['File:' + filename]
        if page.exists == False:
            print page.exists
            site.upload(open('gifs/' + filename), filename=filename, description=filename, ignore=True)
        os.remove('gifs/' + filename)
except Exception as e:
    logging.error(str(e))
