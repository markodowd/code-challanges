def neutralise(s1, s2):
    result = ""
    
    for index, char in enumerate(s1):
        if (char == "+" and s2[index] == "+"):
            result += "+"
        elif char == "-" and s2[index] == "-":
            result += "-"
        else:
            result += "0"
    
    return result

