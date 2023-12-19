def check_salute(string):
    salutes = 0
    right_officer_indices = []

    for idx, char in enumerate(string):
        if char == '>':
            right_officer_indices.append(idx)
        elif char == '<':
            salutes += len([i for i in right_officer_indices if i < idx])

    return salutes

strings_to_test = [
    "->-------------<-------",
    "-<------------->-------",
    "-->>----<<--",
    "--->--->----->--",
    "---<---->-->----<<-->"
]

for string in strings_to_test:
    result = check_salute(string)
    print(f"Pour la chaîne '{string}', le nombre de salutations est : {result}")