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
    elif player_input in list_pronouns:
        call random_chatter_gender
    elif player_input in list_thanks:
        call response_thanks
    else:
        call no_response
    jump loops

#labels start here
label no_response:
    show eliana idle_04
    e "[no_response_quip]"
    e "[no_response_apology_quip]"
    return

label response_compliments_beautiful:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        show eliana joyful_07
        e "Aww, thank you!"
        e "That's so sweet of you!"
        e "I think you're very beautiful, too."
        e "Ehehe!"
    else:
        show idle_03
        e "[thanks_reluctant_quip]"
    $ affection_value += 1
    return

label response_compliments_caring:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        show eliana joyful_07
        e "Ehehe, thanks!"
        e "I'm glad you think so."
        e "You make me feel very loved and cared for~"
    else:
        show idle_03
        e "[thanks_reluctant_quip]"
    $ affection_value += 1
    return

label response_compliments_kind:
    if affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        show eliana high_aff_idle_blink_01
        e "Aww, thank you!"
        show eliana high_aff_idle_01
        e "You're so sweet."
        show eliana idle_00
        e "But you do know I'm a demonic creature, right?"
        e "I'm not meant to be kind to anyone."
        show idle_blink_01
        e "But perhaps I want you all to myself!"
    else:
        e "[thanks_reluctant_quip]"
    $ affection_value += 1
    return

label response_emotes_bad:
    show eliana high_aff_idle_blink_01
    e "What's wrong?"
    return

label response_emotes_good:
    show eliana high_aff_idle_02
    e "Ehehe, what are you smiling for?"
    return

label response_flip_coin:
    show eliana idle_blink_01
    e "Alright, I'll flip a coin for you."
    show eliana joyful_00
    e "It landed on [flip_coin_quip]!"
    return

label response_greetings:
    show eliana idle_blink_02
    $ greeting_quip = random.choice(greeting_quips)
    e "[greeting_quip]"
    show eliana idle_blink_01
    $ greeting_follow_up_quip = random.choice(greeting_follow_up_quips)
    e "[greeting_follow_up_quip]"
    return

label response_howareyou:
    show eliana joyful_00
    $ howareyou_quip = random.choice(howareyou_quips)
    e "[howareyou_quip]"
    show eliana idle_blink_04
    $ greeting_follow_up_quip = random.choice(greeting_follow_up_quips)
    e "[greeting_follow_up_quip]"
    return

label response_hugs:
    if affection_eliana == "sinner":
        show eliana sinner_idle_blink_02
        e "Don't you dare touch me, you dirty sinner."
    elif affection_eliana == "angry":
        show eliana angry_idle_blink_03
        e "Sorry. I don't want to hug right now."
    elif affection_eliana == "low":
        show eliana low_aff_idle_04
        e "Oh... You want a hug...? I guess I can give you one..."
    elif affection_eliana == "normal":
        show eliana neutral_00
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
        show eliana angry_03
        e "Rude. But you're rude all the time anyways."
    else:
        show eliana embarrassed_02
        e "Hey! That's not nice!"
        show eliana embarrassed_01
        e "Why would you say that to me?"
        show eliana angry_idle_blink_04
        e "Grr-"
        e "..."
    $ affection_value -= 5
    return

label response_insults_very_bad:
    if affection_eliana == "sinner" or affection_eliana == "angry":
        show eliana angry_02
        e "Ugh. Disgusting. Just what I would expect from you."
    else:
        show embarrassed_03
        e "Why would you say that to me?!"
        show embarrassed_01
        e "I..."
        e "Why...?"
        show eliana low_aff_idle_00
        e "That's awful."
        e "..."
        show eliana low_aff_idle_blink_00
        e "I can't believe you..."
    $ affection_value -= 20
    return

label response_love:
    if affection_eliana == "love" or affection_eliana == "enamored":
        show eliana high_aff_idle_01
        e "[love_quip]"
    else: 
        show eliana embarrassed_00
        e "Um..."
        show eliana embarrassed_01
        e "It's a bit too early for that..."
    return

label response_name:
    show eliana high_aff_idle_02
    if renpy.seen_label("response_name"):
        e "Oh? You want to change your name?"
    $ player = renpy.input("What should I call you?")
    $ player = player.strip()
    $ player = player.capitalize()
    if player == "":
        $ player = "Sinner"
        show eliana laugh_04
        e "Um... You didn't say anything."
    show eliana idle_blink_03
    e "Okay, I'll call you [player] from now on."
    return

label response_thanks:
    show eliana high_aff_idle_03
    e "[youre_welcome_quip]"
    return
