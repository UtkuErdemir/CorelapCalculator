import numpy

assocation_array = []
dept_count = int(input("Departman sayısını giriniz:"))
for i in range(dept_count):
    temp = []
    for j in range(dept_count):
        if i != j:
            if i > j:
                temp.insert(j, assocation_array[j][i])
            else:
                assocation = input(str(i + 1) + '-' + str(j + 1) + "arasındaki ilişkiyi giriniz:")
                temp.insert(j, assocation)
        else:
            temp.insert(j, '-')
    assocation_array.insert(i, temp)

def convertIntegerValue(value):
    if value == "a":
        return 125
    elif value == "e":
        return 25
    elif value == "ı":
        return 5
    elif value == "o":
        return 1
    elif value == "x":
        return -125
    else:
        return 0


def calculateValues(array):
    valuesArray = []
    for elementArray in array:
        value = 0
        for element in elementArray:
            value += convertIntegerValue(element)
        valuesArray.append(value)
    return valuesArray


"""assocation_array = [['-', 'a', 'a', 'x', 'u', 'o'], ['a', '-', 'e', 'u', 'ı', 'a'], ['a', 'e', '-', 'x', 'a', 'x'],
                    ['x', 'u', 'x', '-', 'o', 'a'], ['u', 'ı', 'a', 'o', '-', 'a'], ['o', 'a', 'x', 'a', 'a', '-']]"""
assocation_array = [['-', 'ı', 'ı', 'ı', 'o', 'o', 'ı', 'ı', 'e', 'a', 'o', 'a'],
                    ['ı', '-', 'a', 'ı', 'ı', 'ı', 'ı', 'ı', 'u', 'u', 'u', 'o'],
                    ['ı', 'a', '-', 'e', 'o', 'ı', 'o', 'ı', 'x', 'u', 'o', 'o'],
                    ['ı', 'ı', 'e', '-', 'o', 'ı', 'ı', 'ı', 'x', 'u', 'u', 'ı'],
                    ['o', 'ı', 'o', 'o', '-', 'o', 'o', 'o', 'x', 'u', 'u', 'ı'],
                    ['o', 'ı', 'ı', 'ı', 'o', '-', 'ı', 'a', 'o', 'u', 'u', 'x'],
                    ['ı', 'ı', 'o', 'ı', 'o', 'ı', '-', 'a', 'o', 'e', 'u', 'u'],
                    ['ı', 'ı', 'ı', 'ı', 'o', 'a', 'a', '-', 'u', 'u', 'o', 'u'],
                    ['e', 'u', 'x', 'x', 'x', 'o', 'o', 'u', '-', 'e', 'x', 'e'],
                    ['a', 'u', 'u', 'u', 'u', 'u', 'e', 'u', 'e', '-', 'x', 'x'],
                    ['o', 'u', 'o', 'u', 'u', 'u', 'u', 'o', 'x', 'x', '-', 'e'],
                    ['a', 'o', 'o', 'ı', 'ı', 'x', 'u', 'u', 'e', 'x', 'e', '-']]
print("Array",assocation_array)
print("TCR Değerleri",calculateValues(assocation_array))


def createListArray(values):
    temp = []
    for i in range(len(values)):
        temp.append(i)
    return temp


"""def orderBy(values):
    swapped = True
    orderList = createListArray(values)
    while swapped:
        swapped=False
        for i in range(len(values)):
            if i+1<len(values):
                if values[i]>values[i+1]:
                    temp = values[i]
                    values[i] = values[i+1]
                    values[i+1] = temp
                    temp = orderList[i]
                    orderList[i] = orderList[i+1]
                    orderList[i+1] = temp
                    swapped = True
    orderList.reverse()
    return orderList
"""


