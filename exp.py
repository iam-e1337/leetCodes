fleetList = [] #    integrated list of position with speed (2d)
duplicateCars = [] #    stores index of duplicate cars (2d)

position = [1,1,3]
speed = [3,4,6]

# for i in range(len(position)):
#     a[position[i]].append(speed[i])

for i in range(len(position)): #    to get index of duplicate cars (incomplete)
    tempList = []
    if position.count(i) != 1:
        tempList.append(position[i])
        tempList.append(speed[i])
    fleetList.append(tempList.copy())

for i in range(len(position)): #    to integrate position with speed
    tempList = []
    tempList.append(position[i])
    tempList.append(speed[i])
    fleetList.append(tempList.copy())

# for i in range(len(fleetList)):
#     for j in range(2):
#         if fleetList[i][0]

print(fleetList.count([1,]))