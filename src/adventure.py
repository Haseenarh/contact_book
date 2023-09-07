def start_game():
    print("Welcome to the Text-based Adventure Game!")
    print("You find yourself in a dense forest. The sun is setting, and you need to make a decision.")
    print("Do you want to explore the cave or go to the river?")
    choice = input("Type 'cave' to explore the cave or 'river' to go to the river: ").lower()

    if choice == 'cave':
        explore_cave()
    elif choice == 'river':
        go_to_river()
    else:
        print("Invalid choice. Game Over.")

def explore_cave():
    print("\nYou decide to explore the cave.")
    print("As you go deeper, you see two paths.")
    print("Do you take the left path or the right path?")
    choice = input("Type 'left' to take the left path or 'right' to take the right path: ").lower()

    if choice == 'left':
        print("\nYou find a treasure chest! You're rich!")
    elif choice == 'right':
        print("\nOh no! You encounter a bear and it chases you out of the cave. You barely escape!")
    else:
        print("\nInvalid choice. You're lost in the cave. Game Over.")

def go_to_river():
    print("\nYou decide to go to the river.")
    print("You see a boat and a bridge.")
    print("Do you want to take the boat or cross the bridge?")
    choice = input("Type 'boat' to take the boat or 'bridge' to cross the bridge: ").lower()

    if choice == 'boat':
        print("\nYou take the boat and enjoy a peaceful ride down the river. You're safe!")
    elif choice == 'bridge':
        print("\nThe bridge collapses! You fall into the river and struggle to get to the shore.")
    else:
        print("\nInvalid choice. You're lost. Game Over.")

# Start the game
start_game()
