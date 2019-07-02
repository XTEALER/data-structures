import Reader as r
import Parser as p

#Queque method
def Cola():
    cola = []
    choice = 0
    Restr = ""
    ToQueque = ""
    while True:
        if (Restr == ""):
            Restr = p.ParseList(cola, False)

        Restr += (" " * (24 - len(Restr)))
        print('''
┌────────────────────────────┐
│            COLA            │
├────────────────────────────┤
│->''' + Restr +'''->│
├────────────────────────────┤
│  1] VER COLA               │
│  2] AGREGAR ELEMENTO       │
│  3] QUITAR ELEMENTO        │
│  0] SALIR                  │
└────────────────────────────┘''')
        Restr = ""
        choice = r.ReadInt(0, 3)
        if (choice == 1):
            continue
        elif (choice == 2):
            if (len(cola) < 6):
                print("[AGREGAR ELEMENTO]")
                while True:
                    ToQueque = input("[2 CARACTERES MAX]: ")
                    if (len(ToQueque) < 3 and (ToQueque != "")):
                        if(len(ToQueque) == 1):
                            ToQueque += " "
                        cola.insert(0, ToQueque)
                        break
            else:
                Restr = "     OVERFLOW ERROR"
        elif (choice == 3):
            if (len(cola) > 0):
                print("[QUITAR ELEMENTO] (" + cola.pop() + ")")
            else:
                Restr = "    UNDERFLOW ERROR"
        elif (choice == 0):
            print("VOLVIENDO A MENU...")
            break
