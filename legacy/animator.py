#Author: Mycroft92
#Date  : 21-Dec-2017
import mwclient
from mwclient import Site
import json
import urllib2
from data import *
from animation_templates import *
import logging
import time
from itertools import islice

##logger settings
logging.basicConfig(filename="animations.log", level=logging.INFO,filemode='w')

#t2k5's card data url
#card_url            = "https://duelyststats.info/scripts/carddata/cardData.json"
card_url             = "https://duelyststats.info/scripts/carddata/cardData.json"

#load it into a python object
try:
    card_data       = json.loads(urllib2.urlopen(card_url).read())
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


nexisting_cnt       = 0
skipped             = 0
successful          = 0
try:
    pages_created   = open("pages_added.txt",'w')
    pages_failed    = open("pages_failed.txt",'w')
except OSError:
    logging.error("[!]Cannot create log file for created pages! No write permissions.")
    raise (OSError,"No permissions to create log files.")

for card in card_data['cardData']:
    if card['name'] in exception_list:
        skipped       += 1
        continue #skip processing for exceptions
    card_link          = replace(card['name']) #replaces spaces and 'Of','The' with '_','of','the' respectively
    page               = site.pages[card_link]
    if not (page.exists):
        logging.info("[-]Page doesnt exist for :"+ card['name'])
        nexisting_cnt  += 1
    else:
        #if page.exists: #this is needed else latest_rev might throw IndexError if page is not present
            #Removed the check for the last edit, I screwed up the last one
        #if not(card['factionName'] in faction.keys()):
        #    logging.info("[*]Skipping page :" + card['name'])
        #    skipped += 1
        logging.info("[*]Adding animations page for:" + card['name'])
        text        = page.text()
        ##Replace all text related to animations
        for i in remove_lines:
            text = text.replace(i,"")
        ##^All duplicates removed
        cat         = ""
        anim        = ""
        if card['isUnit']:
            anim    = minion_animation_template
        elif card['isSpell']:
            anim    = spell_animation_template
        elif card['isArtifact']:
            anim    = artifact_animation_template
        text       += anim
        result     = page.save(text,'Adding animations for '+card['name'])
        if result['result'] == 'Success':
            try:
                pages_created.write(card_link+"\n")
            except UnicodeEncodeError:
                logging.info("[-]warning some card text could not be printed onto txt file:"+card_link)
            logging.info("[*]Successfully created page: "+card_link)
            successful  +=1
            time.sleep(1)
        else:
            pages_failed.write(card_link+"\n")
            logging.info("[!]Failed to write card:"+card['name'])
            skipped     += 1

print "No:of card pages to be created: "+str(nexisting_cnt)
logging.info("No:of card pages to be created: "+str(nexisting_cnt))
print "No:of successful pages created: "+str(successful)
logging.info("No:of successful pages created: "+str(successful))
print "No:of pages skipped: "+str(skipped)
logging.info("No:of pages skipped: "+str(skipped))
print "Find the detailed logs in animator.log, pages_created.txt,pages_failed.txt"
