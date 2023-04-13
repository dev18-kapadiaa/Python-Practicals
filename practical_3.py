#exception for string size > 100.
class StringSizeExceeded(Exception):
    pass

#exception for array size > 104.
class lengthOverFlow(Exception):
    pass

def Anagrams(li):
    """Sort word alphabetically and add in dictionary and check if that already exists in dictionary or not if it exists then append in dicitojnary's value part.
    And print value pairs of dictionary as an anagram group."""
    dictionary = {}
    for word in li:
        sortedWord = ''.join(sorted(word))

        if sortedWord not in dictionary:
            dictionary[sortedWord] = [word]

        else:
            dictionary[sortedWord] += [word]
    return [dictionary[i] for i in dictionary]


#exceptions for input array size, string length and input string capitalization.
try:
    arr = input("Enter array:")
    list = eval(arr)
    for i in list:
        if len(i) > 100:
            raise StringSizeExceeded
        for j in i:
            if j.isupper():
                raise ValueError
    if len(list) > 104:
        raise lengthOverflow

except StringSizeExceeded:
    print("Length limit of a String exceeded.")
except ValueError:
    print("String entered in an array contain uppercase letter/characters within it.")
except lengthOverFlow:
    print("Array Size Exceeded.")
else:
    print(Anagrams(list))




