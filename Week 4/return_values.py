def sum_weights(char, inv):
    total = char + inv
    return total


def calc_avg_weight(char, inv):
    average = (sum_weights(char, inv) / 2)
    return average


def run():
    print("What is the weight of the person?")
    char = int(input())
    print("What is the weight of their inventory?")
    inv = int(input())
    print("Would you like to calculate (sum or average)?")
    decision = input()
    if decision == "sum":
        print(sum_weights(char, inv))
    elif decision == "average":
        print(calc_avg_weight(char, inv))
    else:
        print("That wasn't an option!")


run()
