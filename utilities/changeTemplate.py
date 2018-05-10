from src import card_data, wiki_login
from src.wiki_defines import *
from src.helper import *
from src.defines import *
import logging
import sys
old_rarity = {'Basic': 'Basic',
                   'Token': 'Token',
                   'Common': 'Common',
          'Rare': '|[[file:rrarity.png|center]]',
          'Epic': '|[[file:erarity.png|center]]',
          'Legendary': '|[[file:lrarity.png|center]]',
              'Mythron': '|[[file:mrarity.png|center]]Mythron'}
old_minion_template = ["""|'''Rarity'''
|%(rarity)s
|-""",
"""|'''Rarity'''
|Common
|-"""]

new_minion_template = """|'''Rarity'''
|%(rarity)s
|-"""

old_artifact_template = [""""|'''Rarity'''
|%(rarity)s
|-""",
"""|'''Rarity'''
|Common
|-"""]

new_artifact_template = """|'''Rarity'''
|%(rarity)s
|-"""

old_spell_template = ["""|'''Rarity'''
|%(rarity)s
|-""",
"""|'''Rarity'''
|Common
|-"""]

new_spell_template = """|'''Rarity'''
|%(rarity)s
|-"""


def getOldCardText(card):
    text = []
    if card['factionName'] == "Tutorial Teacher":
        return []
    if card['isUnit']:
        fill = {'faction': faction[card['factionName']],
                'cost': card['cost'],
                'attack': card['attack'],
                'health': card['health'],
                'rarity': old_rarity[card['rarityName']],
                'ability': card['description'],
                'expansion': expansion[card['cardSetName']],
                'description': expansion_des.get(card['cardSetName'], " ")}
        print fill['rarity']
        for t in old_minion_template:
            text.append(t%fill)
    
    elif card['isSpell']:
        #spell_template
        fill = {'faction': faction[card['factionName']],
                'cost': card['cost'],
                'attack': card['attack'],
                'health': card['health'],
                'rarity': old_rarity[card['rarityName']],
                'expansion': expansion[card['cardSetName']],
                'ability': card['description'],
                'description': expansion_des.get(card['cardSetName'], " ")}
        print fill['rarity']
        for t in old_spell_template:
            text.append(t % fill)

    elif card['isArtifact']:
         #artifact_template
        fill = {'faction': faction[card['factionName']],
                'cost': card['cost'],
                'attack': card['attack'],
                'health': card['health'],
                'rarity': old_rarity[card['rarityName']],
                'expansion': expansion[card['cardSetName']],
                'ability' :card['description'],
                'description': expansion_des.get(card['cardSetName'], " ")}
        print fill['rarity']
        for t in old_artifact_template:
            text.append(t % fill)
    return text  
        

def getNewCardText(card):
    text = ""
    if card['factionName'] == "Tutorial Teacher":
        return ""
    if card['isUnit'] :
        ability_cat = "".join([keyword_category %
                               i for i in plain_ability(card['description'])])
        minion_fill = {'faction': faction[card['factionName']],
                       'cost': card['cost'],
                       'attack': card['attack'],
                       'health': card['health'],
                       'rarity': rarity[card['rarityName']],
                       #'ability': linkify(ability(card['description'])),
                       'expansion': expansion[card['cardSetName']],
                       'description': expansion_des.get(card['cardSetName'], " "),
                       'standard': card["isStandard"],
                       'ability': linkify(card['description']),
                       'Cfaction': replace(card['factionName']),
                       'Cexpansion': replace(plain_expansion[card['cardSetName']])}
        text = new_minion_template%minion_fill
    elif card['isSpell']:
        spell_fill = {'faction': faction[card['factionName']],
                      'cost': card['cost'],
                      'attack': card['attack'],
                      'health': card['health'],
                      'rarity': rarity[card['rarityName']],
                      'expansion': expansion[card['cardSetName']],
                      'description': expansion_des.get(card['cardSetName'], " "),
                      'ability': linkify(card['description']),
                      'standard': card["isStandard"],
                      'Cfaction': replace(card['factionName']),
                      'Cexpansion': replace(plain_expansion[card['cardSetName']])}
        text = new_spell_template%spell_fill
    
    elif card['isArtifact']:
        artifact_fill = {'faction': faction[card['factionName']],
                         'cost': card['cost'],
                         'attack': card['attack'],
                         'health': card['health'],
                         'rarity': rarity[card['rarityName']],
                         'expansion': expansion[card['cardSetName']],
                         'description': expansion_des.get(card['cardSetName'], " "),
                         'ability': linkify(card['description']),
                         'standard': card["isStandard"],
                         'Cfaction': replace(card['factionName']),
                         'Cexpansion': replace(plain_expansion[card['cardSetName']])}
        text = new_artifact_template%artifact_fill
    return text

def changeTemplate():
    pages_created = open("pages_changed.txt", 'w')
    pages_failed = open("pages_failed.txt", 'w')
    cards = card_data.fullCollectionURL()
    wiki  = wiki_login.wiki()
        
    for card in cards.filter({"prismatic":False}):
        text = wiki.getPage(card['link'])
        copy = text
        old  = getOldCardText(card)
        new  = getNewCardText(card)
        if(old):
            for i in old:
                print text.find(i)
                text = text.replace(i,new) 
            if(copy == text):
                continue
            if(wiki.editPage(card['link'],text,force=True)):
                try:
                    pages_created.write(card['link']+"\n")
                except Exception as e:
                    logger.info("[!]Couldn't write the url of some card")
            else:
                pages_failed.write(card['link']+"\n")

if __name__ == "__main__":
    logging.basicConfig(filename="ChangeTemplate.log",
                        level=logging.DEBUG, filemode='w')
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    changeTemplate()

        

