#gift system

#where it calls a reaction/registers the sacrifice
label sacrifice_response:
    if player_input in gifts_goat:
        if not renpy.seen_label("sacrifice_goat_unseen"):
            call sacrifice_goat_unseen
        elif renpy.seen_label("sacrifice_goat_unseen"):
            call sacrifice_goat
    else:
        call cannot_sacrifice
    return

#reactions
label cannot_sacrifice:
    "You can't sacrifice this."
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
