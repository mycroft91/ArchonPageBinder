#Author: Mycroft92
#Date  : 21-July-2017
#this is used to sub for the rarity image correspondingly. Basic doesnt have an image on wiki
redirect        = "#REDIRECT [[%(link)s]]"

rarity          = { 'Basic'     :'Basic',
                    'Token'     :'Token',
                    'Common'    :'|[[file:crarity.png|center]]',
                    'Rare'      :'|[[file:rrarity.png|center]]',
                    'Epic'      :'|[[file:erarity.png|center]]',
                    'Legendary' :'|[[file:lrarity.png|center]]'}

expansion_des   = { 'Core'               :'Core',
                    "Shim'Zar"           :"[https://news.duelyst.com/duelyst-patch-1-71/ v. 1.71] - added with the [[Denizens of Shim'Zar]] expansion.",
                    "Unearthed Prophecy" :"[https://news.duelyst.com/unearthed-prophecy-live/ v. 1.87] - added with the [[Unearthed Prophecy]] expansion.",
                    "Bloodbound"         :"[https://news.duelyst.com/rise-of-the-bloodborn-duelyst-patch-1-78/ v. 1.78] - added with the [[Rise of the Bloodborn]] expansion",
                    "Ancient Bonds"      :"[https://news.duelyst.com/duelyst-patch-1-81/ v. 1.81] - added with the [[Ancient Bonds]] expansion.",
                    "Gauntlet Specials"  :"[https://news.duelyst.com/duelyst-patch-1-85/ v 1.85] - added with [[Gauntlet Specials]]"}

expansion       = { 'Core'               :'Core',
                    "Shim'Zar"           :"[[Shim'Zar]]",
                    "Unearthed Prophecy" :"[[Unearthed Prophecy]]",
                    "Bloodbound"         :"[[Rise of the Bloodbound]]",
                    "Ancient Bonds"      :"[[Ancient Bonds]]",
                    "Gauntlet Specials"  :"[[Gauntlet Specials]]" }

faction         = { 'Lyonar Kingdoms'    :'[[Lyonar]]',
                    'Songhai Empire'     :'[[Songhai]]',
                    'Vetruvian Imperium' :'[[Vetruvian]]',
                    'Abyssian Host'      :'[[Abyssian]]',
                    'Magmar Aspects'     :'[[Magmar]]',
                    'Vanar Kindred'      :'[[Vanar]]',
                    'Neutral'            :'[[Neutral]]',
                    'Boss'               :'[[Boss]]'}

keywords        = { 'Airdrop'            :'[[Airdrop]]',
                    'Backstab'           :'[[Backstab]]',
                    'Blast'              :'[[Blast]]',
                    'Blood Surge'        :'[[Blood Surge]]',
                    'Bond'               :'[[Bond]]',
                    'Celerity'           :'[[Celerity]]',
                    'Deathwatch'         :'[[Deathwatch]]',
                    'Dying Wish'         :'[[Dying Wish]]',
                    'Exhuming Sand'      :'[[Exhuming Sand]]',
                    'Flying'             :'[[Flying]]',
                    'Forcefield'         :'[[Forcefield]]',
                    'Frenzy'             :'[[Frenzy]]',
                    'Grow'               :'[[Grow]]',
                    'Infiltrate'         :'[[Infiltrate]]',
                    'Opening Gambit'     :'[[Opening Gambit]]',
                    'Primal Flourish'    :'[[Primal Flourish]]',
                    'Provoke'            :'[[Provoke]]',
                    'Ranged'             :'[[Ranged]]',
                    'Rebirth'            :'[[Rebirth]]',
                    'Rush'               :'[[Rush]]',
                    'Sentinel'           :'[[Sentinel]]',
                    'Shadow Creep'       :'[[Shadow Creep]]',
                    'Stun'               :'[[Stun]]',
                    'Summon Dervish'     :'[[Summon Dervish]]',
                    'Zeal'               :'[[Zeal]]'}

