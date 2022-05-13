#contains the code for quickmenu buttons
label button_input:
    $ player_input = renpy.input.("Hey! What's going on?")
    $ input.lower() # To all lowercase 
    call input_response
    return

label button_games:
    if affection_eliana = "low":
        e "I don't want to play a game with you."
    elif affection_eliana = "normal":
        menu:
            e "What game do you want to play?"
            "Nevermind.":
                e "Oh, okay!"
    elif affection_eliana = "high":
        menu: 
            e "Yay, ehehe~! What game do you want to play together?"
            "Nevermind.":
                e "Aww, that's okay."
                e "Let's play something soon!"
    jump loops
label button_quit:
    $ renpy.save_persistent()
    $ renpy.quit()
