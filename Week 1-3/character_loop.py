print("What word do you see?")
word = input()

print("Displaying index positions...\n")

for count in range(0, len(word), 1):
    print(f"index {count}: {word[count]}")

print()
print("Done!")
