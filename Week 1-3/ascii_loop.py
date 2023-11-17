print("How many bars should be charged?")
bars_charged = int(input())

bars_to_charge = 0

while bars_to_charge < bars_charged:
    bars_to_charge = bars_to_charge + 1
    print(f"Charging: {'█' * bars_to_charge}")

print("The battery is fully charged")