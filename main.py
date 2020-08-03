class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bigH = None

    def bigH_update(self, m):
        self.bigH = min(self.bigH, m)


f = open('/Users/apple/Desktop/givenMap.txt')

n = int(f.readline())
m = int(f.readline())

sc = list(f.readline().split())
x, y = int(sc[0]), int(sc[1])

k = int(f.readline())
reds = blues = k

blueBool = redBool = False
blueSteps = redSteps = 0

givenMap = dict()

for i in range(k):
    sc = list(f.readline().split())
    givenMap[int(sc[0]), int(sc[1])] = 'red'
for i in range(k):
    sc = list(f.readline().split())
    givenMap[int(sc[0]), int(sc[1])] = 'blue'

for line in f:
    if line.strip() != '':
        sc = list(line.split())
        givenMap[int(sc[0]), int(sc[1])] = 'block'
print(givenMap)

stepNums = 0
remaining = 2 * k


def final_print():
    print('Number of steps to reach the first RED mushroom: ', redSteps)
    print('Number of steps to reach the first BLUE mushroom: ', blueSteps)


while (True):

    if redBool & blueBool:
        final_print()
        break

# '''nxpancpanc
# a ckadncp
#
# aaxax
# '''
