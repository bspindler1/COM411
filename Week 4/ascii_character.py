print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())

if code in range(32,127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}")
else:
    print("The code needs to be in the range 32 - 126 inclusive")

print("Program ended!")