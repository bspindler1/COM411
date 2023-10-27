print("What phrase do you want to see in reverse?")

word = input()

print("Reversing...\n")
print("The phrase is: ", end="")
for count in range(len(word) - 1, -1, -1):
    print(word[count], end="")