boss_template = """{{Template:Cardinfo}}
|-
|'''Faction'''
|%(faction)s
|-
|'''Cost'''
|%(cost)s
|-
|'''Attack'''
|%(attack)s
|-
|'''Health'''
|%(health)s
|-
|'''Rarity'''
|%(rarity)s
|-
|'''Ability'''
|%(ability)s
|-
|'''Expansion'''
|%(expansion)s
|-
|}



==Boss Ability==
%(description)s


<!-- ArchonBot -->
"""

minion_template = """{{Template:Cardinfo}}
|-
|'''Faction'''
|%(faction)s
|-
|'''Cost'''
|%(cost)s
|-
|'''Attack'''
|%(attack)s
|-
|'''Health'''
|%(health)s
|-
|'''Rarity'''
|%(rarity)s
|-
|'''Ability'''
|%(ability)s
|-
|'''Expansion'''
|%(expansion)s
|-
|}



==Balance Changes==
%(description)s


<!-- ArchonBot -->
"""

artifact_template = """{{Template:Cardinfo}}
|-
|'''Faction'''
|%(faction)s
|-
|'''Cost'''
|%(cost)s
|-
|'''Durability'''
|3
|-
|'''Rarity'''
|%(rarity)s
|-
|'''Ability'''
|
|-
|'''Expansion'''
|%(expansion)s
|-
|}

==Balance Changes==
%(description)s


<!-- ArchonBot -->
"""

spell_template   = """{{Template:Cardinfo}}
|-
|'''Faction'''
|%(faction)s
|-
|'''Cost'''
|%(cost)s
|-
|'''Rarity'''
|%(rarity)s
|-
|'''Ability'''
|
|-
|'''Expansion'''
|%(expansion)s
|-
|}

==Balance Changes==
%(description)s


<!-- ArchonBot -->
"""
#This forces bot resets

try:
    overwrite      = open("overwrite.txt",'r').readlines()
    overwrite      = [i.strip() for i in overwrite]
except IOError:
    overwrite      = []
##These listed entities are considered cards by the system but they are not
exception_list = [  "Zen'Rui, The BlightSpawned",#the page is already present as Zen'Rui, The Blightspawned (lowercase s)
                    "Mind Control",
                    "Fight!",
                    "Teleport To Shadow Creep",
                    "Bounce Minion Spawn Entity",
                    "Shadowspawn",
                    "Abyssal Scar",
                    "Teleport",
                    "Riddle",
                    "Activate Battlepet",
                    "Clone Self",
                    "Clone Entity",
                    "Double Attack And Health",
                    "Kinetic Surge",
                    "Warbird",
                    "Seeking Eye",
                    "Overload",
                    "Psionic Strike",
                    "Iron Shroud",
                    "Arcane Heart",
                    "Blink",
                    "Afterglow",
                    "Roar",
                    "Assassinate",
                    "Kill Target",
                    "Revive Dead minion",
                    "Random Teleport",
                    "Heal Damge",
                    "Deal Damage",
                    "Dunecaster Followup",
                    "Deploy MECHAZ0R",
                    "Teleport General",
                    "Spell Damge",
                    "Repulsion",
                    "Spawn Entity",
                    "Apply Modifiers",
                    "Teleport Enemy To Me",
                    "Mana Spring",
                    "Shadow Creep Tile",
                    "Hallowed Ground",
                    "Exhuming Sand",
                    "Primal Flourish"]

def replace(name):
    #replaces spaces and 'Of','The' with '_','of','the' respectively
    temp = name.replace(' ','_').replace('_Of_','_of_').replace('_The_','_the_')
    return temp

def ability(des):
    #ability extraction from card description
    abilities = ''
    for key in keywords.keys():
        if (des.find(key) >=0):
            abilities += ', '+keywords[key]
    if len(abilities) >0:
        abilities = abilities[2:] #trimming the first ', '
    return abilities

def alternates(link):
    alts = []
    alts.append(link.lower())
    alts.append(link.lower().replace('-',''))
    alts.append(link.lower().replace("'",''))
    return set(alts)

if __name__ == '__main__':
    print ability("<b>Provoke</b><br><b>Zeal</b>: Gains +2 Attack.")
    print ability("<b>Opening Gambit</b>: Give ANY nearby minion +2 Attack, but -2 Health.")
    print ability("<b>Dying Wish</b>: Summon two 2/2 Iron Dervishes nearby.")
