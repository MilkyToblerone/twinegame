import random
from data import pokemons,types
from utils import validate_input

def calculate_damage(attacker, defender):
    basedamage = attacker['attack']
    attackertype = attacker['type']
    defendertype = defender['type']
    multiplyer = types.get(attackertype, {}).get(defendertype, 1.0)
    return int(basedamage * multiplyer)

def catch_pokemon(player_team, wild_pokemon):
    # Calculate catch success rate based on wild Pokémon's remaining health
    catch_chance = (1 - (wild_pokemon['hp'] / wild_pokemon['max_hp'])) * 100  # Higher chance if HP is lower
    catch_chance = max(10, min(90, catch_chance))  # Ensure chance is between 10% and 90%
    
    print(f"Attempting to catch {wild_pokemon['name']}... (Chance: {int(catch_chance)}%)")
    if random.random() * 100 < catch_chance:
        player_team.append(wild_pokemon)
        print(f"You caught {wild_pokemon['name']}!")
        return True
    else:
        print(f"{wild_pokemon['name']} broke free!")
        return False

def battle(player_team, wild_pokemon):
    if not player_team:
        print("You have no Pokémon left to battle!")
        return False  # Player loses if team is empty

    active_pokemon = player_team[0]
    wild_pokemon['max_hp'] = wild_pokemon['hp']  # Store max HP for catch chance calculation

    while True:
        print(f"{active_pokemon['name']} (HP: {active_pokemon['hp']}) vs {wild_pokemon['name']} (HP: {wild_pokemon['hp']})")
        print("1. Quick Attack")
        print("2. Power Attack")
        print("3. Switch Pokémon")
        print("4. Catch Pokémon")
        action = validate_input("Choose an action (1-4): ", ["1", "2", "3", "4"])

        if action == "3":  # Switch Pokémon
            print("Choose a Pokémon to switch to:")
            for i, pokemon in enumerate(player_team):
                print(f"{i+1}. {pokemon['name']} (HP: {pokemon['hp']})")
            switch_choice = int(validate_input("Select Pokémon (1-n): ", [str(i+1) for i in range(len(player_team))]))
            if player_team[switch_choice - 1]['hp'] > 0:
                player_team.insert(0, player_team.pop(switch_choice - 1))
                print(f"Switched to {player_team[0]['name']}!")
                continue
            else:
                print("That Pokémon is fainted! Choose a different one.")
                continue

        elif action == "4":  # Catch Pokémon
            if catch_pokemon(player_team, wild_pokemon):
                return True  # End battle if caught
            continue  # Continue battle if catch fails

        else:  # Attack logic
            damage = calculate_damage(active_pokemon, wild_pokemon)
            wild_pokemon['hp'] -= damage
            print(f"{active_pokemon['name']} attacked! {wild_pokemon['name']} has {wild_pokemon['hp']} HP left.")

            if wild_pokemon['hp'] <= 0:
                print(f"You defeated {wild_pokemon['name']}!")
                active_pokemon['xp'] += 10
                evolve_pokemon(active_pokemon)
                return True

        # Wild Pokémon's turn
        damage = calculate_damage(wild_pokemon, active_pokemon)
        active_pokemon['hp'] -= damage
        print(f"{wild_pokemon['name']} attacked! {active_pokemon['name']} has {active_pokemon['hp']} HP left.")

        if active_pokemon['hp'] <= 0:
            print(f"{active_pokemon['name']} has fainted!")
            player_team.pop(0)
            if not player_team:
                print("All your Pokémon have fainted! You lose.")
                return False
            
def evolve_pokemon(pokemon):
    if pokemon['xp'] >= pokemon['evolves_at']:
        evolved_name = pokemon['evolves_to']
        if evolved_name in pokemons:
            pokemon.update({"name": evolved_name, **pokemons[evolved_name]})
            print(f"{pokemon['name']} evolved into {evolved_name}!")
        else:
            print(f"{pokemon['name']} is ready to evolve, but no evolution data is available.")

def random_encounter():
    # Ensure POKEMON_DATA is not empty
    if not pokemons:
        raise ValueError("POKEMON_DATA is empty. Please define Pokémon in data.py.")
    
    # Randomly select a Pokémon from POKEMON_DATA
    name = random.choice(list(pokemons.keys()))
    base_stats = pokemons[name]

    
    # Generate a wild Pokémon with random level and stats
    level = random.randint(5, 10)
    wild_pokemon = {
        "name": name,
        **base_stats,
        "level": level,
        "hp": base_stats['hp'] + (level - 5) * 2,  # Scale HP based on level
        "attack": base_stats['attack'] + (level - 5) * 2,  # Scale attack based on level
    }
    wild_pokemon['max_hp'] = wild_pokemon['hp']  # Store max HP for catch chance calculation
    return wild_pokemon
