import Parser as p
import Reader as r

#Stack Method
def Pila():
    pila = []
    choice = 0
    ToStack = ""
    Restr = ""
    Stack = []
    while True:
        if (Restr == ""):
            Restr = p.ParseList(pila, True)
            Stack = Restr.split('\n')
            Restr = ""
        
        Restr += (" " * (22 - len(Restr)))
        print('''
┌────────────────────────────┐
│            PILA            │
├───────────────────────┬────┤
''' +
"│  1] VER PILA          │" + Stack[5] + (" " * (4 - len(Stack[5]))) +
"│\n│  2] AGREGAR ELEMENTO  │" + Stack[4] + (" " * (4 - len(Stack[4]))) +
"│\n│  3] QUITAR ELEMENTO   │" + Stack[3] + (" " * (4 - len(Stack[3]))) +
"│\n│  0] SALIR             │" + Stack[2] + (" " * (4 - len(Stack[2]))) +
"│\n├───────────────────────┤" + Stack[1] + (" " * (4 - len(Stack[1]))) +
"│\n│ " + Restr + "│" + Stack[0] + (" " * (4 - len(Stack[0]))) +
"│\n└───────────────────────┴────┘")
        Restr = ""
        choice = r.ReadInt(0, 3)
        if (choice == 1):
            continue
        elif (choice == 2):
            if (len(pila) < 6):
                print("[AGREGAR ELEMENTO]")
                while True:
                    ToStack = input("[2 CARACTERES MAX]: ")
                    if (len(ToStack) < 3 and ToStack != ""):
                        if (len(ToStack) == 1):
                            ToStack += " "
                        pila.append(ToStack)
                        break
            else:
                Restr = "   OVERFLOW ERROR"
        elif (choice == 3):
            if (len(pila) > 0):
                print("[QUITAR ELEMENTO] (" + pila.pop() + ")")
            else:
                Restr = "   UNDERFLOW ERROR"
        elif (choice == 0):
            print("VOLVIENDO A MENU...")
            break
