print("How many obstacles must I avoid?")
obstacles = int(input())

number_of_obstacles = 0

while number_of_obstacles < obstacles:
    number_of_obstacles = number_of_obstacles + 1
    print(f"Avoiding...Done! {number_of_obstacles} obstacles avoided.")