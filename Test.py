
ListS = ["-->"]
ListIndexes = [100]
ListSize = 0

def StoreOnList(valueToStore, Pointer):
    ListSize = len(ListS)

    for x in range(ListSize):
        if ListSize > 1 and (x + 1) < ListSize and Pointer > ListIndexes[x] and Pointer < ListIndexes[x + 1]:
            # adds new value on middle of positions that arent bigger or smaller than the value itself
            print(f"between: {ListIndexes[x]} and {ListIndexes[x + 1]}")
            ListIndexes.insert((x + 1), Pointer)
            ListS.insert((x + 1), valueToStore)
            break
        elif Pointer == ListIndexes[x]:
            # if the value to store equals any already on the list then it's going to be saved behind it
            print("equals to")
            ListIndexes.insert(x, Pointer)
            ListS.insert(x, valueToStore)
            break
        elif Pointer < ListIndexes[x] and (x + 1) == ListSize:
            # if the new value is smaller than all others stored, then it's going to be saved at the beggining of the list
            print("its less than")
            ListIndexes.insert((x + 1), Pointer)
            ListS.insert((x + 1), valueToStore)
        elif Pointer > ListIndexes[x] and (x + 1) == ListSize:
            # if the new value is greater than the ones already stored, then it's going to be stored at the end of the list
            print("its more than")
            ListIndexes.insert((x + 1), Pointer)
            ListS.insert((x + 1), valueToStore)

print("\n\n\n")

StoreOnList("hi", 199)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

StoreOnList("hey", 105)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

StoreOnList("hiya", 133)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

StoreOnList("hello", 150)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

StoreOnList("another one", 101)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

StoreOnList("Finals", 170)
print(f"Elements Stored on List: {ListS}, Indexes: {ListIndexes}")

print("\n\n\n")
