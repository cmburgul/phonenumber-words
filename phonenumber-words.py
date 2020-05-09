
mapping = {
    '0':['0'],
    '1':['1'],
    '2':['A','B','C'],
    '3':['D','E','F'],
    '4':['G','H','I'],
    '5':['J','K','L'],
    '6':['M','N','O'],
    '7':['P','Q','R','S'],
    '8':['T','U','V'],
    '9':['W','X','Y','Z']}

# words_to_number

number = "1-800-PAINTER"
number = number.replace("-","")


def words_to_number(number):
    for ch in number:

        for key, val in mapping.items():
            if (ch in val):
                number = number.replace(ch, key)
        op = str(number[0]) + "-" + str(number[1:4]) + "-" + str(number[4:7]) + "-" + str(number[7:])

    return op   
op = words_to_number(number)
print(op)