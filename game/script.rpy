# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Raniya", color = "#vhk"))
define p = Character("Pet Store Owner", color = "#bjba")

transform smallright:
    zoom 0.7  # scale down to 40% of original size
    xalign 1.0  # right edge
    yalign 1.0  # bottom edge
transform smallleft:
    zoom 0.7
    xalign -0.7
    yalign 1.0

label scene_loop:
    # Loop through scenes 1-5 with 0.1 second pauses
    $ i = 0
    while i < 6:
        scene 1
        pause 0.05
        scene 2
        pause 0.05
        $ i += 1
    return
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    scene sleep with fade
    play music "snoring-71560.mp3" volume 8.5
    pause 3.0
    play sound "magic-03-278824.mp3"
    scene dream with fade
    pause 3.0
    play music "sweet-acoustic-guitar-music-311691.mp3"
    scene yawn
    play sound "yawning-6096.mp3"
    pause 2.0
    call scene_loop



    return
