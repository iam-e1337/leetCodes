# accumulate speed with position in every iteration until target is reached
# make same speed of cars with same position
# count the number of group of cars that has position  == target

#   ***COMPLETED but time limit exceded***


def carFleet(target, position, speed):
    allFleet = False    # to stop the loop once all cars get to the target.

    Fleets = 0 # store number of fleets

    def removeDuplicates(position, speed): #    [[position][speed]] returns list of position and speed without duplicates.
        fleetList = [] #    integrated list of position with speed (2d arr)
        duplicateCars = [] #    stores index of duplicate cars (2d arr)

        unrep = [] #    store unrepeated position
        unrep = [x for x in position if x not in unrep] #    get list of unrepeated values of position to for iteration
        for i in range(len(unrep)): #    to get index of duplicate cars
            tempList = [j for j in range(len(position)) if position.count(position[j]) != 1 and position[j] == position[i]]
            # for j in range(len(position)):
            #     if position.count(position[j]) != 1 and position[j] == position[i]:
            #         tempList.append(j)
            if tempList != []:
                duplicateCars.append(tempList[:])

        yspeeed = []
        for i in range(len(duplicateCars)): #   keep the only car with the lowest speed with same position
            tempPosition = position[duplicateCars[i][0]]
            tempSpeed = [speed[duplicateCars[i][j]] for j in range(len(duplicateCars[i]))]
            # for j in range(len(duplicateCars[i])):
            #     tempSpeed.append(speed[duplicateCars[i][j]])
            
            yspeeed.append([tempPosition, min(tempSpeed)])

        # print(yspeeed)

        for i in range(len(position)): #    to integrate position with speed
            tempList = []
            tempList.append(position[i])
            tempList.append(speed[i])
            fleetList.append(tempList[:])


        cleanList = fleetList[:] # list without duplicates

        for i in range(len(fleetList)): # remove the duplicates
            for x in range(len(yspeeed)):
                if fleetList[i][0] == yspeeed[x][0]:
                    for j in range(2):
                        if fleetList[i][j] != yspeeed [x][j]:
                            cleanList[i] = 0

        # aList = [x for x in cleanList if x != 0]

        finalList = [[x[0] for x in cleanList if x != 0], [x[1] for x in cleanList if x != 0]]

        return finalList
    
#   in one iteration {
    while allFleet is False:
        newPosition = removeDuplicates(position, speed) #    result of removeDuplicates()
        nextPosition = [[],[]]

        # newPosition = result[0]     # store number of fleets (temp)

        for i in range(len(newPosition[0])): # check if a fleet has reached the target
            if newPosition[0][i] == target:
                newPosition[0][i] = 0
                newPosition[1][i] = 0
                Fleets += 1
        
            if newPosition[0][i] != 0:
                nextPosition[0].append(newPosition[0][i])
                nextPosition[1].append(newPosition[1][i])

        # for i in range(len(newPosition[0])): #  remove the zeros in list that has zeros
        
        if sum(nextPosition[0]) == 0: #     to stop the loop
            allFleet = True

        for i in range(len(nextPosition[0])):  # update the position
            nextPosition[0][i] += nextPosition[1][i]

        position = nextPosition[0]
        speed = nextPosition[1]

       # print(newPosition)
#   }        
    return Fleets

obj = carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
print(obj)