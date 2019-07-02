import Reader as r 
import Parser as p 

# list global variables
ListStorage = ["->"]
ListIndexes = [100]


def IndexOnList(Index):
    ToReturn = ""
    for n in ListIndexes:
        if Index == n:
            print(Index)
            ToReturn = "      Already Stored"
            break
    return ToReturn


# sorts and stores values on list, ordering them on the process
def StoreOnList(valueToStore, Pointer, ListSize):
    for x in range(ListSize):
        if ListSize > 1 and (x + 1) < ListSize and Pointer > ListIndexes[x] and Pointer < ListIndexes[x + 1]:
            # adds new value on middle of positions that arent bigger or smaller than the value itself
            ListIndexes.insert((x + 1), Pointer)
            ListStorage.insert((x + 1), valueToStore)
            break
        elif Pointer < ListIndexes[x] and (x + 1) == ListSize:
            # if the new value is smaller than all others stored, then it's going to be saved at the beggining of the list
            ListIndexes.insert((x + 1), Pointer)
            ListStorage.insert((x + 1), valueToStore)
        elif Pointer > ListIndexes[x] and (x + 1) == ListSize:
            # if the new value is greater than the ones already stored, then it's going to be stored at the end of the list
            ListIndexes.insert((x + 1), Pointer)
            ListStorage.insert((x + 1), valueToStore)

# fix issues
def StoreChars(IndexToStore, ListSize):
    while True:
        ItemToStore = input("CARACTERES A GUARDAR EN LISTA (MAX. 2): ")
        if len(ItemToStore) > 0 and len(ItemToStore) < 3:
            if(len(ItemToStore) == 1):
                ItemToStore += " "
            MsgToReturn = StoreOnList(ItemToStore, IndexToStore, ListSize)
            break
        elif ItemToStore == "":
            print("NO SE PUEDE GUARDAR UN ELEMENTO VACIO!")
        else:
            print("INGRESE SOLO 2 CARACTERES!")


# adds elements to List
def AddToList(ListSize):
    MsgToReturn = ""
    #reads ID where new element is going to be saved
    while True:
        IndexToStore = r.intReader("ID DE ELEMENTO A AGREGAR (101 a 200): ", "ID INVALIDO")
        if IndexToStore > 100 and IndexToStore <= 200:
            break
        else:
            print("VALOR DE ID FUERA DE RANGO")
    # checks if index has already been stored
    MsgToReturn = IndexOnList(IndexToStore)
    # if index is clear then saves elements to that position
    if(MsgToReturn == ""):
        StoreChars(IndexToStore, ListSize)
    # Returns string
    return MsgToReturn


def RemoveFromList(ListSize):
    MsgToReturn = ""
    if ListSize > 1:
        IndexToRemove = 0
        while True:
            ItemToRemove = r.intReader("POSICION DE ELEMENTO A REMOVER: ", "VALOR NO VALIDO")
            for x in range(ListSize):
                if ItemToRemove == ListIndexes[x] and ItemToRemove > 100 and ItemToRemove <= 200:
                    if (x + 1) < ListSize and ItemToRemove == ListIndexes[x + 1]:
                        IndexToRemove = x + 1
                        break
                    else:
                        IndexToRemove = x
                        break
            if IndexToRemove > 0:
                break
            else:
                print("ID DE POSICION FUERA DE RANGO")
        # deletes items requested on IndexToRemove at lists
        ListStorage.pop(IndexToRemove)
        ListIndexes.pop(IndexToRemove)
    else:
        MsgToReturn = "     UNDERFLOW ERROR"
    # Returns string
    return MsgToReturn


def CleanList(ListSize):
    MsgToReturn = ""
    if ListSize > 1:
        print("LIMPIANDO LISTA...")
        for x in range(ListSize):
            if x > 0:
                ListStorage.pop(1)
                ListIndexes.pop(1)
    else:
        MsgToReturn = "     UNDERFLOW ERROR"
    # Returns error string
    return MsgToReturn
    

#Simple List
def ListaSimple():
    IndexToRemove = 0
    ListString = ""
    UpperMiddleLine = ""
    LowerMiddleLine = ""
    ListSize = 1
    x = 0
    # Program loops until user chooses exit
    while True:
        ListSize = len(ListStorage)
        if ListString == "":
            for x in range(ListSize):
                if x == 0:
                    ListString += str(ListIndexes[0]) + ListStorage[0]
                else:
                    ListString += "[" + ListStorage[x] + "]:" + str(ListIndexes[x]) + "->"

            # defines end of list
            ListString += "NULL"
    
        if ListSize < 3:
            UpperMiddleLine = "┤"
            LowerMiddleLine = "┤"
            if (25 - len(ListString)) > 0:
                ListString += (25 - len(ListString)) * " "
        else:
            UpperMiddleLine = "┴" + "─" *  (len(ListString) - 26) + "┐"
            LowerMiddleLine = "┬" + "─" *  (len(ListString) - 26) + "┘"
            if (25 - len(ListString)) > 0:
                ListString += ((25 + 1) - len(ListString)) * " "
        
        
        print(f'''
┌─────────────────────────┐
│      LISTA  SIMPLE      │
├─────────────────────────{UpperMiddleLine}
│{ListString}│
├─────────────────────────{LowerMiddleLine}
│  1] VER LISTA SIMPLE    │
│  2] AGREGAR ELEMENTO    │
│  3] QUITAR ELEMENTO     │
│  4] LIMPIAR LISTA       │
│  0] SALIR               │
└─────────────────────────┘''')
        choice = r.ReadInt(0, 4)
        ListString = ""
        if (choice == 1):
            continue
        elif (choice == 2):
            if ListSize < 7:
                # stores position pointer
                ListString = AddToList(ListSize)
            else:
                ListString = "      OVERFLOW ERROR"
        elif (choice == 3):
            ListString = RemoveFromList(ListSize)
        elif choice == 4:
            ListString = CleanList(ListSize)
        elif choice == 0:
            print("VOLVIENDO A MENU...")
            break
