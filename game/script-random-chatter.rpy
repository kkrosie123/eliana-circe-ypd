#random topics brought up at the end of each loop
init python:
    import random
    random_chatter_list = [
        _("random_chatter_gender"),
        _("random_chatter_rare_entry"),
        _("random_chatter_sacrifices"),
        _("random_chatter_seasons"),
        _("random_chatter_seven_sins")
    ]
    random_chatter = random.choice(random_chatter_list)
    rare_chatter_list = [
        _("rare_chatter_dating_games"),
        _("rare_chatter_pixel_thirst")
    ]
    rare_chatter = random.choice(rare_chatter_list)

label random_chatter_rare_entry:
    $ rare_chatter = random.choice(rare_chatter_list)
    $ rare_chatter_chance = renpy.random.randint(1,15)
    if rare_chatter_chance == 1:
        call expression rare_chatter
    else:
        call expression random_chatter
    return

#random chatter
label random_chatter_gender:
    if not renpy.seen_label("random_chatter_gender_unseen"):
        call random_chatter_gender_unseen
    else:
        call random_chatter_gender_seen
    return

label random_chatter_gender_seen:
    show eliana neutral_02
    e "I've definitely learned a lot more about genders since we last talked about them."
    show eliana neutral_00
    e "Did you know that they can change?"
    show eliana joyful_07
    e "They're like self-expression! That's so cool to me!"
    show eliana idle_04
    e "Say, has your gender changed since we last talked about it?"
    menu:
        "Yes.":
            show eliana idle_blink_00
            e "Oh, okay! In that case, what are your pronouns?"
            menu:
                "He/Him.":
                    call pronouns_he
                "She/Her.":
                    call pronouns_she
                "They/Them.":
                    call pronouns_they
                "Something else.":
                    e "Is that so?"
                    e "Would you tell me your pronouns?"
                    call pronouns_custom
        "No.":
            show eliana idle_blink_00
            e "Oh, okay!"
    show eliana idle_04
    e "If you ever want to change what pronouns I call you, just tell me!"
    return

label random_chatter_gender_unseen:
    show eliana idle_03
    e "You know, in hell, humans lose all of their distinguishing features."
    e "As a result, I'm pretty new to the whole gender thing..."
    show eliana idle_02
    e "I understand it's a complicated topic, but I want to refer to you properly."
    e "So, [player]... What are your pronouns?"
    menu:
        "He/Him.":
            call pronouns_he
            e "Alright!"
        "She/Her.":
            call pronouns_she
            e "Alright!"
        "They/Them.":
            call pronouns_they
            e "Alright!"
        "Something else.":
            e "Is that so?"
            show eliana idle_blink_00
            e "Huh, this gender thing seems to have a lot more to it than I thought!"
            e "Would you tell me your pronouns?"
            call pronouns_custom
    e "If you ever want to change what pronouns I call you, just tell me!"
    return

label random_chatter_have_you_eaten:
    e "Hey, [player]?"
    menu:
        e "Have you eaten today?"
        "Yes.":
            e "Good!"
        "No.":
            e "!!!"
            e "Are you serious?"
            e "I don't want to have to see you in hell any sooner than I need to!"
        e "It's really important that you take care of yourself."
        e "Even demons have to eat to survive."
        e "Albeit, it's different from the way you humans eat."
        e "But I know how important it is, including for you!"
        e "Take care of yourself!"
        menu:
            e "Got it?"
            "Got it.":
                e "Ehehe!"
        e "Good. I knew I could count on you."
    return

label random_chatter_sacrifices:
    show eliana angry_idle_blink_04
    e "Hey, [player]?"
    show eliana angry_idle_04
    e "Have you ever heard of demonic sacrifices?"
    show eliana embarrassed_01
    e "Why do people do that garbage???"
    show eliana angry_00
    e "The last thing we need is another dead goat!"
    show eliana angry_idle_00
    e "What am I supposed to do with all of these animals??"
    e "Like, we don't eat them or anything..."
    show eliana angry_idle_02
    e "Just another soul we have to deal with."
    e "Hell is only so big, you know?"
    show eliana embarrassed_02
    e "Please, PLEASE don't send me anything like that."
    e "If you're gonna sacrifice anything, how about something I can actually, I dunno, use?"
    show eliana high_aff_idle_blink_01
    e "Like a soft plushie..."
    e "..."
    show eliana low_aff_idle_01
    e "We don't get many nice things in hell."
    e "All of the sinners."
    e "You know, pieces of crap type people."
    show eliana low_aff_idle_02
    e "I'm lucky enough that I get to come to Earth."
    show eliana high_aff_idle_blink_02
    e "There is some good here."
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "Like you..."
    return
    
label random_chatter_seasons:
    show eliana high_aff_idle_blink_03
    e "You know, [player]..."
    show eliana high_aff_idle_blink_02
    e "The seasons in this world are quite beautiful."
    show eliana low_aff_idle_04
    e "Sure, the different circles of hell have different climates, you could say, but things don't change much."
    show eliana idle_03
    e "The cycle of the year provides so many experiences and sensations I've never had before."
    show eliana high_aff_idle_blink_03
    e "Spring is full of rain and the scent of flowers."
    e "Summer is hot like hell, but in a different way, I guess."
    e "Nothing is on fire, nothing smells of ash or rotting flesh..."
    show eliana high_aff_idle_blink_02
    e "It's all so bright and... sunshiney?"
    e "The sun is so new to me, as well."
    e "Everything is so dark where I'm from."
    show eliana enamored_idle_blink_03
    e "In autumn, things become the perfect temperature."
    e "Literally perfect. I've never felt so comfortable."
    e "In winter, I get to bundle up..."
    show eliana enamored_idle_blink_04
    e "Oh Satan. It's all so new."
    show eliana idle_01
    e "Perhaps I'll follow you the next time you go for a walk, so I can really take it all in."
    e "Ehehe, don't worry. I'll keep out of sight of other mortals."
    return

label random_chatter_seven_sins:
    show eliana idle_00
    e "Hmm..."
    show eliana idle_03
    e "Say, have you heard of the Seven Deadly Sins?"
    show eliana idle_blink_03
    e "They are as follows..."
    show eliana idle_04
    e "Pride, greed, gluttony, sloth, wrath, envy..."
    e "Do you know the last one?"
    e "..."
    show eliana laugh_03
    e "Lust, of course!"
    e "And my my, you are OVERFLOWING with lust!"
    e "That's why I came here in the first place, you are SUCH a thirsty sinner!"
    show eliana idle_blink_04
    e "Ehehe."
    e "I hope you're not committing the other sins I mentioned, [player]."
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "Not like I would mind~"
    return 

#rare chatter
label rare_chatter_dating_games:
    show eliana neutral_00
    e "Why do people play dating games?"
    e "Shouldn't they just go out and, I don't know, get a real girlfriend?"
    e "Ehehe."
    return

label rare_chatter_pixel_thirst:
    show eliana idle_blink_00
    e "You really are a sinner."
    e "Thirsting after me when I'm nothing but pixels."
    e "...Ehehe."
    return
