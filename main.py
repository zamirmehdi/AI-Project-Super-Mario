class State:
    state_map = dict()

    def __init__(self, input_map):
        self.state_map = input_map
        self.bigH = 2147483647

    def big_h_update(self, m):
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
print('Given map: ', givenMap)

stepNums = 0
remaining = 2 * k

current = State(givenMap.copy())
last = None
states = []


def final_print():
    print('Number of steps to reach the first RED mushroom: ', redSteps)
    print('Number of steps to reach the first BLUE mushroom: ', blueSteps)


def minimum_distance_heuristic():
    first_try = 1
    min_dist = 10000
    for temp in current.state_map:
        if current.state_map.get(temp) == 'blue' or current.state_map.get(temp) == 'red':
            if first_try == 1:
                min_dist = abs(temp[0] - x) + abs(temp[1] - y)
            else:
                min_dist = min(min_dist, abs(temp[0] - x) + abs(temp[1] - y))
                first_try -= 1
    return min_dist


def maximum_distance_heuristic():
    max_dist = -1
    for first in current.state_map:
        for second in current.state_map:
            if (current.state_map.get(first) == 'blue' or current.state_map.get(first) == 'red') and (
                    current.state_map.get(second) == 'blue' or current.state_map.get(second) == 'red'):
                max_dist = max(max_dist, abs(first[0] - second[0]) + abs(first[0] - second[0]))
    return max_dist


while (True):


while True:

    if redBool & blueBool:
        final_print()
        break

    if any(state.state_map == current.state_map for state in states):
        print(states[states.index(current)].bigH)
    else:
        states.append(current)
        states[states.index(current)].big_h_update(remaining)

    if last is not None:
        print('result[last, action = current')

    break
