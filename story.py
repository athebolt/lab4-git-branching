def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        neutral_path()


def neutral_path():
    print("You stand still, unsure what to do. The forest hums around you.")
    print("You could sit and listen, climb a tree to look around, or walk straight ahead.")
    action = input("What do you do? (sit/climb/forward): ").strip().lower()

    if action == "sit":
        print("You sit quietly until dawn. Birds lead you to a safe trail out of the woods.")
    elif action == "climb":
        print("You climb a sturdy pine and spot a distant village light. You make your way there—safe and unchanged.")
    elif action == "forward":
        print("You walk forward along a mossy path that loops back to the forest's edge. You leave without glory or guilt.")
    else:
        print("You hesitate too long. Night deepens, and you rest under a tree until morning, then head home.")


def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    choice = input("How do you respond? (duel/trick/ignore): ").strip().lower()

    if choice == "duel":
        right_duel()
    elif choice == "trick":
        right_trick()
    elif choice == "ignore":
        print("You brush past the squirrel. It chatters angrily as shadows gather behind you.")
        follow = input("Do you follow the shadows or keep walking? (follow/walk): ").strip().lower()
        if follow == "follow":
            print("You follow them to a hollow stump and accept their whisper. Your eyes darken; the forest bends to your will.")
        else:
            print("You keep walking. The forest remembers your coldness; a quiet cruelty settles in your step.")
    else:
        print("You say nothing. The squirrel flees as a chill settles over the path.")


def right_duel():
    print("The squirrel flourishes a twig like a sword.")
    tactic = input("Do you fight fair or cheat? (fair/cheat/back): ").strip().lower()

    if tactic == "fair":
        print("You fight fair and lose. Laughter echoes; pride curdles.")
        choice = input("Do you accept defeat or swear revenge? (accept/revenge): ").strip().lower()
        if choice == "accept":
            print("You walk away humbled, yet a small meanness takes root.")
        else:
            print("You swear revenge. The trees darken and seem to approve.")
    elif tactic == "cheat":
        print("You fling dirt and win easily. The forest falls silent.")
        mercy = input("Do you spare the squirrel, enslave it, or banish it? (spare/enslave/banish): ").strip().lower()
        if mercy == "spare":
            print("You let it go, but the taste of power lingers—sweet and cold.")
        elif mercy == "enslave":
            print("You bind the squirrel to your will. Whispers crown you the spiteful warden of this trail.")
        else:
            print("You banish it from its tree. The forest bows to your unkindness.")
    else:
        print("You step back from the duel. A petty hunger for control follows you down the path.")


def right_trick():
    print("You grin and speak in circles. The squirrel squints, uncertain.")
    ploy = input("Do you bargain or steal? (bargain/steal/back): ").strip().lower()

    if ploy == "bargain":
        print("You offer 'protection' for a price. It hands you an acorn etched with tiny eyes.")
        promise = input("Do you keep your word or break it? (keep/break): ").strip().lower()
        if promise == "keep":
            print("You keep your word—then quietly raise the price. Fear becomes your guide.")
        else:
            print("You break it at once. The acorn opens and the voices serve your will.")
    elif ploy == "steal":
        print("While it hesitates, you swipe the acorn of voices.")
        use = input("Do you listen to the acorn or crush it? (listen/crush): ").strip().lower()
        if use == "listen":
            print("Whispered maps of secrets fill your head. Paths bend to your command.")
        else:
            print("You crush it; a hush falls. The forest grows mean in your image.")
    else:
        print("You stop scheming for a moment. The chance passes, but you feel colder.")


if __name__ == "__main__":
    intro()
