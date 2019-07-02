import SimpleList as sl
import CQueque as cq
import Queque as q
import Stack as st
import Reader as r

# global variables
choice = 0
selection = 0

#------------PROGRAM STARTS------------
#keeps the program running until 0 is choosen
while True:
    print('''
┌─────────────────────┐
│  MENU DE SELECCION  │
├─────────────────────┤
│  1] COLA            │
│  2] PILA            │
│  3] COLA CIRCULAR   │
│  4] LISTA SIMPLE    │
│  0] SALIR           │
└─────────────────────┘''')
    #selection of choice
    selection = r.ReadInt(0, 4)

    if (selection == 1):
        q.Cola()
    elif (selection == 2):
        st.Pila()
    elif (selection == 3):
        cq.ColaCircular()
    elif (selection == 4):
        sl.ListaSimple()
    elif (selection == 0):
        print("CERRANDO PROGRAMA...\n")
        break
#------------END OF PROGRAM------------
