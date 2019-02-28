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
wind_pos =[]
startpos =[]


class Agent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("white")
        self.penup()
        self.speed(0)
        self.reward = 0
        self.wtime = 0
        self.flag = 0
        self.counter = 0
        self.m = 0
        self.dict = {}
        self.fails = []
        self.fail = 0
        self.goals = []
        self.crash = []
        self.crashes = 0
        self.done = 0
        self.goal = 0
        self.pos_orientation = ['east', 'north', 'west', 'south']
        # bow pointing [left, up, right, down]
        self.orientation = 'east'
        self.o = 0
        self.Update = 0
        self.nogo = 0

    def get_rewards(self):
        X = agent.xcor()
        Y = agent.ycor()

        if (X, Y) in hole_pos:
            self.flag = 1
            print('Fail!')
            self.fail = self.fail + 1
            self.fails.append(self.fail)
            self.goals.append(self.goal)
            self.crash.append(self.crashes)
            self.counter = 0
            self.reward = hole.value

        elif (X,Y) == other.pos():
            self.flag = 1
            print('crash')
            self.crashes = self.crashes + 1
            self.fails.append(self.fail)
            self.goals.append(self.goal)
            self.crash.append(self.crashes)
            self.reward = other.value

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
            self.crash.append(self.crashes)
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
        if self.pos() in wind_pos:
            wind.go_right()
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
        if self.pos() in wind_pos:
            wind.go_right()
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
        self.get_rewards()

class Hole(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("gray")
        self.value = -2
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
        self.value = -.5


class BlackTile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


class Wind(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
        self.penup()
        self.speed(0)

    def go_right(self):
        chance = np.random.randint(0,100)
        if chance <= 30:
            X = self.xcor() + 24
            Y = self.ycor()
            if (X, Y) not in walls:
                agent.goto(X,Y)
        elif chance >= 70:
            X = self.xcor() - 24
            Y = self.ycor()
            if (X, Y) not in walls:
                agent.goto(X, Y)

class OtherAgent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.value = -10

    def go_up(self,stuff):
        chance = np.random.randint(0,100)
        pos = self.pos()
        X = self.xcor()
        Y = self.ycor() + 24
        start = goal_pos[stuff]
        if agent.pos() == self.pos():
            print('Oh No!')
        if (X,Y) in hole_pos:
            self.goto(start)
        elif (X,Y) not in walls:
            self.goto(X,Y)
        elif pos == self.pos():
            self.goto(start)


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

level_5 = [
    "XXXXXXXXXXXXXXXXXX",
    "XHHHHHWIWHHHHHHHHX",
    "XHHIIHWIWHIIHIIWHX",
    "XHHGIHWIWHGIHIIWHX",
    "XHHWIHWIWHWIHGOWHX",
    "XHHOIHWIWHOIHWIWHX",
    "XHHIIHWIWHIIHIIWHX",
    "XHHIIHWIWHIIIIIWHX",
    "XWWIIWIIIIIIIIIWHX",
    "XIIIIWHIIIIWHHHHHX",
    "XIIIIWHIIWWHHHHHHX",
    "XIIIWHIIWWHHHHHHHX",
    "XIIIHIIWWHHHHHHHHX",
    "XIIIIIWIWHHHHHHHHX",
    "XIIIWWWIWWHHHHHHHX",
    "XSIIWWWIWWWWWHHHHX",
    "XXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)


def LakeSetup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = (x*24)
            screen_y = (y*24)

            if character == "S":
                ice.goto(screen_x, screen_y)
                ice.stamp()
                agent.goto(screen_x,screen_y)
                global initx, inity
                initx = screen_x
                inity = screen_y
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[agent.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0]*5

            elif character == "I":
                ice_pos.append((screen_x, screen_y))
                ice.goto(screen_x,screen_y)
                ice.stamp()
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[ice.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0]*5

            elif character == "O":
                other.goto(screen_x, screen_y)
                other.stamp()
                startpos.append((screen_x, screen_y))
                ice_pos.append((screen_x, screen_y))
                ice.goto(screen_x,screen_y)
                ice.stamp()
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[ice.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0]*5

            elif character == "H":
                hole_pos.append((screen_x, screen_y))
                hole.goto(screen_x,screen_y)
                hole.stamp()
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[hole.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0]*5

            elif character == "G":
                goal_pos.append((screen_x, screen_y))
                goal.goto(screen_x,screen_y)
                for x in range(0,4):
                    for j in range(0,3):
                        agent.dict[goal.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0]*5
                goal.stamp()

            elif character == "W":
                wind_pos.append((screen_x, screen_y))
                wind.goto(screen_x, screen_y)
                wind.stamp()
                for x in range(0, 4):
                    for j in range(0, 3):
                        agent.dict[wind.pos(), agent.pos_orientation[x],
                                   goal.occupied[j]] = [0.0] * 5

            else:
                walls.append((screen_x, screen_y))


ice = Ice()
agent = Agent()
goal = Goal()
hole = Hole()
wind = Wind()
other = OtherAgent()
blacktile = BlackTile()
LakeSetup(levels[4])
epsilon = 0.1
alpha = 0.5
gamma = 0.9


def random_move():
    chance = np.random.randint(0, 5)
    if chance == 0:
        agent.m = 0
        agent.move_forward()
    elif chance == 1:
        agent.m = 1
        agent.move_backward()
    elif chance == 2:
        agent.m = 2
        agent.turn_left()
    elif chance == 3:
        agent.m = 3
        agent.turn_right()
    elif chance == 4:
        agent.m = 4
        agent.wait()



def best_move():
    if max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][0]:
        agent.m = 0
        agent.move_forward()
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][1]:
        agent.m = 1
        agent.move_backward()
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][2]:
        agent.m = 2
        agent.turn_left()
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][3]:
        agent.m = 3
        agent.turn_right()
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][4]:
        agent.m = 4
        agent.wait()


