#gift system

#where it calls a reaction/registers the sacrifice
label sacrifice_response:
    if player_input in gifts_bible:
        call sacrifice_bible
    elif player_input in gifts_cross:
        call sacrifice_cross
    elif player_input in gifts_evil_eye:
        call sacrifice_evil_eye
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
    show eliana angry_idle_03
    e "..."
    e "Um..."
    e "A... A bible?"
    e "Um... You want me to read about the tyrant that downcasted my father to hell?"
    show eliana angry_idle_blink_03
    e "No thanks. I've heard it all before."
    show eliana angry_idle_03
    e "Please don't give me this garbage. I like books, but this is just garbage."
    $ affection_value -= 10
    return

label sacrifice_cross:
    show eliana angry_idle_03
    e "..."
    e "Really? A cross?"
    e "Are you trying to expel me from your home, [sinner]?"
    show eliana angry_idle_00
    e "Good luck. I'm not going anywhere."
    $ affection_value -= 10
    return

label sacrifice_evil_eye:
    show eliana angry_idle_01
    e "Are you... trying to curse me?"
    show eliana angry_02
    e "Hah. Good luck, [sinner]."
    show eliana angry_00
    e "Still, that's rude."
    $ affection_value -= 5
    return

label sacrifice_goat:
    show eliana angry_idle_02
    e "ARE YOU KIDDING ME?"
    e "STOP IT!"
    $ affection_value -= 20
    return

label sacrifice_goat_unseen:
    show eliana angry_02
    e "Are you serious right now??"
    e "A dead goat?"
    e "..."
    e "Just another soul to deal with..."
    $ affection_value -= 20
    return

label sacrifice_holy_water:
    show eliana terrified_03
    e "EEEEEEEEEEEEEEK!!!"
    e "NO, NO!!!"
    show eliana terrified_04
    e "WHY WOULD YOU-"
    show eliana terrified_03
    e "GET THAT AWAY FROM ME!!!"
    e "AGH- EEK-"
    show eliana terrified_01
    e "!!!"
    e "...!"
    e "..."
    show eliana terrified_02
    e "..."
    show eliana terrified_00
    e "D-Don't... don't do that..."
    e "Don't do that to me..."
    $ affection_value -= 50
    return

label sacrifice_plush:
    show eliana high_aff_idle_00
    e "Ohhh my satan!"
    show eliana high_aff_idle_01
    e "It's so cute!"
    show eliana high_aff_idle_blink_00
    e "Thank you, [player]!"
    e "I love it!"
    $ affection_value += 10
    return
