class State:
    map = dict()

    def __init__(self, input_map):
        self.map = input_map
        self.bigH = None

    def big_h_update(self, m):
        self.bigH = min(self.bigH, m)

    def get_map(self):
        return self.map


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

current = givenMap.copy()
states = list()
states.append(State(current))


def final_print():
    print('Number of steps to reach the first RED mushroom: ', redSteps)
    print('Number of steps to reach the first BLUE mushroom: ', blueSteps)


def minimum_distance_heuristic():
    first_try = 1
    min_dist = 10000
    for temp in current:
        if current.get(temp) == 'blue' or current.get(temp) == 'red':
            if first_try == 1:
                min_dist = abs(temp[0] - x) + abs(temp[1] - y)
            else:
                min_dist = min(min_dist, abs(temp[0] - x) + abs(temp[1] - y))
                first_try -= 1
    return min_dist


def maximum_distance_heuristic():
    max_dist = -1
    for first in current:
        for second in current:
            if (current.get(first) == 'blue' or current.get(first) == 'red') and (
                    current.get(second) == 'blue' or current.get(second) == 'red'):
                max_dist = max(max_dist, abs(first[0] - second[0]) + abs(first[0] - second[0]))
    return max_dist


while (True):

    # print(maximum_distance_heuristic())
    # break

    if redBool & blueBool:
        final_print()
        break

    if states[0].get((1, 1)) is None:
        states[0][1, 1] = 'black'
        print(states[0])

        diffChecker = False

        for tempState in states:
            diffChecker = False
            for tempLoc in tempState.keys():
                if tempState.get(tempLoc) != current.get(tempLoc):
                    diffChecker = True
                    break
            if diffChecker is False:
                break

        if diffChecker:
            states.append(current)
        else:
            print('Kamel shavad')

        break
    else:
        break

# '''nxpancpanc
# a ckadncp
#
# aaxax
# '''
