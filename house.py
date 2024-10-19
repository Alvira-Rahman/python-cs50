name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Cedric":
    print("Hufflepuff")
elif name == "Draco":
    print("Slytherin")
elif name == "Cho Chang":
    print("Ravenclaw")
else:
    print("Who?")
    
# Match
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Cedric":
        print("Hufflepuff")
    case _:
        print("Who?")