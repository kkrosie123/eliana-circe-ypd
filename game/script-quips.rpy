#contains eliana's quips
init python:
    import random
    #coin flip
    flip_coin_quips = [
        _("heads"),
        _("tails")
    ]
    flip_coin_quip = random.choice(flip_coin_quips)
    #hello
    greeting_quips = [
        _("Hello!"),
        _("Hellooooooo!"),
        _("Hello there!"),
        _("Hey!"),
        _("Heyyyy!"),
        _("Hey hi hello!"),
        _("Hey there!"),
        _("Hi!"),
        _("Hiiiii!"),
        _("Hi there!")
    ]
    greeting_quip = random.choice(greeting_quips)
    greeting_follow_up_quips = [
        _("How are things?"),
        _("How are you?"),
        _("How are you today?"),
        _("Nice to see you again!"),
        _("What should we do today?")
    ]
    greeting_follow_up_quip = random.choice(greeting_follow_up_quips)
    #how are you response
    howareyou_quips = [
        _("I'm doing alright!"),
        _("I'm doing good!"),
        _("I'm doing great!"),
        _("I'm doing okay!"),
        _("I'm doing well!")
    ]
    howareyou_quip = random.choice(howareyou_quips)
    #love
    love_quips = [
        _("I love and adore you!"),
        _("I love you more!"),
        _("I love you most!"),
        _("I love you too!"),
        _("I looooove you, [player]!"),
        _("I love you soooo much!"),
        _("You're so amazing! I love you!")
    ]
    love_quip = random.choice(love_quips)
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
        _("Oh... Uh, thanks?"),
        _("Uh... Thanks, I guess.")
    ]
    thanks_reluctant_quip = random.choice(thanks_reluctant_quips)
