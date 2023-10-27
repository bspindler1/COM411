def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    direction = movements()
    print(f"{direction[0]} for {direction[1]} steps")
    print(f"{direction[2]} for {direction[3]} steps")
    print(f"{direction[4]} for {direction[5]} steps")
    print(f"{direction[6]} for {direction[7]} steps")


run_task2()
