#contains definitions and technical stuff
#set affection
init python: 
    renpy.block_rollback()
    affection_value = 0
    affection_eliana = "normal"
    if affection_value < -100:
        affection_eliana = "low"
    elif affection_value > 100:
        affection_eliana = "high"

#registers Eliana as a character
define e = Character("Eliana", color="#c55e5e")
