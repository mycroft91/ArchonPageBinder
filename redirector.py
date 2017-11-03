#Author: Mycroft92
#Date  : 02-August-2017
import mwclient
from mwclient import Site
import json
import urllib2
from data import *
import logging
import time
from itertools import islice

##logger settings
logging.basicConfig(filename="Redirected.log", level=logging.INFO,filemode='w')

#t2k5's card data url
card_url            = "https://duelyststats.info/scripts/carddata/cardData.json"

#load it into a python object
try:
    card_data       = json.loads(urllib2.urlopen(card_url).read())
    logging.info("[*]Downloaded card data successfully.")
except Exception as e:
    logging.error(str(e))
    raise (type(e),e.args)

try:
    #load user, pass file
    p               = open("config.txt",'r').readlines()
    user            = p[0][5:].strip()
    password        = p[1][5:].strip()
except Exception as e:
    logging.error(str(e))
    raise (type(e),e.args)
try:
    site            = mwclient.Site('duelyst.gamepedia.com',path='/')
    logging.info("[*]Connected to  duelyst.gamepedia.com ")
    site.login(user,password)
    logging.info("[*]Logged in with bot credentials from config.txt.")
except Exception as e:
    logging.error(str(e))
    raise (type(e),e.args)

redirected_cnt      = 0
failed_cnt          = 0

try:
    pages_created   = open("pages_redirected.txt",'w')
    pages_failed    = open("pages_failed.txt",'w')
except OSError:
    logging.error("[!]Cannot create log file for created pages! No write permissions.")
    raise (OSError,"No permissions to create log files.")

for card in card_data['cardData']:
    if card['name'] in exception_list:
        continue
    card_link          = replace(card['name']) #replaces spaces and 'Of','The' with '_','of','the' respectively
    if card_link.find("_")<0:
        continue
    link_success       = []
    link_fail          = []
    for alt_link in alternates(card_link):
        page           = site.pages[alt_link]
        if not (page.exists):
            result     = page.save(redirect%{'link':named_replace(card['name'])})
            if result['result'] == "Success":
                link_success.append(alt_link)
            else:
                link_fail.append(alt_link)
        else:
            if page.exists: #this is needed else latest_rev might throw IndexError if page is not present
                latest_rev = "Mycroft92"
                for rev in islice(page.revisions(),1):
                    latest_rev     = rev['user']    #this is one tricky way to get the last element, no cleaner way available
                if latest_rev     != "Mycroft92":  ##If the latest edit is not by me then dont disturb it
                    logging.info("[*]Skipping page :" + card['name']+",Latest edit made by:"+latest_rev)
                    continue
                result     = page.save(redirect%{'link':named_replace(card['name'])})
                if result['result'] == "Success":
                    link_success.append(alt_link)
                else:
                    link_fail.append(alt_link)
    if link_success:
        logging.info("[*]Successfully created redirects:"+",".join(link_success))
        pages_created.write(",".join(link_success)+"\n")
        time.sleep(2)
    if link_fail:
        logging.error("[!]Failed in creating redirects:"+",".join(link_fail))
        pages_failed.write(",".join(link_fail)+"\n")
logging.info("[*]Finished creating redirects.")
