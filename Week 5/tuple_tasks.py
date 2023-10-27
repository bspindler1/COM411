def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}%")


def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    data = likelihood_min_max()
    print(f"Minimum likelihood of falling: {data[0]}%")
    print(f"Maximum likelihood of falling: {data[1]}%")


run_task2()


