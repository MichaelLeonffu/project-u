# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define diego = Character("Diego", color="#498A2D")
define brianna = Character("Brianna", color="#55BBF9")
define me = Character("Me")

# The game starts here.

label start:

    scene bg li_estate
    with fade

    play music corny

    "Wow! this must be the Li estate"

    "I wonder what I'll find here..."

    show diego neutral
    with dissolve

    diego "Hi there!"

    me "Oh. Hi Diego."

label choice_nothing:

    diego "How may I take your order?"

    menu:

        "I'd like a Pizza.":
            jump choice_pizza
        
        "...":
            jump choice_nothing

label choice_pizza:

    diego "Pizza?!"
    diego "Well I don't have any of those...."

# label choice_nothing:

    show diego at left
    with moveinleft

    show brianna neutral at right
    with moveinright

    brianna "Good..."
    brianna "...greif, diego you have one in your hand"

    diego "Oh? This thing?"

    hide diego
    with moveoutleft

    show brianna angry

    brianna "sigh"

    show brianna happy at center
    with moveinleft

    brianna "Ah he's gone."

    show brianna neutral

    me "What a strange estate."

    brianna "{cps=20}Yeah...{/cps}"
    brianna "Anyways, welcome to Li estate. \nFeel free to explore around!"

    show brianna angry

    brianna "If you'll excuse me, I need to go catch a Diego."

    show brianna angry at offscreenleft
    with zoomout

    brianna "{color=#880808}{size=+10}{b}Found you!{/b}{/size}{/color}"

    diego "!!!"

    with vpunch
    with hpunch

    me "What a {i}strange{/i} estate...."

    "Good ending?"

    return

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
