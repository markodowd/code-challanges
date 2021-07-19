def abbrevName(name):
    words = name.split(" ")
    first = words[0][0]
    second = words[1][0]
    letters_joined = first.upper() + "." + second.upper()
    return letters_joined
