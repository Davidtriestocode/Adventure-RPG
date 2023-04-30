def combat(char_attributes, monster_attributes):
    char_attack = char_attributes["Strength"] + char_attributes["Agility"] + char_attributes["Attack"]
    char_defence = char_attributes["Endurance"] + char_attributes["Defence"]
    monster_attack = monster_attributes["Strength"] + monster_attributes["Agility"] + monster_attributes["Attack"]
    monster_defence = monster_attributes["Endurance"] + monster_attributes["Defence"]
    
    if char_attack - monster_defence > monster_attack - char_defence:
        # character wins
        print("You defeated the monster!")
        char_attributes["Experience Points"] += 10
        level_up(char_attributes)
    else:
        # monster wins
        print("You were defeated by the monster!")
        return False
        
    return True
