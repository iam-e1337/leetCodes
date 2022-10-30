from cgi import print_arguments


fleetList = [] #    integrated list of position with speed (2d arr)
duplicateCars = [] #    stores index of duplicate cars (2d arr)
newFleet = [] # exp state

position = [7,4,3,2,7,2]
speed = [3,4,6,3,2,4]

# for i in range(len(position)):
#     a[position[i]].append(speed[i])

# for i in range(len(position)): #    to get index of duplicate cars
#     tempList = []
#     if position.count(position[i]) != 1:
#         tempList.append(i)
#         tempList.append(speed[i])
#         duplicateCars.append(tempList.copy())

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

print(yspeeed)

for i in range(len(position)): #    to integrate position with speed
    tempList = []
    tempList.append(position[i])
    tempList.append(speed[i])
    fleetList.append(tempList.copy())

# for i in range(len(fleetList)):
#     for j in range(2):
#         if fleetList[i][0]

# print(duplicateCars)