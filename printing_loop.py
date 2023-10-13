print("What phrase do you want to print?")

phrase = input()

print("outputting...\n")
print("The phrase is: ")

for count in range(0, len(phrase), 1):
    print(phrase[count])