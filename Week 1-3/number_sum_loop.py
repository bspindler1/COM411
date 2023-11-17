print("How many numbers should I sum up?")
sum = int(input())

start = 1
total = 0

while start <= sum:
    print(f"Please enter number {start} of {sum}:")
    number = int(input())
    start = start + 1
    total = total + number

print(f"The answer is {total}.")
