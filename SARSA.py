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
wind_pos = []


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
        self.crashes = []
        self.crash = 0
        self.done = 0
        self.goal = 0
        self.pos_orientation = ['east', 'north', 'west', 'south']
        # bow pointing [left, up, right, down]
        self.orientation = 'east'
        self.o = 0
        self.nogo = 0

    def get_rewards(self):
        X = self.xcor()
        Y = self.ycor()

        if (X, Y) in hole_pos:
            self.flag = 1
            print('Fail!')
            self.reward = hole.value
            self.fail = self.fail + 1
            self.fails.append(self.fail)
            self.goals.append(self.goal)
            self.crashes.append(self.crash)
            self.counter = 0

        elif (X,Y) == other.pos():
            self.flag = 1
            print('crash')
            self.crash = self.crash + 1
            self.fails.append(self.fail)
            self.goals.append(self.goal)
            self.crashes.append(self.crash)
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

        #elif (X, Y) in ice_pos:
         #   self.reward = ice.value

        elif (X, Y) in goal_pos and self.orientation == goal.entry:
            self.flag = 1
            print('Goal!')
            self.reward = goal.value
            self.goal = self.goal + 1
            self.goals.append(self.goal)
            self.fails.append(self.fail)
            self.crashes.append(self.crash)
            self.counter += 1

        elif (X, Y) in goal_pos and self.orientation != goal.entry:
            print('wrong orientation')
            self.reward = 0

        elif (X,Y) == (initx, inity):
            self.reward = ice.value

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

    def turn_left(self):
        if self.o < 3:
            self.o = self.o + 1
        elif self.o == 3:
            self.o = 0
        self.orientation = self.pos_orientation[self.o]
        agent.left(90)
        self.get_rewards()

    def turn_right(self):
        if self.o > 0:
            self.o = self.o - 1
        elif self.o == 0:
            self.o = 3
        self.orientation = self.pos_orientation[self.o]
        agent.right(90)
        self.get_rewards()

    def wait(self):
        self.get_rewards()


class Hole(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.value = -160
        self.penup()
        self.speed(0)


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("green")
        self.penup()
        self.speed(0)
        self.value = 100
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
        self.value = -1


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
                print('oh no')
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
    "XIIIX"
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
    "XXXXXXXXXXXXXXXXXX"]

level_5 = [
    "XXXXXXXXXXXXXXXXXX",
    "XHHHHHWIWHHHHHHHHX",
    "XHHIIHWIWHIIHIIWHX",
    "XHHGIHWIWHGIHIIWHX",
    "XHHWIHWIWHWIHGIWHX",
    "XHHIIHWIWHIIHWIWHX",
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
blacktile = BlackTile()
wind = Wind()
other = OtherAgent()
LakeSetup(levels[4])


epsilon = 0.1
alpha = 0.2
gamma = 0.99


def random_move():
    chance = np.random.randint(0, 5)
    if chance == 0:
        agent.m = 0
    elif chance == 1:
        agent.m = 1
    elif chance == 2:
        agent.m = 2
    elif chance == 3:
        agent.m = 3
    elif chance == 4:
        agent.m = 4


def best_move():
    if max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][0]:
        agent.m = 0
       # print('FW')
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][1]:
        agent.m = 1
       # print('BW')
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][2]:
        agent.m = 2
       # print('TL')
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][3]:
        agent.m = 3
       # print('TR')
    elif max(agent.dict[agent.pos(), agent.orientation, agent.nogo]) == \
            agent.dict[agent.pos(), agent.orientation, agent.nogo][4]:
        agent.m = 4
      #  print('WA')


def update_Q():
    Oc = 0
    pos, ori, _ = choose_actions()
    while agent.flag == 0:
        other.go_up(agent.nogo)
        take_action()
        if agent.flag == 1:
            agent.dict[pos, ori, agent.nogo][agent.m] = \
                (1-alpha)*agent.dict[pos, ori, agent.nogo][agent.m]+alpha*agent.reward
        else:
            pos2, ori2, prev_m = choose_actions()
            agent.dict[pos, ori, agent.nogo][prev_m] = \
                (1 - alpha) * agent.dict[pos, ori, agent.nogo][prev_m]+alpha*\
                agent.reward+alpha*gamma*\
                agent.dict[agent.pos(),agent.orientation, agent.nogo][agent.m]
            pos = pos2
            ori = ori2
            if 25 == np.random.randint(0, 150):
                reset_goals()
                rand_occupied_goal()
            #wn.update()
    return agent.dict


def take_action():
    if agent.m == 0:
        agent.move_forward()
    elif agent.m == 1:
        agent.move_backward()
    elif agent.m == 2:
        agent.turn_left()
    elif agent.m == 3:
        agent.turn_right()
    elif agent.m == 4:
        agent.wait()