def orderBy(values):
    orderTemp = []
    for orderCounter in range(len(values)):
        array = []
        if orderCounter == 0:
            array = values
        elif orderCounter != 0 and orderCounter < len(values) - 1:
            assocation_types = ["a", "e", "ı", "o", "u"]
            counter = 0
            loop_temp = []
            while len(loop_temp) == 0:
                loop_temp = [index for index, value in enumerate(assocation_array[orderTemp[orderCounter - 1]]) if
                             value == assocation_types[counter]]
                removeElements = []
                for removeElementIndex in range(len(loop_temp)):
                    if loop_temp[removeElementIndex] in orderTemp:
                        removeElements.append(loop_temp[removeElementIndex])
                for removeElement in removeElements:
                    loop_temp.remove(removeElement)
                counter += 1
            for element in loop_temp:
                array.append(values[element])
        elif orderCounter == len(values) - 1:
            loop_temp = createListArray(values)
            for element in loop_temp:
                if element not in orderTemp:
                    array.append(values[element])
        maximum = max(array)
        index = values.index(maximum)
        orderTemp.append(index)
    orderTemp = [element + 1 for element in orderTemp]
    return orderTemp


print(orderBy(calculateValues(assocation_array)))

""""
def definePositions2(values):
    corelapValueArray = numpy.zeros(shape=(len(assocation_array) * 3, len(assocation_array) * 3))
    corelapArray = numpy.zeros(shape=(len(assocation_array) * 3, len(assocation_array) * 3))
    corelapIndexes = []
    for value_counter in range(len(values)):
        loop_temp = [index for index, value in enumerate(assocation_array[values[value_counter] - 1]) if
                     value == "x"]
        for loop in range(len(loop_temp)):
            ind = values.index(loop_temp[loop] + 1)
            if ind < value_counter:
                if [corelapIndexes[ind][0] - 1, corelapIndexes[ind][1] - 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] - 1, corelapIndexes[ind][1] - 1] -= 62.5
                if [corelapIndexes[ind][0] - 1, corelapIndexes[ind][1]] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] - 1, corelapIndexes[ind][1]] -= 125
                if [corelapIndexes[ind][0] - 1, corelapIndexes[ind][1] + 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] - 1, corelapIndexes[ind][1] + 1] -= 62.5
                if [corelapIndexes[ind][0], corelapIndexes[ind][1] - 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0], corelapIndexes[ind][1] - 1] -= 125
                if [corelapIndexes[ind][0], corelapIndexes[ind][1] + 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0], corelapIndexes[ind][1] + 1] -= 125
                if [corelapIndexes[ind][0] + 1, corelapIndexes[ind][1] - 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] + 1, corelapIndexes[ind][1] - 1] -= 62.5
                if [corelapIndexes[ind][0] + 1, corelapIndexes[ind][1]] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] + 1, corelapIndexes[ind][1]] -= 125
                if [corelapIndexes[ind][0] + 1, corelapIndexes[ind][1] + 1] not in corelapIndexes:
                    corelapValueArray[corelapIndexes[ind][0] + 1, corelapIndexes[ind][1] + 1] -= 62.5
        print("")
        if value_counter == 0:
            corelapIndexes.insert(value_counter, [int((len(assocation_array)) * 3 / 2), int((len(assocation_array)) * 3 / 2)])
        else:
            result = numpy.where(corelapValueArray == numpy.amax(corelapValueArray))
            listOfCordinates = list(zip(result[0], result[1]))
            bestCoord = listOfCordinates[0]
            for coord in listOfCordinates:
                if bestCoord[1] > coord[1]:
                    bestCoord = coord
                elif bestCoord[1] == coord[1]:
                    if bestCoord[0] < coord[0]:
                        bestCoord = coord
            corelapIndexes.insert(value_counter,bestCoord)
        corelapArray[corelapIndexes[value_counter][0], corelapIndexes[value_counter][1]] = values[value_counter]
        corelapValueArray[corelapIndexes[value_counter][0],corelapIndexes[value_counter][1]] = -9999
        if [corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1] - 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1] - 1] += 62.5
        if [corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1]] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1]] += 125
        if [corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1] + 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] - 1, corelapIndexes[value_counter][1] + 1] += 62.5
        if [corelapIndexes[value_counter][0], corelapIndexes[value_counter][1] - 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0], corelapIndexes[value_counter][1] - 1] += 125
        if [corelapIndexes[value_counter][0], corelapIndexes[value_counter][1] + 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0], corelapIndexes[value_counter][1] + 1] += 125
        if [corelapIndexes[value_counter][0]+1, corelapIndexes[value_counter][1] - 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] + 1, corelapIndexes[value_counter][1] - 1] += 62.5
        if [corelapIndexes[value_counter][0]+1, corelapIndexes[value_counter][1]] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] + 1, corelapIndexes[value_counter][1]] += 125
        if [corelapIndexes[value_counter][0]+1, corelapIndexes[value_counter][1] + 1] not in corelapIndexes:
            corelapValueArray[corelapIndexes[value_counter][0] + 1, corelapIndexes[value_counter][1] + 1] += 62.5
        print("")
        #print(corelapValueArray)
    print(corelapArray)
"""


