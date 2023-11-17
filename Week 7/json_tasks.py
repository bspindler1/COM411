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


def read_task2(file_path):
        print("Reading...")

        with open("futurama.json") as file:
            data = json.load(file)

        print("Done!")
        return data


def save(file_path, data):
    print("Exporting...")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")


def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)

run_task2()