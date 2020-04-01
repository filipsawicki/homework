"""
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one
side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty
or there is no DNA at all (again, except for Haskell).
"""

def DNA_strand(dna):
    """Slice DNA string to single strings"""
    temp = [i for i in dna]

    """ Changing characters in string"""
    change_temp = []
    for character in temp:
        if character == 'A':
            change_temp.append("T")
        if character == "T":
            change_temp.append("A")
        if character == "G":
            change_temp.append("C")
        if character == "C":
            change_temp.append("G")

    return("".join(change_temp))




print(DNA_strand("AAAA"))

