#keeps player from exiting to main menu
#calls the needed affection loop
label loops:
    $ renpy.save_persistent()
    if affection_eliana == "low":
        jump loop_idle_low_aff
    if affection_eliana == "normal":
        jump loop_idle
    if affection_elianna == "high":
        jump loop_idle_high_aff

#low aff
label loop_idle_low_aff:
    call animation_idle_low_aff
    call animation_idle_low_aff
    call animation_idle_low_aff
    jump label_idle_low_aff

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
    jump loop_idle

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
    jump loop_idle_high_aff

label animation_idle_high_aff:

#the animations themself:
#low aff animations
label low_aff_pose_00:
    show low_aff_idle_00
    $ renpy.pause(5)
    hide low_aff_idle_00
    show low_aff_idle_blink_00
    $ renpy.pause(0.15)
    hide low_aff_idle_blink_00
    return

label low_aff_pose_01:
    show low_aff_idle_01
    $ renpy.pause(5)
    hide low_aff_idle_01
    show low_aff_idle_blink_01
    $ renpy.pause(0.15)
    hide low_aff_idle_blink_01
    return

label low_aff_pose_02:
    show low_aff_idle_02
    $ renpy.pause(5)
    hide low_aff_idle_02
    show low_aff_idle_blink_02
    $ renpy.pause(0.15)
    hide low_aff_idle_blink_02
    return

label low_aff_pose_03:
    show low_aff_idle_03
    $ renpy.pause(5)
    hide low_aff_idle_03
    show low_aff_idle_blink_03
    $ renpy.pause(0.15)
    hide low_aff_idle_blink_03
    return

label low_aff_pose_04:
    show low_aff_idle_04
    $ renpy.pause(5)
    hide low_aff_idle_04
    show low_aff_idle_blink_04
    $ renpy.pause(0.15)
    hide low_aff_idle_blink_04
    return

#normal aff animations
label normal_aff_pose_00:
    show idle_00
    $ renpy.pause(5)
    hide idle_00
    show idle_blink_00
    $ renpy.pause(0.15)
    hide idle_blink_00
    return

label normal_aff_pose_01:
    show idle_01
    $ renpy.pause(5)
    hide idle_01
    show idle_blink_01
    $ renpy.pause(0.15)
    hide idle_blink_01
    return

label normal_aff_pose_02:
    show idle_02
    $ renpy.pause(5)
    hide idle_02
    show idle_blink_02
    $ renpy.pause(0.15)
    hide idle_blink_02
    return

label normal_aff_pose_03:
    show idle_03
    $ renpy.pause(5)
    hide idle_03
    show idle_blink_03
    $ renpy.pause(0.15)
    hide idle_blink_03
    return

label normal_aff_pose_04:
    show idle_04
    $ renpy.pause(5)
    hide idle_04
    show idle_blink_04
    $ renpy.pause(0.15)
    hide idle_blink_04
    return

#high aff animations
