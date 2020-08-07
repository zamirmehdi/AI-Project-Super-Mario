class State:

    def __init__(self, input_map):
        self.state_map = dict()
        self.mario_loc = None
        self.possible_actions = []

        if input_map is not None:
            self.state_map = input_map
            self.bigH = 2147483647
            key_list = list(self.state_map.keys())
            val_list = list(self.state_map.values())
            self.mario_loc = key_list[val_list.index('mario')]
            self.possible_actions_update()

    def big_h_update(self, amount):
        self.bigH = min(self.bigH, amount)

    def possible_actions_update(self):
        self.possible_actions.clear()
        if self.mario_loc[0] != m and self.state_map.get((self.mario_loc[0] + 1, self.mario_loc[1])) != 'block':
            self.possible_actions.append('right')
        if self.mario_loc[1] != n and self.state_map.get((self.mario_loc[0], self.mario_loc[1] + 1)) != 'block':
            self.possible_actions.append('up')
        if self.mario_loc[0] != 1 and self.state_map.get((self.mario_loc[0] - 1, self.mario_loc[1])) != 'block':
            self.possible_actions.append('left')
        if self.mario_loc[1] != 1 and self.state_map.get((self.mario_loc[0], self.mario_loc[1] - 1)) != 'block':
            self.possible_actions.append('down')


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
    min_big_h = 2147483647
    found = False

    for temp_action in input_state.possible_actions:

        for temp_tuple in result:
            if temp_tuple[0].state_map == input_state.state_map and temp_tuple[1] == temp_action:
                found = True
                min_big_h = min(min_big_h, result.get(temp_tuple).bigH + step_cost)
                break

        if not found:
            min_big_h = min(min_big_h, input_state.bigH)

        found = False

        # if result.get((input_state, temp_action)) is None:
        #     min_big_h = input_state.bigH
        # else:
        #     min_big_h = min(min_big_h, result[input_state, temp_action].bigH + step_cost)

    # for temp in result.keys():
    #     if temp[0].state_map == input_state.state_map and temp[0].state_map != result[temp].state_map:
    #         min_big_h = min(min_big_h, result.get(temp).bigH + step_cost)
    return min_big_h


def move(input_state):
    state = input_state
    ideal_action = ''
    minimum_cost = 2147483647

    ## finding the best move with the least cost:
    for temp_action in state.possible_actions:

        for temp_tuple in result:

            ## repeated actions may have new cost amounts
            if temp_tuple[0].state_map == state.state_map and temp_tuple[1] == temp_action:
                found = True

                print('cost: ', temp_action, result.get(temp_tuple).bigH + step_cost)

                if ideal_action == '' or result.get(temp_tuple).bigH < minimum_cost:
                    ideal_action = temp_action
                    minimum_cost = min(minimum_cost, result.get(temp_tuple).bigH + step_cost)

                break

        ## new actions cost the amount of H(state)
        if result.get((state, temp_action)) is None:
            if ideal_action == '' or state.bigH <= minimum_cost:
                ideal_action = temp_action
                minimum_cost = min(minimum_cost, state.bigH)

        ## repeated actions may have new cost amounts
        else:
            if ideal_action == '' or result.get(state, temp_action).bigH < minimum_cost:
                ideal_action = temp_action
                minimum_cost = min(minimum_cost, result[state, temp_action].bigH + step_cost)

    next_map = state.state_map.copy()
    next_mario_loc = tuple()
    next_state = State(next_map)
    print('\ncurrent map ', next_state.state_map)
    print('current actions ', next_state.possible_actions)

    if ideal_action == 'left':
        next_mario_loc = (state.mario_loc[0] - 1, state.mario_loc[1])
    if ideal_action == 'down':
        next_mario_loc = (state.mario_loc[0], state.mario_loc[1] - 1)
    if ideal_action == 'right':
        next_mario_loc = (state.mario_loc[0] + 1, state.mario_loc[1])
    if ideal_action == 'up':
        next_mario_loc = (state.mario_loc[0], state.mario_loc[1] + 1)

    ## if the result of the chosen action is a BLOCK:
    if givenMap.get(next_mario_loc) == 'block':
        next_state.state_map[next_mario_loc] = 'block'

    ## if the result of the chosen action is a MUSHROOM:
    elif state.state_map.get(next_mario_loc) == 'red' or state.state_map.get(next_mario_loc) == 'blue':

        global remaining
        remaining -= 1
        next_state.state_map[next_mario_loc] = 'mario'
        del next_state.state_map[state.mario_loc]
        next_state.mario_loc = next_mario_loc

        ## if the mushroom is RED:
        if state.state_map.get(next_mario_loc) == 'red':
            global redBool
            redBool = True
            global reds
            reds -= 1

        ## if the mushroom is BLUE:
        else:
            global blueBool
            blueBool = True
            global blues
            blues -= 1

    ## if the result of the chosen action is an EMPTY SPACE:
    else:
        next_state.state_map[next_mario_loc] = 'mario'
        del next_state.state_map[state.mario_loc]
        next_state.mario_loc = next_mario_loc

    ## updates possible actions for this new state considering new map
    next_state.possible_actions_update()

    # print('\nminimum cost = %i  => ideal action = %s' % (minimum_cost, ideal_action))
    print('\nmario\'s loc: %s + %s => %s' % (state.mario_loc, ideal_action.upper(), next_state.mario_loc))
    print('new map ', next_state.state_map)
    print('new possible actions ', next_state.possible_actions)
    print('\nnew amount of:\nRED mush= %i , BLUE mush= %i' % (reds, blues))

    global current
    global last
    global last_is_None
    last = current
    current = next_state
    last_is_None = False

    global stepNums
    stepNums += 1

    global action
    action = ideal_action


## data input from file and parameters creation:
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

stepNums = 1
remaining = 2 * k

currentDict = dict()
for key in givenMap.keys():
    if givenMap[key] == 'red' or givenMap[key] == 'blue' or givenMap[key] == 'mario':
        currentDict[key] = givenMap[key]

current = State(currentDict.copy())

last_is_None = True
last = State(None)
print('current')

states = []

result = dict()
action = ''
step_cost = 1

print('\nGiven map: ', givenMap)
print('''\n------------------------------------------------------------------
*** LRTA* algorithm using REMAINING NUM OF MUSHROOMS heuristic ***
------------------------------------------------------------------''')
while True:

    if redBool and blueBool:
        final_print()
        break

    print('\n\nSTEP %i:\n------' % stepNums)

    ## H(current state) update if current state is a NEW STATE:
    if not any(state.state_map == current.state_map for state in states):
        current.big_h_update(remaining)
        print('H(current state) updated to: ', current.bigH)
        states.append(current)

    else:
        for state in states:
            if state.state_map == current.state_map:
                current = state
                print('H(current state) is: ', current.bigH)
                break
        # print('H(current state) is: ', states[states.index(current)].bigH)

    ## if last state is not null do 2 things:
    if not last_is_None:
        ### 1) add the previous action( + its origin state and its destination state ) to results
        result[last, action] = current
        print('state numbers: ', len(states))

        ### 2) update H(last state) with minimum amount of relative states H (using LRTA*-Cost function)
        states[states.index(last)].big_h_update(lrta_star_cost(last))
        print('H(previous state) updated to: ', states[states.index(last)].bigH)

    ## take an action on current state:
    move(current)

    if stepNums > 30:
        break
