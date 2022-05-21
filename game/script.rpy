#contains definitions and technical stuff
#set affection
init python: 
    affection_value = -50
    if affection_value < -100 and affection_value > -500:
        affection_eliana = "sinner"
    elif affection_value < -100 and affection_value > -500:
        affection_eliana = "angry"
    elif affection_value < 0 and affection_value > -100:
        affection_eliana = "low"
    elif affection_value < 500 and affection_value > 0:
        affection_eliana = "normal"
    elif affection_value > 500 and affection_value < 700:
        affection_eliana = "high"
    elif affection_value > 700 and affection_value < 1000:
        affection_eliana = "love"
    elif affection_value > 1000:
        affection_eliana = "enamored"

#registers Eliana as a character
define e = Character("Eliana", color="#c55e5e")
define s = Character("Satan", color="#500000")

#default persistent values
default player = "Sinner"
