from characters import superheroes, villains
from battle import battle_sequence

def start_game():
    print("\n🌟 Welcome to Superhero Battle Arena! 🌟")
    print("Choose your hero:")

    for i, hero in enumerate(superheroes):
        print(f"{i + 1}. {hero.name} (Health: {hero.health}, Attack: {hero.attack_power}, Defense: {hero.defense})")

    choice = int(input("\nEnter the number of your hero: ")) - 1
    player = superheroes[choice]
    print(f"\nYou have chosen {player.name}!\n")

    # Choose a random villain
    import random
    villain = random.choice(villains)
    print(f"⚠️ Your opponent is {villain.name}! Prepare for battle! ⚠️\n")

    battle_sequence(player, villain)

if __name__ == "__main__":
    start_game()
