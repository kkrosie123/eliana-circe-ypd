#random topics brought up at the end of each loop
init python:
    import random
    random_chatter_list = [
        _("random_chatter_rare_entry"),
        _("random_chatter_seven_sins")
    ]
    random_chatter = random.choice(random_chatter_list)
    rare_chatter_list = [
        _("rare_chatter_pixel_thirst")
    ]
    rare_chatter = random.choice(rare_chatter_list)

label random_chatter_rare_entry:
    $ rare_chatter_chance = renpy.random.randint(1,15)
    if rare_chatter_chance == 1:
        call expression rare_chatter
    else:
        call expression random_chatter
    return

#random chatter
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
