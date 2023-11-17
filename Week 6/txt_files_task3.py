
def search(file):
    print("Searching..")
    with open(file) as file:
        for line in file:
            print(f"Looked in {line.strip()}")
    print("Done!")

def run_task3():
    search("C:\Users\mroak\vscode\COM411\Week 6\library.txt")


run_task3()