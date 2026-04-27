color=input("enter color:")
match color:
    case "red":
        print("You chose red!")
    case "blue":
        print("You chose blue!")
    case _:  # Catch-all for unmatched inputs
        print("Unknown color.")
