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


def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence":"111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern


def run_task3():
    print("Analysing patterns...")
    patterns = {"short sequence":short_pattern(), "medium sequence":medium_pattern(), "long sequence":long_pattern()}

    for keys, value in patterns.items():
        print(f"{keys}: {value}")


run_task3()

