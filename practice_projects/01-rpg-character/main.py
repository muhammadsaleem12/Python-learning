# Characters used to draw the stat bars
full_dot = '●'
empty_dot = '○'

def create_character(name, STR, INT, CHA):
    # --- NAME VALIDATIONS ---
    
    # Check if the name argument is actually a string type
    if not isinstance(name, str):
        return "The character name should be a string"

    # Check if the name string is empty
    if name == "":
        return "The character should have a name"

    # Check that name length doesn't exceed 10 characters
    if len(name) > 10:
        return "The character name is too long"

    # Ensure the name doesn't contain spaces
    if " " in name:
        return "The character name should not contain spaces"

    # --- STAT VALIDATIONS ---
    
    # Check that all three stats are integer values
    for stats in (STR, INT, CHA):
        if not isinstance(stats, int):
            return "All stats should be integers"

    # Ensure no stat is lower than 1
    for stats in (STR, INT, CHA):
        if stats < 1:
            return "All stats should be no less than 1"

    # Ensure no stat is higher than 4
    for stats in (STR, INT, CHA):
        if stats > 4:
            return "All stats should be no more than 4"
    
    # Ensure the total sum of stat points equals exactly 7
    if STR + INT + CHA != 7:
        return "The character should start with 7 points"

    # --- OUTPUT FORMATTING ---
    
    # Return formatted string with character name and 10-dot stat progress bars
    return (f"{name}\n"
            f"STR {full_dot * STR}{empty_dot * (10 - STR)}\n"
            f"INT {full_dot * INT}{empty_dot * (10 - INT)}\n"
            f"CHA {full_dot * CHA}{empty_dot * (10 - CHA)}")


# Test the function with "Zuko" (STR=4, INT=2, CHA=1 -> Total = 7)
s = create_character("Zuko", 4, 2, 1)
print(s)