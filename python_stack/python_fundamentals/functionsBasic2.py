def countdown(num):
    for i in range(num,-1,-1):
        print(i)

def printAndReturn(list):
    print(list[0])
    return list[1]  

def firstPlusLength(list):
    return list[0] + len(list)

def valuesGreaterThanSecond(list):
    newList = []
    if len(list) == 1:
        return False
    secondVal = list[1]
    for i in list:
        if i > secondVal:
            newList.append(i)
    return newList

print(len(valuesGreaterThanSecond([8,5,4,10])))

def lengthAndValue(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList