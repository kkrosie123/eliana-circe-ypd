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
label greeting_adoration_song_we'll_meet_again:
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
