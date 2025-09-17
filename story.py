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
            right_whisper()
        else:
            print("You keep walking. The forest remembers your coldness; a quiet cruelty settles in your step.")
    else:
        print("You say nothing. The squirrel flees as a chill settles over the path.")


# --- Right-side expansions (villain-leaning) ---

def right_duel():
    print("The squirrel flourishes a twig like a sword.")
    tactic = input("Do you fight fair or cheat? (fair/cheat/back): ").strip().lower()

    if tactic == "fair":
        print("You fight fair and lose. Laughter echoes; pride curdles.")
        choice = input("Do you accept defeat or swear revenge? (accept/revenge): ").strip().lower()
        if choice == "accept":
            print("You walk away humbled, yet a small meanness takes root.")
        else:
            right_revenge()
    elif tactic == "cheat":
        print("You fling dirt and win easily. The forest falls silent.")
        mercy = input("Do you spare the squirrel, enslave it, or banish it? (spare/enslave/banish): ").strip().lower()
        if mercy == "spare":
            print("You let it go, but the taste of power lingers—sweet and cold.")
        elif mercy == "enslave":
            right_rule("enslave")
        else:
            right_rule("banish")
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
            right_voices()
    elif ploy == "steal":
        print("While it hesitates, you swipe the acorn of voices.")
        use = input("Do you listen to the acorn or crush it? (listen/crush): ").strip().lower()
        if use == "listen":
            right_maps()
        else:
            print("You crush it; a hush falls. The forest grows mean in your image.")
    else:
        print("You stop scheming for a moment. The chance passes, but you feel colder.")


def right_whisper():
    print("In a hollow stump, a whisper coils like smoke and offers you a mark.")
    choice = input("Do you bind it, consume it, or refuse? (bind/consume/refuse): ").strip().lower()

    if choice == "bind":
        print("You bind the whisper to your name. Roots shift aside when you speak.")
        next_step = input("Do you claim a lair or test your sway? (lair/test): ").strip().lower()
        if next_step == "lair":
            print("You mark a ring of stones. Night-creatures gather and wait for orders.")
        else:
            print("You command the brambles to close a path. They obey without question.")
    elif choice == "consume":
        print("You drink the whisper. Your shadow moves half a step ahead, eager.")
        deed = input("Do you send your shadow to scout or to frighten? (scout/frighten): ").strip().lower()
        if deed == "scout":
            print("It returns with shortcuts and secrets. You walk them like a throne.")
        else:
            print("Trees shiver as travelers turn back, afraid of you and what follows.")
    else:
        print("You refuse, but the whisper clings. You leave with a chill that never warms.")


def right_rule(mode):
    if mode == "enslave":
        print("The squirrel bows against its will, eyes dull.")
    else:
        print("You exile the squirrel from its home tree; it trembles on the ground.")
    order = input("Do you set it to spy, guide you, or release it for tribute? (spy/guide/release): ").strip().lower()

    if order == "spy":
        print("It returns with secrets: nests, paths, hidden caches. You claim them as yours.")
    elif order == "guide":
        print("It leads you through thorns that part at your command. You walk like a small tyrant.")
    else:
        print("You grant false mercy, demanding gifts each moon. Fear keeps them coming.")


def right_revenge():
    print("You swear revenge beneath low branches.")
    plan = input("Do you curse the dueling tree, hunt the squirrel, or learn darker tricks? (curse/hunt/learn): ").strip().lower()

    if plan == "curse":
        print("You whisper blight into the bark. Leaves blacken at your touch.")
    elif plan == "hunt":
        print("You track tiny prints and scatter their stores. Hunger will teach them respect.")
    else:
        print("You practice cruel little magics until even the wind gives you space.")


def right_voices():
    print("You break your promise. The acorn opens; many voices gather around your thoughts.")
    command = input("Do you silence the glades, steal their secrets, or test their loyalty? (silence/steal/test): ").strip().lower()

    if command == "silence":
        print("Birdsong stops when you pass. Quiet crowns you like iron.")
    elif command == "steal":
        print("They whisper where keys and caches lie. You take what you want and more.")
    else:
        print("They repeat your words until the forest believes them. Your lies become paths.")


def right_maps():
    print("The acorn lists hidden routes in your mind, each marked by a cold spark.")
    move = input("Do you close the paths, mark a lair, or ambush travelers? (close/lair/ambush): ").strip().lower()

    if move == "close":
        print("You knot the trails into loops. Wanderers tire and turn back at your pleasure.")
    elif move == "lair":
        print("You choose a shaded hollow. Every route now bends toward your seat of power.")
    else:
        print("You wait in the boughs. Footsteps falter; your reputation walks ahead of you.")


if __name__ == "__main__":
    intro()
