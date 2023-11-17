def identify():
    print("Enter a word representing what you see")
    word = input()
    if word == "a large boulder":
        return "It's time to run!"

    return "We will be fine."

print(identify())

