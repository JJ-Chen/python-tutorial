def sum_values(values):
    result = 0
    for value in values:
        result += value
    return result


array = [1, 3, 5, 7, 9]
print(sum_values(array))


def show_name(name="frank"):
    print(name)


show_name("peter")
show_name()
show_name(name="peter")
