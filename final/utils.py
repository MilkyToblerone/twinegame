def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def display_team(team):
    if not team:
        print("Your team is empty!")
        return
    print("Your Pokémon Team:")
    for i, pokemon in enumerate(team, start=1):
        print(f"{i}. {pokemon['name']} (HP: {pokemon['hp']}, Level: {pokemon['level']}, XP: {pokemon['xp']})")