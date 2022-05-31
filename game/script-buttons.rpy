#contains the code for quickmenu buttons
label button_input:
    $ player_input = renpy.input("Hey! What's going on?")
    $ player_input.lower() # To all lowercase 
    call input_response
    return

label button_games:
    if affection_eliana == "sinner":
        e "I do not want to play a game with you, you dirty sinner."
    elif affection_eliana == "angry":
        e "I don't want to play with you."
    elif affection_eliana == "low":
        e "Oh... You want to play a game?"
    elif affection_eliana == "normal":
        menu:
            e "What game do you want to play?"
            "Nevermind.":
                e "Oh, okay!"
    elif affection_eliana == "high" or affection_eliana == "love" or affection_eliana == "enamored":
        menu: 
            e "Yay, ehehe~! What game do you want to play together?"
            "Nevermind.":
                e "Aww, that's okay."
                e "Let's play something soon!"
    jump loops

label button_quit:
    call farewell_entry
    $ renpy.save_persistent()
    $ renpy.quit()

label button_sacrifices:
    $ player_input = renpy.input("What do you want to sacrifice?")
    $ player_input.lower()
    call sacrifice_response
    jump loops
