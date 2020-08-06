class State:
    state_map = dict()
    mario_loc = None
    possible_actions = []

    def __init__(self, input_map):
        # in is not None ke ezafe kardam moshkel dorost nakone
        if input_map is not None:
            self.state_map = input_map
            self.bigH = 2147483647

            key_list = list(self.state_map.keys())
            val_list = list(self.state_map.values())
            self.mario_loc = key_list[val_list.index('mario')]

            if self.mario_loc[0] != 1:
                self.possible_actions.append('left')
            if self.mario_loc[0] != m:
                self.possible_actions.append('down')
            if self.mario_loc[1] != 1:
                self.possible_actions.append('right')
            if self.mario_loc[1] != n:
                self.possible_actions.append('up')

    def big_h_update(self, m):
        self.bigH = min(self.bigH, m)


def final_print():
    print('Number of steps to reach both Red and Blue Mushrooms: ', stepNums)


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


def lrta_star_cost(input_state):
    # input_state = State(input_state)
    # print(input_state == current)
    min_big_h = 2147483647
    # min_big_h = input_state.bigH

    # if result is not None:
    for temp_action in input_state.possible_actions:
        if result.get(input_state, temp_action) is None:
            min_big_h = input_state
        # elif result.get(input_state, temp_action).state_map != input_state.state_map:
        else:
            min_big_h = min(min_big_h, result.get(input_state, temp_action).bigH + step_cost)

    # for temp in result.keys():
    #     # print('action haii ke b block mikhoran check beshan')
    #     if temp[0].state_map == input_state.state_map and temp[0].state_map != result[temp].state_map:
    #         min_big_h = min(min_big_h, result.get(temp).bigH + step_cost)

    return min_big_h


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

givenMap[x, y] = 'mario'
print('Given map: ', givenMap)

stepNums = 1
remaining = 2 * k

currentDict = dict()
for key in givenMap.keys():
    if givenMap[key] == 'red' or givenMap[key] == 'blue' or givenMap[key] == 'mario':
        currentDict[key] = givenMap[key]
current = State(currentDict.copy())

last_is_None = True
last = State(None)
states = []

result = dict()
action = ''
step_cost = 1

while True:

    if redBool & blueBool:
        final_print()
        break

    print('STEP %i:' % stepNums)

    # print('remaining heuristic: ', remaining)
    # print('minimum_distance heuristic: ', minimum_distance_heuristic())
    # print('maximum_distance heuristic: ', maximum_distance_heuristic())
    # print('current_state map: ', current.state_map)
    # print('last_state map: ', last)

    ## H(current state) update if current state is a NEW STATE:
    if not any(state.state_map == current.state_map for state in states):
        current.big_h_update(remaining)
        print('H(current state) updated to: ', current.bigH)
        states.append(current)

    else:
        print('H(current state) is: ', states[states.index(current)].bigH)

    ## if last state is not null do 2 things:
    if not last_is_None:
        ### 1) add the previous action( + its origin state and its destination state ) to results
        result[last, action] = current

        ### 2) update H(last state) with minimum amount of relative states H (using LRTA*-Cost function)
        states[states.index(last)].big_h_update(lrta_star_cost(last))
        print('H(previous state) updated to: ', states[states.index(last)].bigH)

    ## take an action on current state:
    move(current)

    last = current
    last_is_None = False

    # if stepNums > 20:
    break
