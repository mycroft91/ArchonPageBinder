##parts being replaced
generic_animation_template = """==Animations==
{{Template:Animation}}
"""
min_cat                    = """{{Category:Minion}}"""
spell_cat                  = """{{Category:Spell}}"""
artifact_cat               = """{{Category:Artifact}}"""

remove_lines               = ["{{Template:Animation}}"
                            ,"==Animations=="
                            ,"{{Category:Minion}}"
                            ,"{{Category:Spell}}"
                            ,"{{Category:Artifact}}"
                            ,"{{Template:SpellAnimation}}"]

minion_animation_template  = """
==Animations==
{{Template:Animation}}

{{Category:Minion}}
"""
spell_animation_template   = """
==Animations==
{{Template:SpellAnimation}}

{{Category:Spell}}
"""
artifact_animation_template   = """
==Animations==
{{Template:SpellAnimation}}

{{Category:Artifact}}
"""
