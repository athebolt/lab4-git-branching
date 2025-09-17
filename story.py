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
    act = input("What do you do? (pull/inspect/leave): ").strip().lower()

    if act == "pull":
        print("With a steady breath, you pull. The sword slides free, light spilling through the trees.")
        hero_quest()
    elif act == "inspect":
        print("You check the clearing. Under roots you find a worn shield and a faded map pointing to an old tower.")
        take = input("Take the gear? (yes/no): ").strip().lower()
        if take == "yes":
            print("You strap on the shield and tuck the map away.")
        else:
            print("You leave the gear, trusting your feet and your nerve.")
        hero_quest()
    elif act == "leave":
        print("You leave the sword for another and follow a narrow trail out of the clearing.")
        hero_quest()
    else:
        print("You hesitate. A distant horn echoes through the forest.")
        hero_quest()


def hero_quest():
    print("A limping traveler bursts from the brush. 'Please—our village! A dragon nests in the old tower.'")
    help_choice = input("Will you help? (help/ignore): ").strip().lower()

    if help_choice == "help":
        dragon_encounter()
    elif help_choice == "ignore":
        print("You start to walk away, then hear the villagers' cries on the wind. You turn back.")
        dragon_encounter()
    else:
        print("You say nothing, but your feet are already moving toward the tower.")
        dragon_encounter()


def dragon_encounter():
    print("You reach the ivy-choked tower. The dragon coils on a broken spire, eyes like embers.")
    tactic = input("How do you face it? (fight/trick): ").strip().lower()

    if tactic == "fight":
        print("You stand your ground and strike true. The dragon takes wing and flees. The village is safe.")
    elif tactic == "trick":
        print("You ring a rusted bell and toss a torch into the empty granary—by design. The dragon chases sound and fire far away.")
    else:
        print("You raise your voice and speak calmly. The dragon blinks, then lifts away, leaving the tower in peace.")

    print("By nightfall, the villagers call you a hero, and the forest feels lighter.")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")


if __name__ == "__main__":
    intro()
