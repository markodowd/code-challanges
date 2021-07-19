def calculate_age(year_of_birth, current_year):
    if current_year > year_of_birth:
        age = current_year - year_of_birth
        if age == 1:
            return "You are " + str(age) + " year old."
        else:
            return "You are " + str(age) + " years old."
    elif current_year < year_of_birth:
        age = year_of_birth - current_year
        if age == 1:
            return "You will be born in " + str(age) + " year."
        else:
            return "You will be born in " + str(age) + " years."
    elif current_year == year_of_birth:
        return "You were born this very year!"
