print("How far are we from the target?")
remaining_steps = int(input())

for steps in range(remaining_steps):
    print(f"{remaining_steps} steps remaining")
    remaining_steps = remaining_steps - 1

print("Target achieved!")