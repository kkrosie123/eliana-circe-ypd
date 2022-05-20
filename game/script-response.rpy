#this is where eliana calls a response to the player
label input_response:
    if player_input in list_compliments_beautiful:
        call response_compliments_beautiful
    elif player_input in list_compliments_caring:
        call response_compliments_caring
    elif player_input in list_compliments_kind:
        call response_compliments_kind
    elif player_input in list_emotes_bad:
        call response_emotes_bad
    elif player_input in list_emotes_good:
        call response_emotes_good
    elif player_input in list_flip_coin:
        call response_flip_coin
    elif player_input in list_greetings:
        call response_greetings
    elif player_input in list_howareyou:
        call response_howareyou
    elif player_input in list_hugs:
        call response_hugs
    elif player_input in list_insults_bad:
        call response_insults_bad
    elif player_input in list_insults_very_bad:
        call response_insults_very_bad
    elif player_input in list_love:
        call response_love
    elif player_input in list_name:
        call response_name
    elif player_input in list_thanks:
        call response_thanks
    else:
        call no_response
    jump loops

#labels start here
label no_response:
    e "[no_response_quip]"
    e "[no_response_apology_quip]"
    return

label response_compliments_beautiful:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        e "Aww, thank you!"
        e "That's so sweet of you!"
        e "I think you're very beautiful, too."
        e "Ehehe!"
    else:
        e "[thanks_reluctant_quip]"
    $ affection_eliana += 1
    return

label response_compliments_caring:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        e "Ehehe, thanks!"
        e "I'm glad you think so."
        e "You make me feel very loved and cared for~"
    else:
        e "[thanks_reluctant_quip]"
    $ affection_eliana += 1
    return

label response_compliments_kind:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        e "Aww, thank you!"
        e "You're so sweet."
        e "But you do know I'm a demonic creature, right?"
        e "I'm not meant to be kind to anyone."
        e "But perhaps I want you all to myself!"
    else:
        e "[thanks_reluctant_quip]"
    $ affection_eliana += 1
    return

label response_emotes_bad:
    e "What's wrong?"
    return

label response_emotes_good:
    e "Ehehe, what are you smiling for?"
    return

label response_flip_coin:
    e "Alright, I'll flip a coin for you."
    e "It landed on [flip_coin_quip]!"
    return

label response_greetings:
    e "[greeting_quip]"
    e "[greeting_follow_up_quip]"
    return

label response_howareyou:
    e "[howareyou_quip]"
    e "[greeting_follow_up_quip]"
    return

label response_hugs:
    if affection_eliana == "sinner":
        e "Don't you dare touch me, you dirty sinner."
    elif affection_eliana == "angry":
        e "Sorry. I don't want to hug right now."
    elif affection_eliana == "low":
        e "Oh... You want a hug...? I guess I can give you one..."
    elif affection_eliana == "normal":
        e "Oooh! Hugs? Sure!"
    elif affection_eliana == "high":
        e "Yayy, hugs~ Ehehe~"
    elif affection_eliana == "love":
        e "Aww! I love your hugs!"
    elif affection_eliana == "enamored":
        e "Your hugs are seriously the best. Thank you!"
    return

label response_insults_bad:
    if affection_eliana == "sinner" or affection_eliana == "angry":
        e "Rude. But you're rude all the time anyways."
    else:
        e "Hey! That's not nice!"
        e "Why would you say that to me?"
        e "Grr-"
        e "..."
    $ affection_value -= 5
    return

label response_insults_very_bad:
    if affection_eliana == "sinner" or affection_eliana == "angry":
        e "Ugh. Disgusting. Just what I would expect from you."
    else:
        e "Why would you say that to me?!"
        e "I..."
        e "Why...?"
        e "That's awful."
        e "..."
        e "I can't believe you..."
    $ affection_value -= 20
    return

label response_love:
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "[love_quip]"
    return

label response_name:
    if renpy.seen_label("response_name"):
        e "Oh? You want to change your name?"
    $ player = renpy.input("What should I call you?")
    $ player = player.strip()
    $ player = player.capitalize()
    if player == "":
        $ player = "Sinner"
        e "Um... You didn't say anything."
    e "Okay, I'll call you [player] from now on."

label response_thanks:
    return
