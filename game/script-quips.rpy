#contains eliana's quips
init python:
    import random
    #no response
    no_response_quips = [
        _("Hmm, I don't have anything to say."),
        _("I don't have anything to say about that."),
        _("I don't know what to say about that."),
        _("Sorry, I don't think I have anything to say.")
    ]
    no_response_quip = random.choice(no_response_quips)
    no_response_apology_quips = [
        _("I hope you're not dissapointed."),
        _("Sorry about that.")
    ]
    no_response_apology_quip = random.choice(no_response_apology_quips)
    #thanks
    thanks_quips = [
        _("Aww, thanks!"),
        _("Oh, thank you!"),
        _("Thanks!"),
        _("Thank you!")
    ]
    thanks_quip = random.choice(thanks_quips)
    thanks_reluctant_quips = [
        _("Uh... Thanks, I guess.")
    ]
    thanks_reluctant_quip = random.choice(thanks_reluctant_quips)