global states
states = []


def update_Q(model):
    #other.go_up(agent.nogo)
    prev_pos, prev_reward, prev_or = move_and_observe()
    states.append((prev_pos, prev_or, agent.nogo))
    if agent.flag == 1:
        agent.dict[prev_pos, prev_or, agent.nogo][agent.m] = (1 - alpha) * \
        agent.dict[prev_pos, prev_or, agent.nogo][agent.m]+alpha*agent.reward
    else:
        agent.dict[prev_pos, prev_or, agent.nogo][agent.m] = \
            (1-alpha)*agent.dict[prev_pos, prev_or, agent.nogo][agent.m]+alpha*(agent.
            reward+gamma*max(agent.dict[agent.pos(), agent.orientation, agent.nogo]))
    model.append(((prev_pos, prev_or, agent.nogo), (agent.pos(), agent.orientation, agent.nogo), agent.m, agent.reward))
    if len(model) >20:
        for number in range(100):
            x = np.random.randint(0,len(model))
            state = model[x][0]
            #print(state)
            nextstate = model[x][1]
            #print(nextstate)
            action = model[x][2]
            #print(action)
            reward = model[x][3]
            #print(reward)
            agent.dict[state][action] = (1 - alpha) * agent.dict[state][action] + alpha * (reward + gamma * max(agent.dict[nextstate]))
    return agent.dict


def move_and_observe():
    if sum(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == 0 or \
            np.random.uniform(0.0, 1.0) < epsilon:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        prev_reward = agent.reward
        random_move()
    else:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        prev_reward = agent.reward
        best_move()
    return prev_pos, prev_reward, prev_or


def print_opt_policy():
    optimal_pol = {}
    for j in agent.pos_orientation:
        for i in goal.occupied:
            for y in range(1,15):
                for x in range(1,16):
                    if max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24),j, i][0] and \
                            agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'FW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24),j, i][1] and \
                            agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'BW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24),j, i][2] and \
                            agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TL'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24),j, i][3] and \
                            agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TR'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24),j, i][4] and \
                            agent.dict[(x*24, y*24), j, i] not in walls:
                        optimal_pol[(x * 24, y * 24), j, i] = 'WA'
    print(optimal_pol)
    return optimal_pol


def rand_occupied_goal():
    chance = np.random.uniform(0, 0.4)
    #w = 0
    if chance <= 0.1:
     #   w = 0
        agent.nogo = 0
    elif 0.1 < chance <= 0.2:
      #  w = 1
        agent.nogo = 1
    elif 0.2 < chance <= 0.3:
       # w = 2
        agent.nogo = 2
    blacktile.goto(goal_pos[agent.nogo])
    walls.append(goal_pos[agent.nogo])


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
    #plt.plot(input, agent.crash, 'b', label='Crash')
    plt.plot(input, agent.goals, 'g', label='Goals')
    plt.plot(input, agent.fails, 'r', label='Fails')
    plt.legend(loc='upper left')
    plt.xlabel('Iterations')
    plt.ylabel('Fails/Goals/Crashes')
    plt.title('Q-learning alpha 0.5')
    plt.grid(True)
    plt.show()


def converge_proof():
    if agent.counter == 10:
        agent.done = 1
    else:
        agent.done = 0


if __name__ == '__main__':
    iterations = 7000
    iteration = []
    model = []
    j = 0
    rand_occupied_goal()
    for i in range(iterations):
        print(i)
        print(agent.goal, agent.fail)
        print('stuff', agent.crashes + agent.goal + agent.fail, 'iter', i)
        iteration.append(j)
        key = rand_start()
        agent.goto(key)
        agent.reward = 0
        Oc = 0
        while agent.flag == 0:
            sol = update_Q(model)
            if 25 == np.random.randint(0,150):
                reset_goals()
                rand_occupied_goal()
        j += i +1
        agent.flag = 0
    pol = print_opt_policy()
    print(agent.goal, agent.fail, agent.crashes)
    stop = int(timeit.default_timer())
    print('runtime =', stop - start)
    plot_goals(iteration)
