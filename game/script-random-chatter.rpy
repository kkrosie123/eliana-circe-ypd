#random topics brought up at the end of each loop
init python:
    import random
    random_chatter_list = [
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
label random_chatter_sacrifices:
    e "Hey, [player]?"
    e "Have you ever heard of demonic sacrifices?"
    e "Why do people do that garbage???"
    e "The last thing we need is another dead goat!"
    e "What am I supposed to do with all of these animals??"
    e "Like, we don't eat them or anything..."
    e "Just another soul we have to deal with."
    e "Hell is only so big, you know?"
    e "Please, PLEASE don't send me anything like that."
    e "If you're gonna sacrifice anything, how about something I can actually, I dunno, use?"
    e "Like a soft plushie..."
    e "..."
    e "We don't get many nice things in hell."
    e "All of the sinners."
    e "You know, pieces of crap type people."
    e "I'm lucky enough that I get to come to Earth."
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
