name = input("What's your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slizeren")
    case _:
        print("who?")
