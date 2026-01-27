START = "you"
END = "out"


def prepare_input(file):
    result = {}

    for line in file:
        line = line.strip()
        key, values = line.split(":")
        key = key.strip()
        values_list = values.strip().split()
        result[key] = values_list

    return result


def find_paths_to_out(graph, start, path=None):
    if path is None:
        path = []

    path = path + [start]

    if graph[start] == [END]:
        return [path]

    paths = []
    for nxt in graph[start]:
        if nxt not in graph:
            continue
        paths.extend(find_paths_to_out(graph, nxt, path))

    return paths


with open("./input.txt", "r") as file:
    devices = prepare_input(file)

    paths = find_paths_to_out(devices, START)

    print(len(paths))
