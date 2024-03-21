def persian_numbers_converter(mystr):
    numbers = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e, p)

    return mystr