def resetValuesArray(cvaluesArray):
    for cvalueRowCounter in range(len(cvaluesArray)):
        for cvalueColCounter in range(len(cvaluesArray[cvalueRowCounter])):
            if cvaluesArray[cvalueRowCounter][cvalueColCounter] > -10000:
                cvaluesArray[cvalueRowCounter][cvalueColCounter] = 0


def defineValues(cvaluesArray, position, assocation_type):
    alpha = 0.5
    assocation_number = convertIntegerValue(assocation_type)
    cvaluesArray[position[0] - 1, position[1] - 1] += assocation_number*alpha
    cvaluesArray[position[0] - 1, position[1]] += assocation_number
    cvaluesArray[position[0] - 1, position[1] + 1] += assocation_number*alpha
    cvaluesArray[position[0], position[1] - 1] += assocation_number
    cvaluesArray[position[0], position[1] + 1] += assocation_number
    cvaluesArray[position[0] + 1, position[1] - 1] += assocation_number*alpha
    cvaluesArray[position[0] + 1, position[1]] += assocation_number
    cvaluesArray[position[0] + 1, position[1] + 1] += assocation_number*alpha


def definePositions(values):
    corelapValueArray = numpy.zeros(shape=(len(assocation_array) * 3, len(assocation_array) * 3))
    corelapArray = numpy.zeros(shape=(len(assocation_array) * 3, len(assocation_array) * 3))
    corelapIndexes = []
    for value_counter in range(len(values)):
        for defineValueCounter in range(value_counter):
            defineValues(corelapValueArray,corelapIndexes[defineValueCounter],assocation_array[values[value_counter]-1][values[defineValueCounter]-1])
        print("")
        if value_counter == 0:
            corelapIndexes.insert(value_counter, [int((len(assocation_array)) * 3 / 2), int((len(assocation_array)) * 3 / 2)])
        else:
            result = numpy.where(corelapValueArray == numpy.amax(corelapValueArray))
            listOfCordinates = list(zip(result[0], result[1]))
            bestCoord = listOfCordinates[0]
            for coord in listOfCordinates:
                if bestCoord[1] > coord[1]:
                    bestCoord = coord
                elif bestCoord[1] == coord[1]:
                    if bestCoord[0] < coord[0]:
                        bestCoord = coord
            corelapIndexes.insert(value_counter,bestCoord)
        corelapArray[corelapIndexes[value_counter][0], corelapIndexes[value_counter][1]] = values[value_counter]
        corelapValueArray[corelapIndexes[value_counter][0],corelapIndexes[value_counter][1]] = -99999
        resetValuesArray(corelapValueArray)
        print("")
        #print(corelapValueArray)
    print(corelapArray)
    return corelapArray


corelapResultArray = definePositions(orderBy(calculateValues(assocation_array)))
print("utku")
