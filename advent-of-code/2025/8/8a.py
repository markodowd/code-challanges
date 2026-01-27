circuits = []

def cleaned_input(file):
    positions = []

    for line in file:
        positions.append(list(map(int, line.strip().split(","))))

    return positions


with open("./input.txt", "r") as file:
    positions = cleaned_input(file)

    for position in positions:
        pass

        
sorted_circuits = sorted(circuits, key=len, reverse=True)

largest_circuits_product = sorted_circuits[0] * sorted_circuits[1] * sorted_circuits[2]

print(largest_circuits_product)
