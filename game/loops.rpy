#keeps player from exiting to main menu
#calls the needed affection loop
label loops:
    $ renpy.save_persistent()
    if affection_eliana == "sinner":
        jump loop_idle_sinner
    elif affection_eliana == "angry":
        jump loop_idle_angry
    elif affection_eliana == "low":
        jump loop_idle_low_aff
    elif affection_eliana == "normal":
        jump loop_idle
    elif affection_eliana == "high":
        jump loop_idle_high_aff
    elif affection_eliana == "love":
        jump loop_idle_love
    elif affection_eliana == "enamored":
        jump loop_idle_enamored

#sinner 
label loop_idle_sinner:
    call animation_idle_sinner
    call animation_idle_sinner
    call animation_idle_sinner
    $ random_chatter = random.choice(random_chatter_list)
    call expression random_chatter
    jump loops

label animation_idle_sinner:
    call sinner_pose_00
    call sinner_pose_00
    call sinner_pose_00
    call sinner_pose_01
    call sinner_pose_01
    call sinner_pose_01
    call sinner_pose_02
    call sinner_pose_02
    call sinner_pose_02
    call sinner_pose_03
    call sinner_pose_03
    call sinner_pose_03
    call sinner_pose_04
    call sinner_pose_04
    call sinner_pose_04
    return

#angry
label loop_idle_angry:
    call animation_idle_angry
    call animation_idle_angry
    call animation_idle_angry
    $ random_chatter = random.choice(random_chatter_list)
    call expression random_chatter
    jump loops

label animation_idle_angry:
    call angry_aff_pose_00
    call angry_aff_pose_00
    call angry_aff_pose_00
    call angry_aff_pose_01
    call angry_aff_pose_01
    call angry_aff_pose_01
    call angry_aff_pose_02
    call angry_aff_pose_02
    call angry_aff_pose_02
    call angry_aff_pose_03
    call angry_aff_pose_03
    call angry_aff_pose_03
    call angry_aff_pose_04
    call angry_aff_pose_04
    call angry_aff_pose_04
    return

#low aff
label loop_idle_low_aff:
    call animation_idle_low_aff
    call animation_idle_low_aff
    call animation_idle_low_aff
    $ random_chatter = random.choice(random_chatter_list)
    call expression random_chatter
    jump loops

label animation_idle_low_aff:
    call low_aff_pose_00
    call low_aff_pose_00
    call low_aff_pose_00
    call low_aff_pose_01
    call low_aff_pose_01
    call low_aff_pose_01
    call low_aff_pose_02
    call low_aff_pose_02
    call low_aff_pose_02
    call low_aff_pose_03
    call low_aff_pose_03
    call low_aff_pose_03
    call low_aff_pose_04
    call low_aff_pose_04
    call low_aff_pose_04
    return

#normal aff
label loop_idle:
    call animation_idle
    call animation_idle
    call animation_idle
    $ random_chatter = random.choice(random_chatter_list)
    call expression random_chatter
    jump loops

label animation_idle:
    call normal_aff_pose_00
    call normal_aff_pose_00
    call normal_aff_pose_00
    call normal_aff_pose_01
    call normal_aff_pose_01
    call normal_aff_pose_01
    call normal_aff_pose_02
    call normal_aff_pose_02
    call normal_aff_pose_02
    call normal_aff_pose_03
    call normal_aff_pose_03
    call normal_aff_pose_03
    call normal_aff_pose_04
    call normal_aff_pose_04
    call normal_aff_pose_04
    return

#high aff
label loop_idle_high_aff:
    call animation_idle_high_aff
    call animation_idle_high_aff
    call animation_idle_high_aff
    $ random_chatter = random.choice(random_chatter_list)
    call expression random_chatter
    jump loops

label animation_idle_high_aff:
    call high_aff_pose_00
    call high_aff_pose_00
    call high_aff_pose_00
    call high_aff_pose_01
    call high_aff_pose_01
    call high_aff_pose_01
    call high_aff_pose_02
    call high_aff_pose_02
    call high_aff_pose_02
    call high_aff_pose_03
    call high_aff_pose_03
    call high_aff_pose_03
    call high_aff_pose_04
    call high_aff_pose_04
    call high_aff_pose_04
    return
    
#love
label loop_idle_love:
    jump loops

#enamored
label loop_idle_enamored:
    jump loops

#the animations themselves:
#sinner animations
label sinner_pose_00:
    show eliana sinner_idle_00
    $ renpy.pause(5)
    show eliana sinner_idle_blink_00
    $ renpy.pause(0.15)
    return

