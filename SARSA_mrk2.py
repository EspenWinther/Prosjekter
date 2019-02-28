import numpy as np
import random
import turtle
import matplotlib.pyplot as plt
import timeit


start = int(timeit.default_timer())
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("FrozenLake")
wn.setup(1000, 850)
ice_pos = []
goal_pos = []
hole_pos = []
walls = []



class Agent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("white")
        self.penup()
        self.speed(0)
        self.reward = 0
        self.flag = 0
        self.counter = 0
        self.m = 0
        self.dict = {}
        self.fails = []
        self.fail = 0
        self.goals = []
        self.done = 0
        self.goal = 0
        self.pos_orientation = ['east', 'north', 'west', 'south']  # bow pointing [left, up, right, down]
        self.orientation = 'east'
        self.o = 0
        self.nogo = 0

    def get_rewards(self):
        X = self.xcor()
        Y = self.ycor()

        if (X, Y) in hole_pos:
            self.flag = 1
            print('Fail!')
            self.fail = self.fail + 1
            self.fails.append(self.fail)
            self.goals.append(self.goal)
            self.counter = 0
            self.reward = hole.value

        elif (X, Y) in ice_pos:
            if agent.m == 0:
                self.reward = ice.value * 0.5
            elif agent.m == 2:
                self.reward = ice.value * 0.5
            elif agent.m == 3:
                self.reward = ice.value * 0.5
            else:
                self.reward = ice.value

        elif (X, Y) in goal_pos and self.orientation == goal.entry:
            self.flag = 1
            print('Goal!')
            self.goal = self.goal + 1
            self.goals.append(self.goal)
            self.fails.append(self.fail)
            self.counter += 1
            self.reward = goal.value

        elif (X, Y) in goal_pos and self.orientation != goal.entry:
            print('wrong orientation')
            self.reward = 0

# "boat like" movements
    def move_forward(self):
        if self.orientation == 'east':
            X = self.xcor() + 24
            Y = self.ycor()
            if (X, Y) not in walls:
                self.goto(X, Y)

        elif self.orientation == 'north':
            X = self.xcor()
            Y = self.ycor() + 24
            if (X, Y) not in walls:
                self.goto(X, Y)
        elif self.orientation == 'west':
            X = self.xcor() - 24
            Y = self.ycor()
            if (X, Y) not in walls:
                self.goto(X, Y)
        elif self.orientation == 'south':
            X = self.xcor()
            Y = self.ycor() - 24
            if (X, Y) not in walls:
                self.goto(X, Y)
        self.get_rewards()
        #print('forward',self.reward)

    def move_backward(self):
        if self.orientation == 'east':
            X = self.xcor() - 24
            Y = self.ycor()
            if (X, Y) not in walls:
                self.goto(X, Y)
        elif self.orientation == 'north':
            X = self.xcor()
            Y = self.ycor() - 24
            if (X, Y) not in walls:
                self.goto(X, Y)
        elif self.orientation == 'west':
            X = self.xcor() + 24
            Y = self.ycor()
            if (X, Y) not in walls:
                self.goto(X, Y)
        elif self.orientation == 'south':
            X = self.xcor()
            Y = self.ycor() + 24
            if (X, Y) not in walls:
                self.goto(X, Y)
        self.get_rewards()
        #print('backward', self.reward)

    def turn_left(self):
        if self.o < 3:
            self.o = self.o + 1
        elif self.o == 3:
            self.o = 0
        self.orientation = self.pos_orientation[self.o]
        agent.left(90)
        self.get_rewards()
        #print('left', self.reward)

    def turn_right(self):
        if self.o > 0:
            self.o = self.o - 1
        elif self.o == 0:
            self.o = 3
        self.orientation = self.pos_orientation[self.o]
        agent.right(90)
        self.get_rewards()
        #print('right', self.reward)

    def wait(self):
        agent.color('red')
        self.get_rewards()
        agent.color('white')

