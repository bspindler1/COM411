def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


def display_lower(word):
    print(word.lower())


def display_upper(word):
    print(word.upper())


def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")


def repeat(word):
    print("How many times would you like this repeated?")
    times = int(input())
    print(word * times)

print("Enter a word:")
word = input()
print("Choose an option")
print("[1] Display in a box")
print("[2] Display lower-case")
print("[3] Display upper-case")
print("[4] Display mirrored")
print("[5] Display repeated")
print("[6] Quit")
response = int(input())
if response == 1:
    display_box(word)
elif response == 2:
    display_lower(word)
elif response == 3:
    display_upper(word)
elif response == 4:
    display_mirrored(word)
elif response == 5:
    repeat(word)
else:
    print("Unknown option.")