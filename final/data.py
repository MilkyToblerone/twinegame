
import random

pokemons = {
    "Pikachu": {"type": "Electric", "hp": 35, "attack": 55, "evolves_at": 15, "evolves_to": "Raichu"},
    "Charmander": {"type": "Fire", "hp": 39, "attack": 52, "evolves_at": 16, "evolves_to": "Charmeleon"},
    "Riolu": {"type": "Normal", "hp": 40, "attack": 45, "evolves_at": 20, "evolves_to": "Lucario"},
    "Lucario": {"type": "Normal", "hp": 65, "attack": 70, "evolves_at": 999999999, "evolves_to": "???????"},
    "Blaziken": {"type": "Fire", "hp": 65, "attack": 69, "evolves_at": 999909999, "evolves_to": "???????"},
    "Squirtle": {"type": "Water", "hp": 40, "attack": 53, "evolves_at": 16, "evolves_to": "Wartortle"},
}

boss = {
    "name": "Mewtwo",
    "type": "Normal",
    "hp": 120,
    "attack": 90,
}

types = {
    "Fire": {"Water": 0.5, "Electric": 1.0, "Fire": 0.5, "Normal": 1.0},
    "Water": {"Fire": 2.0, "Electric": 0.5, "Water": 0.5, "Normal": 1.0},
    "Electric": {"Water": 2.0, "Fire": 1.0, "Electric": 0.5, "Normal": 1.0},
    "Normal": {"Water": 1.0, "Fire": 1.0, "Electric": 1.0, "Normal": 1.0},
}

def get_random_pokemon():
    name = random.choice(list(pokemons.keys()))
    base_stats = pokemons[name]
    return {
        "name": name,
        **base_stats,
        "level": random.randint(5,10),
    }

print(get_random_pokemon())