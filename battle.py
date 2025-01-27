import time

def battle_sequence(player, villain):
    while player.is_alive() and villain.is_alive():
        print("\nYour turn:")
        print("1. Attack")
        print(f"2. Use Special Move ({player.special_move['name']})")
        print("3. Heal (Potions left: {player.potions})")
        print(player.status())
        action = input("Choose an action: ")

        if action == "1":
            player.attack(villain)
        elif action == "2":
            player.use_special(villain)
        elif action == "3":
            player.heal()
        else:
            print("Invalid choice. You lose your turn!")

        if not villain.is_alive():
            print(f"\n🎉 You defeated {villain.name}! Victory! 🎉")
            break

        time.sleep(1)
        print("\nVillain's turn...")
        villain.attack(player)

        if not player.is_alive():
            print(f"\n💀 You were defeated by {villain.name}. Game Over! 💀")
            break

        print(f"\n{player.status()} | {villain.status()}")
