data = {'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}


def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences


def run():
    print(pattern())
    display_keys(data)
    print("")
    display_values(data)
    print("")
    display_items(data)


def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)


def display_values(data):
    print("Values")
    for value in data.values():
        print(value)


def display_items(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")

run()