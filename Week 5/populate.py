def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu_and_input():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")
    response = int(input())
    return direction[response]


def run_task4():
    route = []
    print("Working out escape route...")
    for index in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}")



