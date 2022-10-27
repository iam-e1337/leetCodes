# accumulate speed with position in every iteration until target is reached
# make same speed of cars with same position
# count the number of group of cars that has position  == target

def carFleet(target, position, speed):
    allFleet = False    # to stop the loop once all cars get to the target.

    Fleets = [] # store number of fleets

    # in one iteration {

    newPosition = []     # store number of fleets (temp)
    for i in (position): 
        if i not in newPosition:
            newPosition.append(i)
    # print(uniqueNums)

    for i in newPosition: # check if a fleet has reached the target
        if i == target:
            newPosition.remove(i)
            Fleets.append(1)

    for i in range(len(newPosition)):  # update the position
        newPosition[i] += speed[i]

    # }
    
    return newPosition

obj = carFleet(12, [2,2,0,5,3], [2,4,1,1,3])
print(obj)