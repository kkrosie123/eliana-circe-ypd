#random topics brought up at the end of each loop
init python:
    import random
    random_chatter_list = [
        _("random_chatter_gender"),
        _("random_chatter_have_you_eaten"),
        _("random_chatter_rare_entry"),
        _("random_chatter_sacrifices"),
        _("random_chatter_seasons"),
        _("random_chatter_seven_sins"),
        _("random_chatter_axolotls"),
        _("random_chatter_videogames"),
        _("random_chatter_lovecraft"),
        _("random_chatter_hellweather"),
        _("random_chatter_blackcats"),
        _("random_chatter_pitties"),
        _("random_chatter_iceskating"),
        _("random_chatter_plushies"),
        _("random_chatter_sweettooth"),
        _("random_chatter_forteorigin")
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

label random_chatter_axolotls:
    e "[player]!"
    e "Have you ever heard of, or seen an axolotl?"
    e "They are the cutest mortal things I've ever seen."
    e "..."
    e "After you, of course, my darling."
    e "Hahaha!"
    e "Anyway, axolotls are a type of salamander, but they don't go under metamorphosis..."
    e "Which means they keep their gills and remain underwater for the rest of their fleeting lives."
    e "Everyone usually recognize them for their external gills that go on top of their heads."
    e "But I can't help but feel a little sad when I think they almost went through extinction..."
    e "All because of the awful human behavior of destroying any nature they touch."
    e "Ugh. Sometimes I can't even believe I fell for a human."
    e "..."
    if affection_eliana == "love" or affection_eliana == "enamored":
        e "Aw, don't look so down, my dear [player]."
        e "There is no human like you, and that's why I am head over heels for you, my mortal dork."
    else:
        e "I guess you're just worth my time~"
    return

label random_chatter_videogames:
    e "Hey [player], I noticed you seem to have quite the collection of video games!"
    e "Do you have any animal games?"
    e "You know, like Slime Simulators?"
    e "Hey! What's that look for?"
    e "Oh, you don't have slimes here on Earth…"
    e "Ahahaha, guess I have to learn a bit more about the animals here then!"
    e "Anyways, if you do have any animal games, I'd love to play them with you, my love~"
    return
    
label random_chatter_lovecraft:
    e "[player], have you heard of H.P. Lovecraft?"
    e "He was an American horror fiction writer during the early 20th century."
    e "You're probably at least somewhat familiar with his work, The Call Of Cthulhu."
    e "Cosmic horror seemed to be his specialty."
    e "Father says he wasn't all that entertaining to torment."
    e "Maybe I can read something of his to you sometime..."
    e "If you get scared of the horror bits, you can hold my hand~"
    e "My little scaredy cat~"
    return

label random_chatter_hellweather:
    e "Hey [player]... Do you like snow?"
    menu:
        "Yes":
            e "Oh, lovely!"
            jump random_chatter_hellweather2

        "No":
            e "Oh, well, I guess it's not for everyone."
            jump random_chatter_hellweather2
        return

label random_chatter_hellweather2:
    e "I adore the snow. We don't have weather in Hell..."
    e "Well, not weather like on Earth, at least."
    e "In Hell, we have hot, hotter, unbearably scorching, and lava rain."
    e "Even lava is a bit too much for low level demons like me."
    e "But here on Earth? It's so much different."
    e "Next time it snows, can we go outside? I promise I won't be seen."
    e "We can do snow angels together..."
    e "Or snow demons, in that case...?"
    e "Hahaha!"
    return

label random_chatter_blackcats:
    e "People say that black cats are a bad omen, or a sign of bad luck."
    e "But that way of thinking is really problematic."
    e "Many black cats are abused because of stupid superstitions..."
    e "Some shelters won't even take them because they believe they won't be adopted."
    e "And even when they're taken in, a lot of the time they end up getting euthanized because nobody adopts them."
    e "But they're no different from other cats!"
    e "Cats are chaos beans, plain and simple. Regardless of the color of their fur."
    e "I have a black cat back in Hell, her name is Forte."
    e "She's the sweetest creature I've ever met."
    e "If you behave well, you can replace that position someday, [player]~"
    e "I wonder if you can show yourself to be the cutest creature ever? Ehehehe~"
    e "Anyways, maybe I can introduce you two someday, [player]."
    return 

label random_chatter_pitties:
    e "Quite a lot of people have this preconceived notion that pitbulls are these vicious monsters,"
    e "But they're usually very sweet, actually."
    e "They're like any other dog, they have their own unique temperaments, and need to be trained."
    e "Pitties tend to mimic the people or animals they grow up around. If you're aggressive, they become aggressive."
    e "Many cruel people, who I've had the deepest pleasure to torment, abuse, or even kill pitties, simply due to a stupid misconception."
    e "Pitties are just dogs, and like any other dog, they just want you to love them."
    e "Next time you see a pittie, and think 'better stay away,' remember how dogs learn behavior."
    return

#TODO: add a conditional related to seeing random_chatter_hellweather
label random_chatter_iceskating:
    e "[player], remember when I mentioned snow?"
    e "Well I found out there's this thing called ice skating!"
    e "We never had anything of the sort in hell!"
    e "We should go try that sometime! I wonder if there are any rinks near you…"
    e "Sounds like a date!"
    return

label random_chatter_plushies: 
    e "[player], do you own any plushies?"
    e "I find them very adorable!" 
    e "I mean, they're soft and made into so many different creatures and animals!"
    e "You probably already guessed but, in hell we don't really have soft things." 
    e "Hm… I wonder if they would have a plushie of Forte?"
    e "I would love to get one~"
    return

label random_chatter_sweettooth:
    e "Hey [player] do you have a sweet tooth?" 
    menu:
        "Yes":
            e "Oh me too!" 
            jump random_chatter_sweettooth2
        "No":
            e "Oh, alright." 
            jump random_chatter_sweettooth3

label random_chatter_sweettooth2:
    e "I love sweets!!! They are so delicious!" 
    e "We never had anything like it in hell!" 
    e "Just thinking about all the different sweet treats has got my mouth watering!"
    e "Ooh! If you want I could teach you some recipes!" 
    return

label random_chatter_sweettooth3:
    e "I love sweets!!! They are so delicious!" 
    e "We never had anything like it in hell!" 
    e "Just thinking about all the different sweet treats has got my mouth watering!"
    e "Ooh! If you want I could teach you some recipes!" 
    e "Maybe you could bring some!"
    return

label random_chatter_forteorigin:
    e "Hey [player], I'm sure you're wondering about the cute little kitten that's been popping up lately!" 
    e "Her name is Forte and she's my little hell kitten!"
    e "Isn't she just the cutest little thing!" 
    e "Mwehehe!" 
    e "Anyway, would you like to hear how I met her?" 
    e "Awesome!" 
    e "So, Forte was actually a kitten from your world, mortal." 
    e "But, she fell through one of our many portals to Hell!" 
    e "That's how she became a hell cat or more specifically a hell kitten!"
    e "Oh, My Satan [player]! It was so cute!" 
    e "She fell right into my arms!" 
    e "It's like we are destined to be together!" 
    e "After all there's no better pair than a demon and their hell cat!" 
    e "Mwehehe! Well, I hope you don't mind her coming and going as she pleases!"
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
