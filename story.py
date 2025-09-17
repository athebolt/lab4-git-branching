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
    choice = input("Do you pull it, inspect it, or leave it alone? (pull/inspect/leave): ").strip().lower()

    if choice == "pull":
        left_pull()
    elif choice == "inspect":
        left_inspect()
    elif choice == "leave":
        print("You decide not to disturb it and follow a soft trail of moss out of the clearing.")
    else:
        print("You wait beside the stone until the glow fades, then wander back the way you came.")


def left_pull():
    print("You grip the hilt. The sword hums softly under your fingers.")
    effort = input("How do you try to free it? (one/two/back): ").strip().lower()

    if effort == "one":
        print("With one hand it barely moves. Your palm tingles.")
        second_try = input("Try with both hands or step back? (two/back): ").strip().lower()
        if second_try == "two":
            left_sword_out()
        else:
            print("You let go. The humming stops. A calm path leads you away from the clearing.")
    elif effort == "two":
        left_sword_out()
    else:
        print("You release the hilt. The forest sighs, and you leave quietly.")


def left_sword_out():
    print("With a slow scrape, the blade slides free. A pale beam points to a hidden footpath.")
    decision = input("Do you keep the sword or return it? (keep/return): ").strip().lower()

    if decision == "keep":
        print("You keep the blade. The beam guides you to the forest edge. A new journey waits, but not tonight.")
    elif decision == "return":
        print("You set the sword back. The light dims, and a gentle breeze carries you to a safe road home.")
    else:
        print("You hesitate, then wrap the sword in leaves and rest. At dawn, you walk out quietly, unsure but at peace.")


def left_inspect():
    print("You study faint runes around the stone. The glow steadies, like a calm breath.")
    action = input("Do you read the runes, knock on the stone, or leave? (read/knock/leave): ").strip().lower()

    if action == "read":
        print("The runes speak of intent over strength.")
        vow = input("Do you make a quiet pledge to do no harm? (pledge/back): ").strip().lower()
        if vow == "pledge":
            print("The stone warms. The sword loosens without effort.")
            left_sword_out()
        else:
            print("You step back. The glow softens, and a narrow track leads you safely away.")
    elif action == "knock":
        print("You tap the stone. A tiny panel opens to reveal a smooth, warm pebble.")
        pebble = input("Do you take the pebble or leave it? (take/leave): ").strip().lower()
        if pebble == "take":
            print("The pebble glows in your pocket and guides you to a quiet stream and an easy path home.")
        else:
            print("You close the panel. The forest settles. You leave the clearing unchanged.")
    else:
        print("You leave the mystery for another day and follow the wind out of the trees.")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")


if __name__ == "__main__":
    intro()
