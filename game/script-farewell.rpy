#contains goodbyes
#defines lists of farewells
init python:
    import random
    farewells_upset = [
        _("farewell_upset_out_of_sight"),
        _("farewell_upset_silent")
    ]
    farewell_upset = random.choice(farewells_upset)
    farewells_normal = [
        _("farewell_normal_see_you")
    ]
    farewell_normal = random.choice(farewells_normal)
    farewells_happy = [
        _("farewell_happy_leaving_already")
    ]
    farewell_happy = random.choice(farewells_happy)
    farewells_adoration = [
        _("farewell_happy_leaving_already"),
        _("farewell_adoration_dreams")
    ]
    farewell_adoration = random.choice(farewells_adoration)

#picks a list
label farewell_entry:
    if affection_eliana == "angry" or affection_eliana == "sinner":
        call expression farewell_upset
    elif affection_eliana == "low" or affection_eliana == "normal":
        call expression farewell_normal
    elif affection_eliana == "high" or affection_eliana == "love":
        call expression farewell_happy
    elif affection_eliana == "enamored":
        call expression farewell_adoration
    return

#the farewells themself
#upset
label farewell_upset_out_of_sight:
    e "Good. Get out of my sight."
    return

label farewell_upset_silent:
    e "..."
    return

#normal
label farewell_normal_see_you:
    e "Ah, okay. I'll see you later, then?"
    e "Bye!"
    return

#happy
label farewell_happy_leaving_already:
    e "Aww, leaving already?"
    e "Well, alright. I'll see you later!"
    return

#adoration
label farewell_adoration_dreams:
    e "Goodbye, my love."
    e "I'll be dreaming about you~"
    e "Until we meet again, darling."
    return
