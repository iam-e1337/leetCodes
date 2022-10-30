import time
from datetime import datetime
start_time = datetime.now()

position = [1,4,3,2,1,2]
y = []

for x in position:
    y.append(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()

for x in range(len(position)):
    y.append(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))