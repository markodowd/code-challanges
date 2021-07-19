def fake_bin(x):
    str = ''

    for item in x:
        if int(item) < 5:
            str += '0'
        else:
            str += '1'

    return str