class Hole(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("gray")
        self.value = -5
        self.penup()
        self.speed(0)


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("green")
        self.penup()
        self.speed(0)
        self.value = 1
        self.entry = 'south'
        self.left(270)
        self.occupied = [0, 1, 2]


class Ice(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.value = -0.5


class BlackTile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


levels = [""]

level_1 = [
    "XXXXX",
    "XSIIX",
    "XIXIX",
    "XIIIX",
    "XIIIX",
    "XIHGX",
    "XXXXX"
]

level_2 = [
    "XXXXXXXXX",
    "XGIIIIIGX",
    "XHHIIIHHX",
    "XIIIIIIIX",
    "XIIIIIIIX",
    "XIIIIIIIX",
    "XIIIIIIIX",
    "XIIIHIIIX",
    "XIIHHHIIX",
    "XIIIHIIIX",
    "XSIIIIIIX",
    "XXXXXXXXX"
]


level_3 = [
    "XXXXXXXXX",
    "XSIIIIIIX",
    "XIIIIIIIX",
    "XIIIHIIIX",
    "XIIHHHIIX",
    "XIIIHIIIX",
    "XIIIIIIIX",
    "XIIIIIIIX",
    "XHHIIIHHX",
    "XIIIIIIIX",
    "XGIIGIIGX",
    "XXXXXXXXX"]

level_4 = [
    "XXXXXXXXXXXXXXXXXX",
    "XHHHHHIIIHHHHHHHHX",
    "XHHIIHIIIHIIHIIIHX",
    "XHHGIHIIIHGIHIIIHX",
    "XHHIIHIIIHIIHGIIHX",
    "XHHIIHIIIHIIHIIIHX",
    "XHHIIHIIIHIIHIIIHX",
    "XHHIIHIIIHIIIIIIHX",
    "XIIIIHIIIIIIIIIIHX",
    "XIIIIIHIIIIIHHHHHX",
    "XIIIIIHIIIIHHHHHHX",
    "XIIIIHIIIIHHHHHHHX",
    "XIIIHIIIIHHHHHHHHX",
    "XIIIIIIIIHHHHHHHHX",
    "XIIIIIIIIIHHHHHHHX",
    "XSIIIIIIIIIIIHHHHX",
    "XXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)


def LakeSetup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = (x*24)
            screen_y = (y*24)

            if character == "S":
                ice_pos.append((screen_x, screen_y))
                ice.goto(screen_x, screen_y)
                ice.stamp()
                agent.goto(screen_x,screen_y)
                global initx, inity
                initx = screen_x
                inity = screen_y
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[agent.pos(), agent.pos_orientation[x], goal.occupied[j]] = [0.0]*5

            elif character == "I":
                ice_pos.append((screen_x, screen_y))
                ice.goto(screen_x,screen_y)
                ice.stamp()
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[ice.pos(), agent.pos_orientation[x], goal.occupied[j]] = [0.0]*5

            elif character == "H":
                hole_pos.append((screen_x, screen_y))
                hole.goto(screen_x,screen_y)
                hole.stamp()
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[hole.pos(), agent.pos_orientation[x], goal.occupied[j]] = [0.0]*5

            elif character == "G":
                goal_pos.append((screen_x, screen_y))
                goal.goto(screen_x,screen_y)
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[goal.pos(), agent.pos_orientation[x], goal.occupied[j]] = [0.0]*5
                goal.stamp()

            else:
                walls.append((screen_x, screen_y))


ice = Ice()
agent = Agent()
goal = Goal()
hole = Hole()
blacktile = BlackTile()
LakeSetup(levels[4])
epsilon = 0.1
alpha = 0.8
gamma = 0.8


def random_move():
    chance = np.random.randint(0, 5)
    if chance == 0:
        m = 0
    elif chance == 1:
        m = 1
    elif chance == 2:
        m = 2
    elif chance == 3:
        m = 3
    elif chance == 4:
        m = 4
    return m


def best_move():
    if max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == agent.dict[agent.pos(), agent.orientation, agent.nogo][0]:
        m = 0
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == agent.dict[agent.pos(), agent.orientation, agent.nogo][1]:
        m = 1
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == agent.dict[agent.pos(), agent.orientation, agent.nogo][2]:
        m = 2
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == agent.dict[agent.pos(), agent.orientation, agent.nogo][3]:
        m = 3
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == agent.dict[agent.pos(), agent.orientation, agent.nogo][4]:
        m = 4
    return m


def take_action(m):
    if m == 0:
        agent.move_forward()
    elif m == 1:
        agent.move_backward()
    elif m == 2:
        agent.turn_left()
    elif m == 3:
        agent.turn_right()
    elif m == 4:
        agent.wait()


def choose_actions():
    if sum(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == 0 or np.random.uniform(0.0, 1.0) < epsilon:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        #prev_m = agent.m
        m = random_move()
        #print('random', agent.m)
    else:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        #prev_m = agent.m
        m = best_move()
        #print('choose', agent.m)
    return prev_pos, prev_or, m #prev_m, m


def update_Q():
    agent.flag = 0
    pos, ori, m = choose_actions()                  # save position before taking action, choose initial action
    while agent.flag == 0:
        take_action(m)                               # take action
        prev_m = m
        if agent.flag == 1:                         # last action was terminal
            agent.dict[pos, ori, agent.nogo][m] = (1 - alpha) * agent.dict[pos, ori, agent.nogo][m] + alpha * agent.reward
        else:                                       # do until terminal
            pos2, ori2, m = choose_actions()        # save what last action was, choose new action (agent.m)
            agent.dict[pos, ori, agent.nogo][prev_m] = (1 - alpha) * agent.dict[pos, ori, agent.nogo][prev_m] + alpha * (agent.reward + gamma * agent.dict[pos2, ori2, agent.nogo][m])
            pos = pos2                              # save previous position as current
            ori = ori2                              # save previous orientation as current

        if 25 == np.random.randint(0, 50):          # resets and occupies goals during episodes
            reset_goals()
            rand_occupied_goal()


def print_opt_policy():
    optimal_pol = {}
    for j in agent.pos_orientation:
        for i in goal.occupied:
            for y in range(1,15):
                for x in range(1,16):
                    if max(agent.dict[(x*24, y*24), j, i]) == agent.dict[(x*24, y*24),j, i][0] and agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'FW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == agent.dict[(x*24, y*24),j, i][1] and agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'BW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == agent.dict[(x*24, y*24),j, i][2] and agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TL'
                    elif max(agent.dict[(x*24, y*24), j, i]) == agent.dict[(x*24, y*24),j, i][3] and agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TR'
                    elif max(agent.dict[(x*24, y*24), j, i]) == agent.dict[(x*24, y*24),j, i][4] and agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'WA'
    print(optimal_pol)
    return optimal_pol


def rand_occupied_goal():
    chance = np.random.uniform(0, 0.4)
    w = 0
    if chance <= 0.1:
        w = 0
        agent.nogo = 0
        print('nogo 0')
    elif 0.1 < chance <= 0.2:
        w = 1
        agent.nogo = 1
        print('nogo 1')
    elif 0.2 < chance <= 0.3:
        w = 2
        agent.nogo = 2
        print('nogo 2')
    blacktile.goto(goal_pos[w])
    walls.append(goal_pos[w])


def reset_goals():
    goal.goto(walls.pop())
    goal.stamp()


def rand_start():
    keys = random.choice(list(x[0] for x in agent.dict.keys()))
    if keys in ice_pos:
        start_pos = keys
    else:
        start_pos = (initx, inity)
    return start_pos


def plot_goals(input):
    plt.plot(input, agent.goals, 'g', label='Goals')
    plt.plot(input, agent.fails, 'r', label='Fails')
    plt.legend(loc='upper left')
    plt.xlabel('Iterations')
    plt.ylabel('Fails/Goals')
    plt.title('Q-learning alpha 0.8')
    plt.grid(True)
    plt.show()


def converge_proof():
    if agent.counter == 10:
        agent.done = 1
    else:
        agent.done = 0


if __name__ == '__main__':
    iterations = 5000
    iteration = []
    i = 0
    rand_occupied_goal()
    for i in range(iterations):
        print(i)
        iteration.append(i)
        key = rand_start()
        agent.goto(key)
        update_Q()
        #print(sol)
        print(agent.goal, agent.fail)
    pol = print_opt_policy()
    stop = int(timeit.default_timer())
    print('runtime =', stop - start)
    plot_goals(iteration)