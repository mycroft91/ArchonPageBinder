from src import card_data,wiki_login
from src.wiki_defines import *
from src.helper import *
from src.defines import *
import logging,sys



def createExpansion(name,patch):
    cards         = card_data.fullCollectionURL()
    wiki          = wiki_login.wiki()
    minions       = cards.filter({'isUnit': True, 'cardSetName':name})
    pages_created = open("pages_created.txt", 'w')
    pages_failed  = open("pages_failed.txt", 'w')
    pages_forced  = open("pages_forced.txt", 'w')
    #minions
    for card in minions:
        ability_cat = "".join([keyword_category%i for i in plain_ability(card['description'])] )
        minion_fill = {'faction': faction[card['factionName']],
            'cost': card['cost'],
            'attack': card['attack'],
            'health': card['health'],
            'rarity': rarity[card['rarityName']],
            'expansion': expansion[card['cardSetName']],
            'description': expansion_des.get(card['cardSetName'], " "),
            'standard':card["isStandard"],
            'ability' : linkify(card['description']),
            'Cfaction': replace(card['factionName']),
            'Cexpansion':replace(plain_expansion[card['cardSetName']])          }
        if(wiki.createPage(card['link'],(minion_template%minion_fill) + "\n"+ability_cat)):
            pages_created.write(card["link"]+"\n")
        else:
            pages_failed.write(card["link"]+"\n")

    #spells
    spells = cards.filter({'isSpell': True, 'cardSetName': name})
    for card in spells:
        spell_fill = {'faction': faction[card['factionName']],
        'cost': card['cost'],
        'attack': card['attack'],
        'health': card['health'],
        'rarity': rarity[card['rarityName']],
        'expansion': expansion[card['cardSetName']],
        'description': expansion_des.get(card['cardSetName'], " "),
        'ability' : linkify(card['description']),
        'standard': card["isStandard"],
        'Cfaction': replace(card['factionName']),
        'Cexpansion': replace(plain_expansion[card['cardSetName']])  }
        if(wiki.editPage(card['link'], spell_template % spell_fill)):
            pages_created.write(card["link"]+"\n")
        else:
            pages_failed.write(card["link"]+"\n")
    
    #artifacts
    artifacts = cards.filter({'isArtifact': True, 'cardSetName': name})
    for card in artifacts:
        artifact_fill = {'faction': faction[card['factionName']],
        'cost': card['cost'],
        'attack': card['attack'],
        'health': card['health'],
        'rarity': rarity[card['rarityName']],
        'expansion': expansion[card['cardSetName']],
        'description': expansion_des.get(card['cardSetName'], " "),
        'ability' : linkify(card['description']),
        'standard': card["isStandard"],
        'Cfaction': replace(card['factionName']),
        'Cexpansion': replace(plain_expansion[card['cardSetName']])}
        if(wiki.editPage(card['link'], artifact_template % artifact_fill)):
            pages_created.write(card["link"]+"\n")
        else:
            pages_failed.write(card["link"]+"\n")
    cards.dump(patch+".json")
    wiki.report()

if __name__ == "__main__":
    logging.basicConfig(filename="CreateExpansion.log",
                        level=logging.DEBUG, filemode='w')
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    createExpansion("Mythron","V1.95fulCard")
