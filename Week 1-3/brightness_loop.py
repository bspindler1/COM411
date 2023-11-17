print("What level of brightness is required?")

brightness = int(input())
print("Adjusting brightness...")
for brightness in range(2, brightness + 1, 2):
    print(f"Brightness level: {'*' * brightness}")

print("Complete!")