#templates and other data that fills pages goes here,
#general info regarding rotations etc goes into defines.py

overwrite_list = []
rarity         = {
    'Basic'     : 'Basic',
    'Token'     : 'Token',
    'Common'    : '|[[file:crarity.png|center]]Common',
    'Rare'      : '|[[file:rrarity.png|center]]Rare',
    'Epic'      : '|[[file:erarity.png|center]]Epic',
    'Legendary' : '|[[file:lrarity.png|center]]Legendary',
    'Mythron'   : '|[[file:mrarity.png|center]]Mythron'
}

keyword_category = """
[[Category:%s]]"""

expansion_des    = {
    'Core':    'Core',
    "Shim'Zar":
    "[https://news.duelyst.com/duelyst-patch-1-71/ v. 1.71] - added with the [[Denizens of Shim'Zar]] expansion.",
    "Unearthed Prophecy":
    "[https://news.duelyst.com/unearthed-prophecy-live/ v. 1.87] - added with the [[Unearthed Prophecy]] expansion.",
    "Bloodbound":
    "[https://news.duelyst.com/rise-of-the-bloodborn-duelyst-patch-1-78/ v. 1.78] - added with the [[Rise of the Bloodborn]] expansion",
    "Ancient Bonds":
    "[https://news.duelyst.com/duelyst-patch-1-81/ v. 1.81] - added with the [[Ancient Bonds]] expansion.",
    "Immortal":
    "[https://duelyst.com/news/immortal-vanguard-live v. 1.92] - added with the [[Immortal Vanguard]] expansion.",
    "Gauntlet Specials":
    "[https://news.duelyst.com/duelyst-patch-1-85/ v. 1.85] - added with [[Gauntlet Specials]]",
    "Mythron" :
    "[https://duelyst.com/news/Trials-Of-Mythron-Live v. 1.95] - added with [[Trials of Mythron]] expansion"
}

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
[[Category:%(faction)s]]
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
|'''Standard'''
|%(standard)s
|-
|}


==Description==
%(ability)s

==Balance Changes==
%(description)s

==Animations==
{{Template:Animation}}

<!-- ArchonBot -->
[[Category:Minion]]
[[Category:%(Cfaction)s]]
[[Category:%(Cexpansion)s]]
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
|%(ability)s
|-
|'''Expansion'''
|%(expansion)s
|-
|'''Standard'''
|%(standard)s
|-
|}

==Description==
%(ability)s

==Balance Changes==
%(description)s

==Animations==
{{Template:ArtifactAnimation}}

<!-- ArchonBot -->
[[Category:Artifact]]
[[Category:%(Cfaction)s]]
[[Category:%(Cexpansion)s]]
"""
lore_template = """

==Card Lore==
%(text)s

"""
spell_template = """{{Template:Cardinfo}}
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
|%(ability)s
|-
|'''Expansion'''
|%(expansion)s
|-
|'''Standard'''
|%(standard)s
|-
|}

==Description==
%(ability)s

==Balance Changes==
%(description)s

==Animations==
{{Template:SpellAnimation}}


<!-- ArchonBot -->
[[Category:Spell]]
[[Category:%(Cfaction)s]]
[[Category:%(Cexpansion)s]]
"""

##templates for faction pages


rarity_img = {
    'Basic'     : 'Basic',
    'Token'     : 'Token',
    'Common'    : 'crarity.png',
    'Rare'      : 'rrarity.png',
    'Epic'      : 'erarity.png',
    'Legendary' : 'lrarity.png',
    'Mythron'   : 'mrarity.png'
}

minion_start = """== Minions ==
{| class="wikitable collapsible sortable" style="text-align: center; width: 70%;"
!Image
!Name
!Rarity
!Type
!Cost
!Attack
!Health
!Ability
!Set
|-
"""
minion_fill = """
|[[File:%(name)s.png|160px|link=%(name)s]] || [[%(name)s]] || [[Image:%(irare)s|40px|]]<br>%(rarity)s || Minion || %(cost)s || %(attack)s || %(health)s || %(ability)s
|{{set|%(set)s}}
|-
"""
minion_end = "|}"

artifact_start = """== Artifacts ==
{| class="wikitable collapsible sortable" style="text-align: center; width: 70%;"
!Image
!Name
!Rarity
!Type
!Cost
!Effect
!
|-"""
artifact_fill = """ |[[File:%(name)s.png|160px|link=%(name)s]] || [[%(name)s]] || [[Image:%(irare)s|40px|]]<br>%(rarity)s|| Artifact || %(cost)s || %(ability)s
|{{set|%(set)s}}
|-"""
artifact_end  = "|}"

spell_start = """
== Spells ==
{| class="wikitable collapsible sortable" style="text-align: center; width: 70%;"
!Image
!Name
!Rarity
!Type
!Cost
!Effect
!Set
|-"""
spell_fill = """
|[[File:%(name)s.png|160px|link=%(name)s]] || [[%(name)s]] || [[Image:%(irare)s|40px|]]<br>%(rarity)s || Spell || %(cost)s || %(ability)s
|{{set|%(set)s}}
|- """
spell_end  = "|}"

token_start = """ 
== Tokens ==
{| class="wikitable collapsible sortable" style="text-align: center; width: 70%;"
!Image
!Name
!Type
!Cost
!Attack
!Health
!Summoned from
!Ability
!Set
|-"""

#token fill is minion_fill for minions, spell_fill for spell etc..
token_end  = "|}"

faction_end = "[[Category: Faction]]"
