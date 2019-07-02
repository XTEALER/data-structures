
#returns a string with the elements inside of a list
def ParseList(toParse, Selector):
    x = 0
    Parsed = ""
    for x in range(6):
            if (x < len(toParse)):
                Parsed += ("[" + toParse[x] + "]")
            else:
                Parsed += "[  ]"
            if (Selector):
                Parsed += '\n'
    return Parsed
