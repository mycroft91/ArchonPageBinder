
#Author: Mycroft92
#Date  : 21-July-2017
import mwclient
from mwclient import Site
import json
import urllib2
from data import *
import logging
import time
from itertools import islice

##logger settings
logging.basicConfig(filename="loreweaver.log", level=logging.INFO,filemode='w')

#t2k5's card data url
card_url            = "https://duelyststats.info/scripts/carddata/cardData.json"
#card_url             = "https://duelyststats.info/scripts/carddata/fullCardData.json"
#t2k5's card lore url
lore_url             = "https://duelyststats.info/scripts/carddata/cardLore.json"

#load it into a python object
try:
    #card_data       = json.loads(urllib2.urlopen(card_url).read())
    lore_data       = json.loads(urllib2.urlopen(lore_url).read())
    ##if reading from a file comment out above and uncomment below
    #with open("tempData.txt") as json_data:
    #    card_data        = json.load(json_data)
    #logging.info("[*]Downloaded card data successfully.")
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


skipped             = 0
successful          = 0
failed              = 0
try:
    lore_created    = open("lore_created.txt",'w')
    lore_failed     = open("lore_failed.txt",'w')
except OSError:
    logging.error("[!]Cannot create log file for created pages! No write permissions.")
    raise (OSError,"No permissions to create log files.")

cnt  = False #variable to check existing lore
for card in lore_data:
    if card['cardName'] in exception_list:
        skipped       += 1
        continue #skip processing for exceptions
    card_link          = replace(card['cardName']) #replaces spaces and 'Of','The' with '_','of','the' respectively
    page               = site.pages[card_link]
    if page.exists: #this is needed else latest_rev might throw IndexError if page is not present
        for rev in page.revisions():
            rev_sum        = rev['comment']    #this is one tricky way to get the last element, no cleaner way available
            if rev_sum     == "Lore added for "+card['cardName']:  ##If the latest edit is not by me then dont disturb it
                logging.info("[*]Skipping page :" + card['cardName']+",lore already added by "+rev['user'])
                skipped        +=1
                cnt     = True
        if cnt:
            cnt = False
            continue
        logging.info("[*]Adding lore for:" + card['cardName'])
        text           = page.text()
        fill           = {'text':card['text']}
        text           = text+lore_template%fill
        result         = page.save(text,"Lore added for "+card['cardName'])
        if result['result'] == 'Success':
            lore_created.write(card_link+"\n")
            logging.info("[*]Successfully created lore for page: "+card_link)
            successful  +=1
            time.sleep(1)
        else:
            lore_failed.write(card_link+"\n")
            failed += 1
print "No:of existing card lore found: "+str(len(lore_data))
logging.info("No:of existing cards found: "+str(len(lore_data)))
print "No:of successful pages created: "+str(successful)
logging.info("No:of successful pages created: "+str(successful))
print "No:of pages failed to be created: "+str(failed)
logging.info("No:of pages failed to be created: "+str(failed))
print "No:of pages skipped: "+str(skipped)
logging.info("No:of pages skipped: "+str(skipped))
print "Find the detailed logs in loreweaver.log, lore_created.txt,lore_failed.txt"
