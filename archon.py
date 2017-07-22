#Author: Mycroft92
#Date  : 21-July-2017
import mwclient
from mwclient import Site
import json
import urllib2
from data import *
import logging
import time

##logger settings
logging.basicConfig(filename="Archon.log", level=logging.INFO,filemode='w')

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
    site             = mwclient.Site('duelyst.gamepedia.com',path='/')
    logging.info("[*]Connected to  duelyst.gamepedia.com ")
    site.force_login = False
    logging.info("[*]Setting anonymous edit mode for the bot.")
except Exception as e:
    logging.error(str(e))
    raise (type(e),e.args)

existing_cnt        = 0
nexisting_cnt       = 0
skipped             = 0
successful          = 0
try:
    pages_created   = open("pages_created.txt",'w')
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
    if (page.exists) and (not (card_link in overwrite)):
        logging.info("[*]Page exists for :"+ card['name'])
        existing_cnt  += 1
    else:
        logging.info("[*]Creating page for:" + card['name'])
        text           = None
        if card['isUnit']:
             #minion_template
             fill      = {'faction'     : faction[card['factionName']],
                          'cost'        : card['cost'],
                          'attack'      : card['attack'],
                          'health'      : card['health'],
                          'rarity'      : rarity[card['rarityName']],
                          'ability'     : ability(card['description']),
                          'expansion'   : expansion[card['cardSetName']],
                          'description' : card['description']}
             text      = minion_template%fill
        elif card['isSpell']:
             #spell_template
             fill      = {'faction'     : faction[card['factionName']],
                          'cost'        : card['cost'],
                          'attack'      : card['attack'],
                          'health'      : card['health'],
                          'rarity'      : rarity[card['rarityName']],
                          'expansion'   : expansion[card['cardSetName']],
                          'description' : card['description']}
             text      = spell_template%fill

        elif card['isArtifact']:
             #artifact_template
             fill      = {'faction'     : faction[card['factionName']],
                          'cost'        : card['cost'],
                          'attack'      : card['attack'],
                          'health'      : card['health'],
                          'rarity'      : rarity[card['rarityName']],
                          'expansion'   : expansion[card['cardSetName']],
                          'description' : card['description']}
             text      = artifact_template%fill

        if text:
            result     = page.save(text,'Template Creation for '+card['name'])
            if result['result'] == 'Success':
                pages_created.write(card_link+"\n")
                logging.info("[*]Successfully created page: "+card_link)
                successful  +=1
                time.sleep(10)
            else:
                pages_failed.write(card_link+"\n")
        nexisting_cnt += 1
print "No:of existing cards found: "+str(existing_cnt)
logging.info("No:of existing cards found: "+str(existing_cnt))
print "No:of card pages to be created: "+str(nexisting_cnt)
logging.info("No:of card pages to be created: "+str(nexisting_cnt))
print "No:of successful pages created: "+str(successful)
logging.info("No:of successful pages created: "+str(successful))
print "No:of pages failed to be created: "+str(nexisting_cnt-successful)
logging.info("No:of pages failed to be created: "+str(nexisting_cnt-successful))
print "Find the detailed logs in Archon.log, pages_created.txt,pages_failed.txt"
