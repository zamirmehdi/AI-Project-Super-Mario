class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bigH = None

    def h_update(self, m):
        self.bigH = min(self.bigH, m)


f = open('/Users/apple/Desktop/Mario.txt')

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


def minimum_distance_heuristic():
    first_try = 1
    min_dist = 10000
    for temp in givenMap:
        if givenMap.get(temp) == 'blue' or givenMap.get(temp) == 'red':
            if first_try == 1:
                min_dist = temp[0] - x + temp[1] - y
            else:
                min_dist = min(min_dist, abs(temp[0] - x) + abs(temp[1] - y))
                first_try -= 1


def maximum_distance_heuristic():
    max_dist = -1
    for first in givenMap:
        for second in givenMap:
            if (givenMap.get(first) == 'blue' or givenMap.get(first) == 'red') and (
                    givenMap.get(second) == 'blue' or givenMap.get(second) == 'red'):
                max_dist = max(max_dist, abs(first[0] - second[0]) + abs(first[0] - second[0]))


while (True):

    # minimum_distance_heuristic()
    #  break

    if redBool & blueBool:
        final_print()
        break

    # '''nxpancpanc
    # a ckadncp
    #
    # aaxax
    # '''
