def hello(to="world"):
    print("hello")


# Ask user's name
print("hello, world")
name = input("Whts is yur name?")

# Remove whitespace
name = name.strip().title()

first, last = name.split(" ")


print("Hello, ", end="")
print(name)
print("hello", name, sep=" ")
print(last)
hello(name)
