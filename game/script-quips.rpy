#contains eliana's quips
#defines the quips and randomly generates on on startup
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
    #you're welcome
    youre_welcome_quips = [
        _("Ehehe, no problem!"),
        _("Oh! You're welcome!")
    ]
    youre_welcome_quip = random.choice(youre_welcome_quips)

#okay so these are the labels that you can call when you need a quip
#that way you don't have to use a function every time
#coin flip
label quip_flip_coin:
    $ flip_coin_quip = random.choice(flip_coin_quips)
    e "It landed on [flip_coin_quip]!"
    return

#greeting
label quip_greeting:
    $ greeting_quip = random.choice(greeting_quips)
    e "[greeting_quip]"
    return

#greeting follow up
label quip_greeting_follow_up:
    $ greeting_follow_up_quip = random.choice(greeting_follow_up_quips)
    e "[greeting_follow_up_quip]"
    return

#greeting but it's the whole thing
label quip_greeting_full:
    call quip_greeting
    call quip_greeting_follow_up
    return

#how are you
label quip_howareyou:
    $ howareyou_quip = random.choice(howareyou_quips)
    e "[howareyou_quip]"
    return

#i love u
label quip_love:
    $ love_quip = random.choice(love_quips)
    e "[love_quip]"
    return

#no response part 1
label quip_no_response:
    $ no_response_quip = random.choice(no_response_quips)
    e "[no_response_quip]"
    return

#quip no response apology
label quip_no_response_apology:
    $ no_response_apology_quip = random.choice(no_response_apology_quips)
    e "[no_response_apology_quip]"
    return

#she fully has no response lol
label quip_no_response_full:
    call quip_no_response
    call quip_no_response_full
    return

#thank u
label quip_thanks:
    $ thanks_quip = random.choice(thanks_quips)
    e "[thanks_quip]"
    return

#thank you but only kind of 
label quip_thanks_reluctant:
    $ thanks_reluctant_quip = random.choice(thanks_reluctant_quips)
    e "[thanks_reluctant_quip]"

#what can I say except ur welcome
label quip_youre_welcome:
    $ youre_welcome_quip = random.choice(youre_welcome_quips)
    e "[youre_welcome_quip]"
    return
