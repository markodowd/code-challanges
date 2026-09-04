def plane_seat(a):
    row = int(a[:-1])
    seat = a[-1]

    if row > 60 or seat in "IJ":
        return "No Seat!!"

    if row > 40:
        row_pos = "Back"
    elif row > 20:
        row_pos = "Middle"
    else:
        row_pos = "Front"

    if seat > "F":
        seat_pos = "Right"
    elif seat > "C":
        seat_pos = "Middle"
    else:
        seat_pos = "Left"

    return f"{row_pos}-{seat_pos}"
