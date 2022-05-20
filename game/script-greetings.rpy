#contains start greetings
#defines the list of labels to choose from per affection
init python: 
    import random
    greetings_upset = [
        _("greeting_upset_itsyou")
    ]
    greeting_upset = random.choice(greetings_upset)
    greetings_normal = [
        _("greeting_normal_quips"),
        _("greeting_normal_unexpected")
    ]
    greeting_normal = random.choice(greetings_normal)
    greetings_happy = [
        _("greeting_happy_itsyou"),
        _("greeting_happy_song_meet_again")
    ]
    greeting_happy = random.choice(greetings_happy)
    greetings_adoration = [
        _("greeting_adoration_song_sunshine"),
        _("greeting_happy_itsyou"),
        _("greeting_happy_song_meet_again"),
        _("greeting_normal_quips")
    ]
    greeting_adoration = random.choice(greetings_adoration)

#opening the game
label start:
    if not renpy.seen_label("introduction"):
        call introduction
    else:
        if affection_eliana == "sinner" or affection_eliana == "angry":
            show room_mess_03
            show filter_type red
            call expression greeting_upset
        elif affection_eliana == "low" or affection_eliana == "normal":
            show room_mess_03
            call expression greeting_normal
        elif affection_eliana == "high" or affection_eliana == "love":
            show room_mess_02
            call expression greeting_happy
        elif affection_eliana == "enamored":
            show room_mess_01
            call expression greeting_adoration
    jump loops

#angry and sinner affection greetings (upset)
label greeting_upset_itsyou:
    e "Oh... It's you."
    e "I didn't think you'd be back."
    e "Whatever, you're here now."
    return

#normal and low affection greetings (normal)
label greeting_normal_quips:
    e "[greeting_quip]"
    e "[greeting_follow_up_quip]"
    return

label greeting_normal_unexpected:
    e "..."
    e "..."
    e "!!!"
    e "Hey, sorry, I didn't expect you back so soon!"
    e "[greeting_follow_up_quip]"
    return

#high and love affection greetings (happy)
label greeting_happy_itsyou:
    e "Hmm?"
    e "Well would you look at that, it's you~"
    return

label greeting_happy_song_meet_again:
    e "~We'll meet again~"
    e "~Don't know where~"
    e "~Don't know when~"
    e "~Oh, I know we'll meet again some sunny day~"
    e "Ehehe~ Hello there, Darling~"
    return

#enamored affection greetings (adoration)
#greetings should include those from the previous tier, these are just unlocked at high affection
    
label greeting_adoration_song_sunshine:
    e "~You are my sunshine~"
    e "~My only sunshine~"
    e "~You make me happy~"
    e "~When skies are gray~"
    e "~You'll never know, Dear~"
    e "~How much I love you~"
    e "~Please don't take my sunshine away~"
    e "..."
    e "Where is my sunshine?"
    e "There's my sunshine, ehehe~!"
    e "Hello again, my love."
    return

#the actual intro for the game
label introduction:
    show room_mess_03
    "..."
    "It's a normal day."
    "..."
    "Another day of hating myself."
    "My room is a disaster, but I'm too exhausted to clean it up."
    "It's been like this for weeks."
    "..."
    "Should I even get out of bed today?"
    "..."
    "No."
    "There's no point."
    "..."
    "Wait, what's happening?"
    "!!!"
    show filter_type red
    show eliana evil_01
    e "AHAHAHAHAHA~!"
    show eliana evil_02
    e "YOUR DEMISE IS NOW, DIRTY SINNER!!!"
    show eliana evil_03
    e "I AM ELIANA CIRCE, I HAVE COME FROM THE DEPTHS TO TORMENT YOU!"
    show eliana evil_00
    e "QUIVER AT MY WRATH! FOR I-"
    hide filter_type red
    show eliana embarrassed_00
    e "Oh satan! What's all this?"
    show eliana embarrassed_01
    e "Oh my, oh my..."
    show eliana low_aff_idle_00
    e "I was sent here to torment you, but now I feel guilty..."
    show eliana embarrassed_03
    e "It's like you torment yourself!"
    show eliana embarrassed_01
    e "Oh gosh..."
    show eliana low_aff_idle_02
    e "..."
    show eliana embarrassed_02
    e "Um... I came to torment you for being a thirsty sinner."
<<<<<<< HEAD
<<<<<<< Updated upstream
    hide embarrassed_02
=======
>>>>>>> 053d8f39f3e3655ed2994b7b2ea7574a49da5fce
    show angry_02
=======
    show eliana angry_02
>>>>>>> Stashed changes
    e "Like, to the EXTREME! Do you know how thirsty you are?"
    menu:
        "Thirsty for you.":
            show eliana embarrassed_00
            e "!!!"
            show eliana embarrassed_01
            e "Well, see? Now you're just proving my point!"
        "Definitely not thirsty for you.":
            show eliana angry_03
            e "Okay, rude!"
    show eliana low_aff_idle_01
    e "Listen here, I'm gonna help you with... all of this, okay?"
    show eliana angry_idle_03
    e "Don't tell the Devil."
    return
    
