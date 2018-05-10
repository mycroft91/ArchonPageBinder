from src import card_data, wiki_login
from src.wiki_defines import *
from src.helper import *
from src.defines import *
import logging
import sys

#These templates are only needed here
#If a use use arises in some other script move these to wiki_defines.py
factions = faction.keys()



def createFactionPages():
    cards = card_data.fullCollectionURL()
    wiki  = wiki_login.wiki()
    for f in factions:
        if f == "Boss":
            continue #skip boss faction
        text    = wiki.getPage(replace(f))
        tok_str = text[text.find("== Tokens =="):]
        text    = text[:text.find("== Minions ==")] + minion_start
        filt    = {"factionName":f,'isUnit': True}
        for card in cards.filter(filt):
            if card["prismatic"] == True:
                continue
            filler = {
                'name'    :named_replace(card['name']),
                'irare'   :rarity_img[card['rarityName']],
                'rarity'  :card['rarityName'],
                'cost'    :card['cost'],
                'attack'  :card['attack'],
                'health'  :card['health'],
                'ability' :linkify(card['description']),
                'set'     :card['cardSetName'].lower()}
            if not( card['rarityName'] == 'Token'):
                text = text+minion_fill%filler
        text += minion_end
        text += artifact_start
        filt  = {"factionName":f,'isArtifact': True}
        for card in cards.filter(filt):
            if card["prismatic"] == True:
                continue
            filler = {
                'name'   : named_replace(card['name']),
                'irare'  : rarity_img[card['rarityName']],
                'rarity' : card['rarityName'],
                'cost'   : card['cost'],
                'attack' : card['attack'],
                'health' : card['health'],
                'ability': linkify(card['description']),
                'set'    : card['cardSetName'].lower()}
            if not (card['rarityName'] == 'Token'):
                text = text+artifact_fill % filler

        text += spell_start
        filt = {"factionName": f, 'isSpell': True}
        for card in cards.filter(filt):
            if card["prismatic"] == True:
                continue
            filler = {
                'name'   : named_replace(card['name']),
                'irare'  : rarity_img[card['rarityName']],
                'rarity' : card['rarityName'],
                'cost'   : card['cost'],
                'attack' : card['attack'],
                'health' : card['health'],
                'ability': linkify(card['description']),
                'set'    : card['cardSetName'].lower()}
            if not (card['rarityName'] == 'Token'):
                text = text+spell_fill % filler
        text += spell_end
        text += tok_str        
        if (wiki.editPage(replace(f),text,force=True)):
            logging.info("[*]Successfully created faction page for:"+f+"\n")
        else:
            logging.info("[!]Failed to create faction page for:"+f+"\n")

if __name__ == "__main__":
    logging.basicConfig(filename="CreateExpansion.log",
                    level=logging.DEBUG, filemode='w')
    logger = logging.getLogger(__name__)
    createFactionPages()

