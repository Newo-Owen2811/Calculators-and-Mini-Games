fd = "●" 
ed = "○" 
def cc(): 
    while True: 
        name = input("Enter your character's name: ") 
        if name == "": 
            print("The character should have a name.") 
        elif " " in name: 
            print("The character name should not contain spaces.") 
        elif not name.isalpha(): 
            print("The character name should only contain letters.") 
        elif len(name) > 10: 
            print("The character name is too long.") 
        else: 
            break 

    while True: 
        try: 
            stren = int(input("Enter STR: ")) 
            intel = int(input("Enter INT: ")) 
            char = int(input("Enter CHA: ")) 
        except ValueError: 
            print("All stats should be integers.") 
            continue 

        stats = [stren, intel, char] 
        if any(s < 1 for s in stats): 
            print("All stats should be no less than 1.") 
        elif any(s > 4 for s in stats): 
            print("All stats should be no more than 4.") 
        elif sum(stats) != 7: 
            print("The character should start with 7 points.") 
        else: 
            break 

    cd = {
        "name":name,
        "Strength":stren,
        "intelligence":intel,
        "charisma": char
    }
    return cd

hero = cc()
name, stren, intel, char = hero.values()

print(f"\nCharacter Name: {name}") 
print("STR " + fd * stren + ed * (10 - stren)) 
print("INT " + fd * intel + ed * (10 - intel)) 
print("CHA " + fd * char + ed * (10 - char))
#The end