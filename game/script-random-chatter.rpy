#random topics brought up at the end of each loop
init python:
    import random
    random_chatter_list = [
        _("random_chatter_gender"),
        _("random_chatter_rare_entry"),
        _("random_chatter_sacrifices"),
        _("random_chatter_seven_sins")
    ]
    random_chatter = random.choice(random_chatter_list)
    rare_chatter_list = [
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
    show eliana nuetral_02
    e "I've definitely learned a lot more about genders since we last talked about them."
    show eliana nuetral_00
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
    show high_aff_idle_blink_02
    e "There is some good here."
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "Like you..."
    return


label random_chatter_seven_sins:
    e "Hmm..."
    e "Say, have you heard of the Seven Deadly Sins?"
    e "They are as follows..."
    e "Pride, greed, gluttony, sloth, wrath, envy..."
    e "Do you know the last one?"
    e "..."
    e "Lust, of course!"
    e "And my my, you are OVERFLOWING with lust!"
    e "That's why I came here in the first place, you are SUCH a thirsty sinner!"
    e "Ehehe."
    e "I hope you're not committing the other sins I mentioned, [player]."
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "Not like I would mind~"
    return 

#rare chatter
label rare_chatter_pixel_thirst:
    e "You really are a sinner."
    e "Thirsting after me when I'm nothing but pixels."
    e "...Ehehe."
    return

label rare_chatter_dating_games:
    e "Why do people play dating games?"
    e "Shouldn't they just go out and, I don't know, get a real girlfriend?"
    e "Ehehe."
    return
