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


if __name__ == "__main__":
    intro()
