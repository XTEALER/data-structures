from collections import deque
import Reader as r


# Queque variables
colaRound = ["  ", "  ", "  ", "  ", "  ", "  "]
QuequeSize = 6
ToQueque = ""


# checks if Round Queque is "full", if not then returns False
def isQuequeFull():
    ItemsOnQueque = 0

    for x in range(QuequeSize):
        if colaRound[x] != "  ":
            ItemsOnQueque += 1
    
    if ItemsOnQueque == QuequeSize:
        Status = True
    else:
        Status = False

    return Status


# checks if Round Queque is "empty", if not then returns False
def isQuequeEmpty():
    SpaceOnQueque = 0

    for x in range(QuequeSize):
        if colaRound[x] == "  ":
            SpaceOnQueque += 1
    
    if SpaceOnQueque == QuequeSize:
        Status = True
    else:
        Status = False

    print(f"is Empty: {Status}; Items: {SpaceOnQueque}")
    return Status


#circular queque
def ColaCircular():
    
    # choice and output variables
    choice = 0
    Restr = ""

    # Arrow control variables
    FrontPointer = ""
    RearPointer = ""
    RearIndex = 0
    FrontIndex = 0

    while True:
        if (Restr == ""):
            Items = 0

            # passes elements on list to string that is going to be printted
            for x in range(QuequeSize):
                Restr += ("[" + colaRound[x] + "]")
            
            # controls Front arrow position
            FrontPointer = ((" " * (FrontIndex * 4)) + "▼▼")
            FrontPointer += (" " * (22 - len(FrontPointer)))

            # controls Rear arrow position
            RearPointer = ((" " * (RearIndex * 4)) + "▲▲")
            RearPointer += (" " * (22 - len(RearPointer)))
        else:
            # error in flow
            FrontPointer = ("▼" * 22)
            RearPointer = ("▲" * 22)

        Restr += (" " * (24 - len(Restr)))
        print(f'''
┌─────────────────────────────────┐
│          COLA CIRCULAR          │
├────────────────────────┬────────┤
│ {FrontPointer} │ FINAL  │
│''' + Restr + f'''├────────┤
│ {RearPointer} │ FRENTE │
├────────────────────────┼────────┘
│  1] VER COLA           │
│  2] AGREGAR ELEMENTO   │
│  3] QUITAR ELEMENTO    │
│  0] SALIR              │
└────────────────────────┘''')
        choice = r.ReadInt(0, 3)
        Restr = ""

        if (choice == 1):
            continue
        elif (choice == 2):
            if not isQuequeFull():
                print("[AGREGAR ELEMENTO]")
                while True:
                    ToQueque = input("[2 CARACTERES MAX]: ")
                    if (len(ToQueque) < 3 and (ToQueque != "")):
                        if(len(ToQueque) == 1):
                            ToQueque += " "
                        colaRound[FrontIndex] = ToQueque
                        break
                # index counter
                FrontIndex += 1
                if (FrontIndex == 6):
                    FrontIndex = 0
            else:
                Restr = "     OVERFLOW ERROR"
        elif (choice == 3):
            if not (isQuequeEmpty()):
                print("[QUITAR ELEMENTO] (" + colaRound[RearIndex] + ")")
                colaRound[RearIndex] = "  "
                #index counter
                RearIndex += 1
                if (RearIndex == 6):
                    RearIndex = 0
            else:
                Restr = "    UNDERFLOW ERROR"
        elif (choice == 0):
            print("VOLVIENDO A MENU...")
            break
