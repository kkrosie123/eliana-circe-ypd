#contains start greetings
#opening the game
label start:
    jump loops

#angry and sinner affection greetings (upset)
label greeting_upset_itsyou:
    e "Oh... It's you."
    e "I didn't think you'd be back."
    e "Whatever, you're here now."
    return

#normal and low affection greetings (normal)
label greeting_normal_quips:
    return

#high and love affection greetings (happy)
label greeting_happy_itsyou:
    e "Well would you look at that, it's you~"
    return

#enamored affection greetings (adoration)
#greetings should include those from the previous tier, these are just unlocked at high affection
label greeting_adoration_song_meet_again:
    e "~We'll meet again~"
    e "~Don't know where~"
    e "~Don't know when~"
    e "~Oh, I know we'll meet again some sunny day~"
    e "Ehehe~ Hello there, Darling~"
    return
    
label greeting_adoration_song_sunshine:
    e "~You are my sunshine~"
    e "~My only sunshine~"
    e "~You make me happy~"
    e "~When skies are gray~"
    e "~You'll never know, Dear~"
    e "~How much I love you~"
    e "~Please don't take my sunshine away~"
    e "..."
    e "Where is my sunshine?"
    e "There's my sunshine, ehehe~!"
    e "Hello again, my love."
    return

#the actual intro for the game
label introduction:
    "..."
    "It's a normal day."
    "..."
    "Another day of hating myself."
    "My room is a disaster, but I'm too exhausted to clean it up."
    "It's been like this for weeks."
    "..."
    "Should I even get out of bed today?"
    "..."
    "..."
    "No."
    "There's no point."
    "..."
    "..."
    "Wait, what's happening?"
    "!!!"
    e "AHAHAHAHAHA~!"
    e "YOUR DEMISE IS NOW, DIRTY SINNER!!!"
    e "I AM ELIANA CIRCE, I HAVE COME FROM THE DEPTHS TO TORMENT YOU!"
    e "QUIVER AT MY WRATH! FOR I-"
    e "Oh satan! What's all this?"
    e "Oh my, oh my..."
    e "I was sent here to torment you, but now I feel guilty..."
    e "It's like you torment yourself!"
    e "Oh gosh..."
    e "..."
    e "Um... I came to torment you for being a thirsty sinner."
    e "Like, to the EXTREME! Do you know how thirsty you are?"
    menu:
        "Thirsty for you.":
            e "!!!"
            e "Well, see? Now you're just proving my point!"
        "Definitely not thirsty for you.":
            e "Okay, rude!"
    e "Listen here, I'm gonna help you with... all of this, okay?"
    return
    
