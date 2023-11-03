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
    read_csv("C:\Users\mroak\vscode\COM411\Week 6\clothing.csv")


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
    extract("C:\Users\mroak\vscode\COM411\Week 6\clothing.csv")


run_task2()

