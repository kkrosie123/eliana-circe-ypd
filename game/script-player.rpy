#defines things like gender/pronouns, when needed
label pronouns_he:
    $ he = "he"
    $ him = "him"
    $ his = "his"
    $ boy = "boy"
    $ guy = "guy"
    $ man = "man"
    return

label pronouns_she:
    $ he = "she"
    $ him = "her"
    $ his = "hers"
    $ boy = "girl"
    $ guy = "gal"
    $ man = "woman"
    return

label pronouns_they:
    $ he = "they"
    $ he_is = "they are"
    $ him = "them"
    $ his = "theirs"
    $ boy = "person"
    $ guy = "person"
    $ man = "person"
    return

label pronouns_custom:
    $ he = renpy.input("Enter a pronoun like he, she, they...")
    $ he_is = renpy.input("Enter a pronoun like he is, she is, they are...")
    $ him = renpy.input("Enter a pronoun like him, her, them...")
    $ his = renpy.input("Enter a pronoun like his, hers, theirs...")
    $ boy = renpy.input("Enter a pronoun like boy, girl, person...")
    $ guy = renpy.input("Enter a pronoun like guy, gal, person...")
    $ man = renpy.input("Enter a pronoun like man, woman, person...")
    e "Okay, got it!"
    e "Your pronouns are [he], [he_is], [him], [his], [boy], [guy], [man]."
    e "Is that right?"
    menu:
        "Yes.":
            e "Great!"
        "No.":
            e "Oh, okay, would you tell me again?"
            call pronouns_custom
    return
