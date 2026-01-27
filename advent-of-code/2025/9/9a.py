def process_input(file):
    points = []

    for line in file:
        points.append(line.strip().split(','))

    return points

with open("./input.txt") as file:
    points = process_input(file)

    largest = 0

    for i in range(len(points)):
        p1, p2 = int(points[i][0]), int(points[i][1])

        for j in range(i + 1, len(points)):
            p3, p4 = int(points[j][0]), int(points[j][1])

            dx = abs(p3 - p1) + 1
            dy = abs(p4 - p2) + 1

            area = dx * dy

            if area > largest:
                largest = area

    print(largest)
