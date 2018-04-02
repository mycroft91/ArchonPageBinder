#helper functions reside here
from defines import *

def replace(name):
    #replaces spaces and 'Of','The' with '_','of','the' respectively
    temp = name.replace(' ', '_').replace(
        '_Of_', '_of_').replace('_The_', '_the_')
    return temp


def named_replace(name):
    #replaces  'Of','The' with 'of','the' respectively doesnot affect spaces...needed for handling card names
    temp = name.replace(' Of ', ' of ').replace(' The ', ' the ')
    return temp


def ability(des):
    #ability extraction from card description
    abilities = ''
    for key in keywords.keys():
        if (des.find(key) >= 0):
            abilities += ', '+keywords[key]
    if len(abilities) > 0:
        abilities = abilities[2:]  # trimming the first ', '
    return abilities

def plain_ability(des):
    #returns abilites as keys for category page generation
    abilities = []
    for key in keywords.keys():
        if (des.find(key) >= 0):
            abilities.append(key)
    return abilities




def alternates(link):
    alts = []
    alts.append(link.lower())
    alts.append(link.lower().replace('-', ''))
    alts.append(link.lower().replace(',', ''))
    alts.append(link.lower().replace("'", ''))
    return set(alts)