label sinner_pose_01:
    show eliana sinner_idle_01
    $ renpy.pause(5)
    show eliana sinner_idle_blink_01
    $ renpy.pause(0.15)
    return

label sinner_pose_02:
    show eliana sinner_idle_02
    $ renpy.pause(5)
    show eliana sinner_idle_blink_02
    $ renpy.pause(0.15)
    return

label sinner_pose_03:
    show eliana sinner_idle_03
    $ renpy.pause(5)
    show eliana sinner_idle_blink_03
    $ renpy.pause(0.15)
    return

label sinner_pose_04:
    show eliana sinner_idle_04
    $ renpy.pause(5)
    show eliana sinner_idle_blink_04
    $ renpy.pause(0.15)
    return

#angry animations
label angry_aff_pose_00:
    show eliana angry_idle_00
    $ renpy.pause(5)
    show eliana angry_idle_blink_00
    $ renpy.pause(0.15)
    return

label angry_aff_pose_01:
    show eliana angry_idle_01
    $ renpy.pause(5)
    show eliana angry_idle_blink_01
    $ renpy.pause(0.15)
    return

label angry_aff_pose_02:
    show eliana angry_idle_02
    $ renpy.pause(5)
    show eliana angry_idle_blink_02
    $ renpy.pause(0.15)
    return

label angry_aff_pose_03:
    show eliana angry_idle_03
    $ renpy.pause(5)
    show eliana angry_idle_blink_03
    $ renpy.pause(0.15)
    return

label angry_aff_pose_04:
    show eliana angry_idle_04
    $ renpy.pause(5)
    show eliana angry_idle_blink_04
    $ renpy.pause(0.15)
    return

#low aff animations
label low_aff_pose_00:
    show eliana low_aff_idle_00
    $ renpy.pause(5)
    show eliana low_aff_idle_blink_00
    $ renpy.pause(0.15)
    return

label low_aff_pose_01:
    show eliana low_aff_idle_01
    $ renpy.pause(5)
    show eliana low_aff_idle_blink_01
    $ renpy.pause(0.15)
    return

label low_aff_pose_02:
    show eliana low_aff_idle_02
    $ renpy.pause(5)
    show eliana low_aff_idle_blink_02
    $ renpy.pause(0.15)
    return

label low_aff_pose_03:
    show eliana low_aff_idle_03
    $ renpy.pause(5)
    show eliana low_aff_idle_blink_03
    $ renpy.pause(0.15)
    return

label low_aff_pose_04:
    show eliana low_aff_idle_04
    $ renpy.pause(5)
    show eliana low_aff_idle_blink_04
    $ renpy.pause(0.15)
    return

#normal aff animations
label normal_aff_pose_00:
    show eliana idle_00
    $ renpy.pause(5)
    show eliana  idle_blink_00
    $ renpy.pause(0.15)
    return

label normal_aff_pose_01:
    show eliana idle_01
    $ renpy.pause(5)
    show eliana idle_blink_01
    $ renpy.pause(0.15)
    return

label normal_aff_pose_02:
    show eliana idle_02
    $ renpy.pause(5)
    show eliana idle_blink_02
    $ renpy.pause(0.15)
    return

label normal_aff_pose_03:
    show eliana idle_03
    $ renpy.pause(5)
    show eliana idle_blink_03
    $ renpy.pause(0.15)
    return

label normal_aff_pose_04:
    show eliana idle_04
    $ renpy.pause(5)
    show eliana idle_blink_04
    $ renpy.pause(0.15)
    return

#high aff animations
label high_aff_pose_00:
    show eliana high_aff_idle_00
    $ renpy.pause(5)
    show eliana high_aff_idle_blink_00
    $ renpy.pause(0.15)
    return

label high_aff_pose_01:
    show eliana high_aff_idle_01
    $ renpy.pause(5)
    show eliana high_aff_idle_blink_01
    $ renpy.pause(0.15)
    return

label high_aff_pose_02:
    show eliana high_aff_idle_02
    $ renpy.pause(5)
    show eliana high_aff_idle_blink_02
    $ renpy.pause(0.15)
    return

label high_aff_pose_03:
    show eliana high_aff_idle_03
    $ renpy.pause(5)
    show eliana high_aff_idle_blink_03
    $ renpy.pause(0.15)
    return

label high_aff_pose_04:
    show eliana high_aff_idle_04
    $ renpy.pause(5)
    show eliana high_aff_idle_blink_04
    $ renpy.pause(0.15)
    return
