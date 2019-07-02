
#reads valid integer within min, max values. doesnt return program control until valid int value is inputted
def ReadInt(Min, Max):
    value = 0
    while True:
        try:
            value = int(input(">> "))
            if (value < Min) or (value > Max):
                print("VALOR FUERA DE RANGO!")
            else:
                return value
        except:
            print("INGRESE SOLO NUMEROS")


# message to print, message on except, returns a valid int value after success int value is readed
def intReader(msgToPrint, ErrorMsg):
    ValueToReturn = 0
    while True:
        try:
            ValueToReturn = int(input(msgToPrint))
            break
        except:
            print(ErrorMsg)
    return ValueToReturn
