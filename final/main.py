from data import pokemons, boss
from logic import battle, catch_pokemon, evolve_pokemon, random_encounter
from file_ops import save_game, load_game
from utils import validate_input, display_team

def main():
    print("Welcome to the Pokémon-inspired Game!")
    player_team = load_game() or []  # Load team or start fresh

    if not player_team:
        print("Choose your starter Pokémon:")
        starters = list(pokemons.keys())
        for i, starter in enumerate(starters, start=1):
            print(f"{i}. {starter}")
        choice = validate_input("Select your starter (1-3): ", ["1", "2", "3"])
        starter_choice = starters[int(choice) - 1]
        starter_pokemon = {"name": starter_choice, **pokemons[starter_choice], "level": 5, "xp": 0}
        player_team.append(starter_pokemon)
        print(f"You chose {starter_choice} as your starter!")

    final_boss_defeated = False

    while True:
        print("\nMenu:")
        print("1. Explore")
        print("2. View Team")
        print("3. Save Game")
        print("4. Quit")
        choice = validate_input("Choose an option: ", ["1", "2", "3", "4"])

        if choice == "1":  # Explore
            wild_pokemon = random_encounter()
            print(f"You encountered a wild {wild_pokemon['name']}!")
            if battle(player_team, wild_pokemon):
                print("You won the battle!")
            else:
                print("You lost the battle!")
                if not player_team:
                    print("All your Pokémon have fainted! Game over.")
                    break
        elif choice == "2":  # View Team
            display_team(player_team)
        elif choice == "3":  # Save Game
            save_game(player_team)
        elif choice == "4":  # Quit
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()