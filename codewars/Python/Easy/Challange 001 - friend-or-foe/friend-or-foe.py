def friend(x):
    result = []

    for item in x:
        if len(item) == 4:
            result.append(item)

    return result