def choose_actions():
    if sum(agent.dict[agent.pos(), agent.orientation, agent.nogo]) ==\
            0 or np.random.uniform(0.0, 1.0) < epsilon:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        prev_m = agent.m
        random_move()
    else:
        prev_or = agent.orientation
        prev_pos = agent.pos()
        prev_m = agent.m
        best_move()
    return prev_pos, prev_or, prev_m


# think this works now, as long as No X in middle of map
def print_opt_policy():
    optimal_pol = {}
    for j in agent.pos_orientation:
        for i in goal.occupied:
            for y in range(1,15):
                for x in range(1,16):
                    if max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24), j, i][0]:
                        optimal_pol[(x * 24, y * 24), j, i] = 'FW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24), j, i][1]:
                        optimal_pol[(x * 24, y * 24), j, i] = 'BW'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24), j, i][2]:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TL'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24), j, i][3]:
                        optimal_pol[(x * 24, y * 24), j, i] = 'TR'
                    elif max(agent.dict[(x*24, y*24), j, i]) == \
                            agent.dict[(x*24, y*24), j, i][4]:
                        optimal_pol[(x * 24, y * 24), j, i] = 'WA'
        print(optimal_pol)
        return optimal_pol


def rand_occupied_goal():
    chance = np.random.uniform(0, 0.4)
    w = 0
    if chance <= 0.1:
        w = 0
        agent.nogo = 0
    elif 0.1 < chance <= 0.2:
        w = 1
        agent.nogo = 1
    elif 0.2 < chance <= 0.3:
        w = 2
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


def plot_goals():
    plt.plot(iteration, agent.goals, 'g', label='Goals')
    plt.plot(iteration, agent.fails, 'r', label='Fails')
    plt.plot(iteration, agent.crashes, 'b', label='Crashes')
    plt.legend(loc='upper left')
    plt.xlabel('Iterations')
    plt.ylabel('Fails/Goals')
    plt.title('SARSA alpha = 0.2')
    plt.grid(True)
    plt.show()


def converge_proof():
    if agent.counter == 10:
        agent.done = 1
    else:
        agent.done = 0


if __name__ == '__main__':
    iterations = 15000
    iteration = []
    rand_occupied_goal()
    for i in range(iterations):
        print(i)
        iteration.append(i)
        key = rand_start()
        agent.goto(key)
        agent.flag = 0
        agent.reward = 0
        _ = update_Q()
    print(agent.dict)
    stop = int(timeit.default_timer())
    print('runtime =', stop - start)
    print_opt_policy()
    plot_goals()

#random.choice(list(d.keys()))
""""
0. best move function. Ferdig~ish, fungerer sålenge det ikker er vegger på brettet
1. random start. Ferdig, bruker random.choice(list(agent.dict.keys())) som velger random keys, keys = tiles
2. boaty moves  Ferdig  NB!random start funker også her nå
3. multiple goals   Ferdig
4. goals can be occupied    Ferdig
5. moving hole  

hvordan åpne en pickle
with open('agent.dict.pickle', 'rb') as handle:
    b = pickle.load(handle)

turtle.listen()
turtle.onkey(agent.move_forward,"Up")
turtle.onkey(agent.move_backward,"Down")
turtle.onkey(agent.turn_left,"Left")
turtle.onkey(agent.turn_right,"Right")

def reset_or(prev_or, current_or):
    if prev_or == 'north' and current_or == 'east':
        agent.turn_left()
    elif prev_or == 'east' and current_or == 'south':
        agent.turn_left()
    elif prev_or == 'south' and current_or == 'west':
        agent.turn_left()
    elif prev_or == 'west' and current_or == 'north':
        agent.turn_left()
    elif prev_or == 'west' and current_or == 'south':
        agent.turn_right()
    elif prev_or == 'south' and current_or == 'east':
        agent.turn_right()
    elif prev_or == 'east' and current_or == 'north':
        agent.turn_right()
    elif prev_or == 'north' and current_or == 'west':
        agent.turn_right()
    else:
        return 0
print a == b

FØR FUCKUP
def update_Q():
    Oc = 0
    prev_pos, prev_or, _ = choose_actions()
    while agent.flag == 0:
        take_action()
        if agent.flag == 1:
            agent.dict[prev_pos, prev_or, agent.nogo][agent.m] = (1-alpha)*agent.dict[prev_pos, prev_or, agent.nogo][agent.m] + alpha * agent.reward
        else:
            agent.dict[prev_pos, prev_or, agent.nogo][agent.m] = (1-alpha)*agent.dict[prev_pos, prev_or, agent.nogo][agent.m]+alpha*agent.reward
            prev_pos2, prev_or2, prev_m = choose_actions()
            agent.dict[prev_pos, prev_or, agent.nogo][prev_m] += alpha * (gamma * agent.dict[agent.pos(), agent.orientation, agent.nogo][agent.m])
            prev_pos, prev_or, = prev_pos2, prev_or2
        if Oc == np.random.randint(0, 50):
            reset_goals()
            rand_occupied_goal()
            Oc = 0
        wn.update()
        Oc += 1
    return agent.dict


"""