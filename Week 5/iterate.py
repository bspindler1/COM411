def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu():
    print("Please select a directions:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")


def run_task3():
    menu()


run_task3()