data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(any_structure):
    flat = []
    sum_structure = 0
    for i in any_structure:
        if isinstance(i, (set, list, tuple)):
            flat.append(calculate_structure_sum(i))
        elif isinstance(i, dict):
            for k, v in i.items():
                flat.append(k)
                flat.append(v)
        else:
            flat.append(i)
    for i in flat:
        if isinstance(i, int):
            sum_structure += i
        else:
            sum_structure += len(i)
    return sum_structure


result = calculate_structure_sum(data_structure)
print(result)
