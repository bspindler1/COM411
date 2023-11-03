import csv

def read_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


def run_task1():
    read_csv("Week 6\clothing.csv")


def extract(path):
    print("Extracting...")
    with open(path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n{names}"
    print("Done!")
    print(f"The extracted items are :\n{names}")


def run_task2():
    extract("Week 6\clothing.csv")


def export(path, items):
    print("Exporting...")
    with open(path, "a") as file:
        for count in range(items):
            print("Please enter the item id:")
            item_id = int(input())

            print("Please enter the item name:")
            item_name = input()

            print("Please enter the item colour:")
            item_colour = input()

            data = f"{item_id},{item_name},{item_colour}\n"
            file.write(data)
    print("Done!")
    

def run_task3():
    export("Week 6\exported_items.csv", 2)

run_task3()
        

