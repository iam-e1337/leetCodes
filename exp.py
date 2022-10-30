def removeDuplicates(position, speed):
    fleetList = [] #    integrated list of position with speed (2d arr)
    duplicateCars = [] #    stores index of duplicate cars (2d arr)

    unrep = [] #    store unrepeated position

    for x in position: #    get list of unrepeated values of position to for iteration
        if x not in unrep:
            unrep.append(x)

    for i in range(len(unrep)): #    to get index of duplicate cars
        tempList = []
        for j in range(len(position)):
            if position.count(position[j]) != 1 and position[j] == position[i]:
                tempList.append(j)
        if tempList != []:
            duplicateCars.append(tempList.copy())

    yspeeed = []

    for i in range(len(duplicateCars)): #   keep the only car with the lowest speed with same position
        tempPosition = position[duplicateCars[i][0]]
        tempSpeed = []
        for j in range(len(duplicateCars[i])):
            tempSpeed.append(speed[duplicateCars[i][j]])
        
        yspeeed.append([tempPosition, min(tempSpeed)])

    # print(yspeeed)

    for i in range(len(position)): #    to integrate position with speed
        tempList = []
        tempList.append(position[i])
        tempList.append(speed[i])
        fleetList.append(tempList.copy())


    cleanList = fleetList.copy() # list without duplicates

    for i in range(len(fleetList)): # remove the duplicates
        for x in range(len(yspeeed)):
            if fleetList[i][0] == yspeeed[x][0]:
                for j in range(2):
                    if fleetList[i][j] != yspeeed [x][j]:
                        cleanList[i] = 0

    aList = [x for x in cleanList if x != 0]

    finalList = [[x[0] for x in aList], [x[1] for x in aList]]

    return finalList

print(removeDuplicates([], []))