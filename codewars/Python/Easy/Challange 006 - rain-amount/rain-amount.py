def rain_amount(amount):
    if amount < 40:
        return "You need to give your plant " + str(40 - amount) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
