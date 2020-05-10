import re

dictionary = "./scrabble/dictionary.txt"

# mapping fot each number to possible characters 
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

# Loading vocabulary words from dictionary to vocab(dict)
vocab = []
with open(dictionary) as d:
    vocab = d.readlines()


def words_to_number(number):
    """ Converts words_to_number"""
    number = number.replace("-","")
    number = number.upper()
    
    for ch in number:

        for key, val in mapping.items():
            if (ch in val):
                number = number.replace(ch, key)
        op = str(number[0]) + "-" + str(number[1:4]) + "-" + str(number[4:7]) + "-" + str(number[7:])
    return op  

def find_valid_word(exp, vocab):
    """ finds valid word from a given set of characters matching in vocabulary"""
    all_words = set()
    for word in vocab:
        hit = re.match(exp, word)
        if hit is not None:
            all_words.add(word.replace("\n", ""))
    return all_words

def get_substrs(string, min_substr_len = 1):
    """ Gives all the possible substrings of a string""" 
    substrs = set()

    # Get all the substrings
    for i in range(len(string)):
        for j in range(i+min_substr_len, len(string)+1):
            substrs = substrs.union([string[i:j]])

    # Split the zeros and ones in the substring
    for substr in substrs.copy():
        if ("0" in substr) or ("1" in substr):
            substrs.remove(substr)
            substrs = substrs.union(substr.replace("0", "1").split("1"))
    return substrs

def all_wordification(number, vocab, min_len=1):
    """ Gives all the possible wordification of a phone number """
    ans = set()
    number = number.replace("-","")
    substrs = get_substrs(number)

    while (len(substrs)>0):
        substr = substrs.pop()
        
        exp = "^" + "".join(["[" + "".join(mapping[char]) + "]" for char in substr]) + "$"
        
        word = find_valid_word(exp, vocab)
        
        if word == set():
            word = None
        else:

            for w in word:
                first = number.find(substr)
                last = number.find(substr)+len(substr)-1

                if (last==10 and first == 4 ):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + str(op[4:first]) + "-" + str(op[first:last+1]))
                elif (last == len(number)-1 and first < 7):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:first]) + "-" + str(op[first:last+1]))
                elif (last == len(number)-1 and first != 7):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:7]) + "-"  + str(op[7:first]) + "-" + str(op[first:last+1]))
                elif (last == len(number)-1 and first == 7):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:first]) + "-" + str(op[first:last+1]))
                elif (first == 4):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + str(op[4:first]) + "-" + str(op[first:last+1]) + "-" + str(op[last+1:]))
                elif (first <= 6):
                    op = number.replace(substr,w)
                    ans.add(str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:first]) + "-" + str(op[first:last+1]) + "-" + str(op[last+1:]))
                elif (first > 7):
                    op = number.replace(substr,w)
                    ans.add((str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:7]) + "-" + str(op[7:first]) +  str(op[first:last+1]) + "-" + str(op[last+1:])))
                else:
                    op = number.replace(substr,w)
                    ans.add((str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:7]) + "-" + str(op[7:first]) +  str(op[first:last+1]) + "-" + str(op[last+1:])))
                    
    return ans
                    
def number_to_word(number, vocab, min_len=1):
    """ Gives the biggest possible wordification of a phone number"""
    largest_word = 1
    ans = set()
    number = number.replace("-","")
    ans = ""
    substrs = get_substrs(number, min_len)
    
    while (len(substrs)>0):
        substr = substrs.pop()
        exp = "^" + "".join(["[" + "".join(mapping[char]) + "]" for char in substr]) + "$"
        
        word = find_valid_word(exp, vocab)
        
        if word == set():
            word = None
        else:
            for w in word:
                if (len(w) > largest_word):
                    largest_word = len(w)
                    
                    first = number.find(substr)
                    last = number.find(substr)+len(substr)-1
                    if (last==10 and first == 4 ):
                        op = number.replace(substr,w)
                        ans = str(op[0]) + "-" + str(op[1:4]) + str(op[4:first]) + "-" + str(op[first:last+1])
                    elif (last == len(number)-1 and first < 7):
                        op = number.replace(substr,w)
                        ans = str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:first]) + "-" + str(op[first:last+1])
                    elif (last == len(number)-1 and first != 7):
                        op = number.replace(substr,w)
                        ans = str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:7]) + "-"  + str(op[7:first]) + "-" + str(op[first:last+1])
                    elif (last == len(number)-1 and first == 7):
                        op = number.replace(substr,w)
                        ans = str(op[0]) + "-" + str(op[1:4]) + "-" + str(op[4:first]) + "-" + str(op[first:last+1])
                    elif (first == 4):
                        op = number.replace(substr,w)
                        ans =  str(op[0]) + "-" + str(op[1:4]) + str(op[4:first]) + "-" + str(op[first:last+1]) + "-" + str(op[last+1:])
                    elif (first <= 6):
                        op = number.replace(substr,w)
                        ans = str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:first]) + "-" + str(op[first:last+1]) + "-" + str(op[last+1:])
                    elif (first > 7):
                        op = number.replace(substr,w)
                        ans = (str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:7]) + "-" + str(op[7:first]) +  str(op[first:last+1]) + "-" + str(op[last+1:]))
                    else:
                        op = number.replace(substr,w)
                        ans = (str(op[0]) + "-" + str(op[1:4]) + "-"  + str(op[4:7]) + "-" + str(op[7:first]) +  str(op[first:last+1]) + "-" + str(op[last+1:]))
    
    return ans


if __name__ == '__main__':

    # number_to_word
    
    ph = "1-800-724-6837"
    # ph = "1-800-356-9377"
    ans = number_to_word(ph, vocab, 1)
    print("Converting a number to wordified number ")
    print("number : ", ph)
    print("wordified number : ", ans)

    print("\n----------")
    # words_to_number
    ph = "1-800-PAINTER"
    # ph = "1-800-Flowers"
    ans = words_to_number(ph)
    print("Converting a wordified number to number")
    print("wordified number : ", ph)
    print("numerified number : ", ans)

    print("\n----------")
    # number_to_words
    ph = "1-800-724-6837"
    # ph = "1-800-356-9377"
    ans = all_wordification(ph, vocab)
    print("Converting a number to wordified numbers ")
    print("number : ", ph)
    print("wordified numbers : ", ans)