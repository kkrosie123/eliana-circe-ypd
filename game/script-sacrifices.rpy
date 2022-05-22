#gift system

#where it calls a reaction/registers the sacrifice
label sacrifice_response:
    if player_input in gifts_bible:
        call sacrifice_bible
    elif player_input in gifts_goat:
        if not renpy.seen_label("sacrifice_goat_unseen"):
            call sacrifice_goat_unseen
        elif renpy.seen_label("sacrifice_goat_unseen"):
            call sacrifice_goat
    elif player_input in gifts_holy_water:
        call sacrifice_holy_water
    elif player_input in gifts_plush:
        call sacrifice_plush
    else:
        call cannot_sacrifice
    return

#reactions
label cannot_sacrifice:
    "You can't sacrifice this."
    return

label sacrifice_bible:
    e "..."
    e "Um..."
    e "A... A bible?"
    e "Um... You want me to read about the tyrant that downcasted my father to hell?"
    e "No thanks. I've heard it all before."
    e "Please don't give me this garbage. I like books, but this is just garbage."
    $ affection_value -= 10
    return

label sacrifice_goat:
    e "ARE YOU KIDDING ME?"
    e "STOP IT!"
    $ affection_value -= 20
    return

label sacrifice_goat_unseen:
    e "Are you serious right now??"
    e "A dead goat?"
    e "..."
    e "Just another soul to deal with..."
    $ affection_value -= 20
    return

label sacrifice_holy_water:
    e "EEEEEEEEEEEEEEK!!!"
    e "NO, NO!!!"
    e "WHY WOULD YOU-"
    e "GET THAT AWAY FROM ME!!!"
    e "AGH- EEK-"
    e "!!!"
    e "...!"
    e "..."
    e "..."
    e "D-Don't... don't do that..."
    e "Don't do that to me..."
    $ affection_value -= 50
    return

label sacrifice_plush:
    e "Ohhh my satan!"
    e "It's so cute!"
    e "Thank you, [player]!"
    e "I love it!"
    $ affection_value += 10
    return
