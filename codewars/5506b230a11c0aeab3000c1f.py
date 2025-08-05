def evaporator(content, evap_per_day, threshold):
    days = 0
    
    min_ml = content * (1 * threshold / 100)
    
    while content > min_ml:
        content -= (content * (1 * evap_per_day / 100))
        days += 1
    
    return days
