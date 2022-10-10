# accumulate speed with position in every iteration until target is reached
# make same speed of cars with same position
# count the number of group of cars that has position  == target

def carFleet(target, position, speed):
    allFleet = False
    newPos = position.copy()
    while allFleet is False:
        length = len(newPos)

        for i in range(len(newPos)):
            current = newPos[i]
            k = 1
            for j in range(len(newPos)):
                if newPos[j] == current:
                    newPos[j] = k
                else:
                    k+=1

        for i in range(length):
            newPos[i]+= speed[i]

        allFleet = True
        return newPos


obj = carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
print(obj)