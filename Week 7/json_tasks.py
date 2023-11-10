import json

def read(file_path):
    with open("futurama.json") as file:
        data = json.load(file)

        place_name = data["location"]
        print(f"Place name: {place_name}")

        population_size = data["population"]
        print(f"Population size: {population_size}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("futurama.json")

run()
