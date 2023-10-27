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


def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run_task3():
    data = steps()
    good_steps = []
    bad_steps = []
    for index in data:
        if index[1] >= 50:
            bad_steps.append(index)
        else:
            good_steps.append(index)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run_task3()
