def makeItBig(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"

def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[len(list)-1] = count

def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def average(list):
    avg = 0.0
    for i in list:
        avg += i
    avg = avg / len(list)
    return avg

def length(list):
    return len(list)

def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
    
def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def UltimateAnalyze(list):
    sum = 0
    min = list[0]
    max = list[0]
    length = len(list)

    for i in list:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    
    avg = float(sum) / float(length)
    return {"sumTotal": sum, "average": avg, "minimum": min, "maximum": max}

def reverseList(list):
    for i in range(int(len(list)/2)):
        end = len(list)-i-1
        tmp = list[end]
        list[end] = list[i]
        list[i] = tmp

