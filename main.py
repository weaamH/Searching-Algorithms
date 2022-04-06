from Node import *


def getId(city):
    for i in range(len(listofnodes)):
        if listofnodes[i].get_cityname() == city:
            id = listofnodes[i].get_city_id()
    return id


def getName(index):
    for i in dic:
        if i == index:
            name = dic[i]
    return name


def DFS(depth, listofnodes, distance, initialState, goals):
    temp = depth
    edge = 1
    path = []  # to get goals path
    stack = []  # to store nodes
    found = []  # goals found
    visitedcities = []  # to avoid stuck in a loop
    visitedcities.append(initialState)
    stack.append(Node(initialState, getId(initialState), None, "yes", 0))

    while len(stack) != 0:  # stack not empty

        if len(found) == len(goals):  # all goals found
            break
            # return len(found), len(visitedcities), path, found

        parent = stack[-1].get_parent()
        path.append(stack[-1].get_cityname())
        current = stack.pop().get_city_id()

        if depth != 0:  # depth not exceeded
            counter = 0
            for i in range(len(distance[current])):
                if distance[current][i] != 0 and getName(
                        i) not in visitedcities:  # there is a way which is not visited before
                    visitedcities.append(getName(i))
                    stack.append(Node(getName(i), i, current, "yes", edge))
                    counter = counter + 1

            if counter != 0:
                depth = depth - 1
            elif counter == 0 and depth == 0:  # search for city with children
                path.append(stack[-1].get_cityname())
                current = stack.pop().get_city_id()
                # for ind in range(len(stack)):
                # print(stack[ind].get_cityname())

                while stack[-1].get_parent() == parent:

                    for i in range(len(distance[current])):
                        if distance[current][i] != 0 and getName(i) not in visitedcities:
                            visitedcities.append(getName(i))
                            stack.append(Node(getName(i), i, current, "yes", edge))
                depth = 0
            edge = edge + 1

        if depth == 0:
            while counter != 0:
                childname = stack.pop().get_cityname()
                if len(found) != len(goals):
                    # print("childname ", childname)
                    path.append(childname)
                if childname in goals and childname not in found:
                    found.append(childname)
                counter = counter - 1

        if len(stack) != 0:
            name = stack[-1].get_cityname()
            id = stack[-1].get_parent()
            if name in goals and name not in found:
                path.append(name)
                found.append(name)
            if id == getId(initialState):
                depth = temp - 1
                edge = 1
            else:
                depth = temp - edge

    return len(found), len(visitedcities), path, found


def optimalway(s, g):
    go = []
    global ss
    for x in range(len(listofnodes)):
        if s == listofnodes[x].cityname:
            s = listofnodes[x].city_id
    ss = s
    for gg in g:
        for xx in range(len(listofnodes)):
            if gg == listofnodes[xx].cityname:
                go.append(listofnodes[xx].city_id)

    answer = []
    fringe = []
    fringe.append([0, s, listofnodes[s].cityname, 0])
    visited = []

    fringe = sorted(fringe)
    p = fringe[0]
    del fringe[0]

    while (p[1] not in go):
        visited.append(p[1])
        if (len(go) == 0):
            break
        # print("p[1]",p[1])

        ind = 0
        for i in range(len(cost[p[1]])):
            if cost[p[1]][i] > 0 and (listofnodes[ind].city_id not in visited):
                fringe.append([(cost[p[1]][i] + p[0] + hcost[p[1]][i]), listofnodes[ind].city_id,
                               (p[2]) + "-->" + listofnodes[ind].cityname, 1, hcost[p[1]][i]])

            ind = ind + 1

        # print("unsorted",fringe)
        fringe = sorted(fringe)
        # print("unsorted", fringe)
        for n in range(len(fringe)):
            if fringe[n][3] == 1:
                fringe[n][0] = fringe[n][0] - fringe[n][4]

        for m in range(len(fringe)):
            fringe[m][3] = 0

        # print("sorted", fringe)
        # print("visited",visited)
        p = fringe[0]
        del fringe[0]
        answer.append(p)
        if (p[1] in go):
            visited.append(p[0])
            go.remove(p[1])
            # print("goals", go)
            # print("done!!", fringe)
            # print("path", answer)
            if (len(go) == 0):
                print("the optimal way distance is :", answer[len(answer) - 1][0], "\nthe path to the goal node",
                      answer[len(answer) - 1][2])
                # print("fring",fringe)
                # print("visited",visited)
                # print("vtemp",vtemp)
            fringe = []
            visited = []
            answer = []


def greedy(s, g):
    go = []
    global ss
    for x in range(len(listofnodes)):
        if s == listofnodes[x].cityname:
            s = listofnodes[x].city_id
    ss = s
    for gg in g:
        for xx in range(len(listofnodes)):
            if gg == listofnodes[xx].cityname:
                go.append(listofnodes[xx].city_id)

    answer = []
    fringe = []
    fringe.append([0, s, listofnodes[s].cityname, 0])
    visited = []

    fringe = sorted(fringe)
    p = fringe[0]
    del fringe[0]

    while (p[1] not in go):
        visited.append(p[1])
        if (len(go) == 0):
            break
        # print("p[3]",p[3])

        ind = 0
        for i in range(len(hcost[p[1]])):
            if hcost[p[1]][i] > 0 and (listofnodes[ind].city_id not in visited):
                fringe.append(
                    [(p[0] + hcost[p[1]][i]), listofnodes[ind].city_id, p[2] + "-->" + listofnodes[ind].cityname,
                     cost[p[1]][i] + p[3]])

            ind = ind + 1

        # print("unsorted",fringe)
        fringe = sorted(fringe)
        # print("sorted", fringe)
        # print("visited",visited)
        p = fringe[0]
        del fringe[0]
        answer.append(p)
        if (p[1] in go):
            visited.append(p[0])
            go.remove(p[1])
            # print("goals", go)
            # print("done!!", fringe)
            # print("path", answer)
            if (len(go) == 0):
                print("Greedy search heuristic distance is :", answer[len(answer) - 1][0], "\nThe real distance is",
                      answer[len(answer) - 1][3], "\nthe path to the goal node", answer[len(answer) - 1][2])
                # print("fring",fringe)
                # print("visited",visited)
                # print("vtemp",vtemp)
            fringe = []
            visited = []
            answer = []


def ucl(s, g):
    go = []
    global ss
    for x in range(len(listofnodes)):
        if s == listofnodes[x].cityname:
            s = listofnodes[x].city_id
    ss = s
    for gg in g:
        for xx in range(len(listofnodes)):
            if gg == listofnodes[xx].cityname:
                go.append(listofnodes[xx].city_id)

    answer = []
    fringe = []
    fringe.append([0, s, listofnodes[s].cityname])
    visited = []

    fringe = sorted(fringe)
    p = fringe[0]
    del fringe[0]

    while (p[1] not in go):
        visited.append(p[1])
        if (len(go) == 0):
            break
        # print("p[1]",p[1])

        ind = 0
        for i in cost[p[1]]:
            if i > 0 and (listofnodes[ind].city_id not in visited):
                fringe.append([(i + p[0]), listofnodes[ind].city_id, (p[2]) + "-->" + listofnodes[ind].cityname])

            ind = ind + 1

        # print("unsorted",fringe)
        fringe = sorted(fringe)
        # print("sorted", fringe)
        # print("visited",visited)
        p = fringe[0]
        del fringe[0]
        answer.append(p)
        if (p[1] in go):
            visited.append(p[0])
            go.remove(p[1])
            # print("goals", go)
            # print("done!!", fringe)
            # print("path", answer)
            if (len(go) == 0):
                print("Uniform cost search:the distance is :", answer[len(answer) - 1][0],
                      "\nthe path to the goal node", answer[len(answer) - 1][2])
                # print("fring",fringe)
                # print("visited",visited)
                # print("vtemp",vtemp)
            fringe = []
            visited = []
            answer = []


def breadth(s, g):
    go = []
    global ss
    for x in range(len(listofnodes)):
        if s == listofnodes[x].cityname:
            s = listofnodes[x].city_id
    ss = s
    for gg in g:
        for xx in range(len(listofnodes)):
            if gg == listofnodes[xx].cityname:
                go.append(listofnodes[xx].city_id)

    answer = []
    fringe = []
    fringe.append([1, s, listofnodes[s].cityname,0])
    visited = []

    fringe = sorted(fringe)
    p = fringe[0]
    del fringe[0]

    while (p[1] not in go):
        visited.append(p[1])
        if (len(go) == 0):
            break
        # print("p[1]",p[1])

        ind = 0
        for i in cost[p[1]]:
            if i > 0 and (listofnodes[ind].city_id not in visited):
                fringe.append([1, listofnodes[ind].city_id, (p[2]) + "-->" + listofnodes[ind].cityname,(i + p[3])])

            ind = ind + 1

        # print("unsorted",fringe)
        fringe = sorted(fringe)
        # print("sorted", fringe)
        # print("visited",visited)
        p = fringe[0]
        del fringe[0]
        answer.append(p)
        if (p[1] in go):
            visited.append(p[0])
            go.remove(p[1])
            # print("goals", go)
            # print("done!!", fringe)
            # print("path", answer)
            if (len(go) == 0):
                print("Breadth search:the distance is :", answer[len(answer) - 1][3],
                      "\nthe path to the goal node", answer[len(answer) - 1][2])
                # print("fring",fringe)
                # print("visited",visited)
                # print("vtemp",vtemp)
            fringe = []
            visited = []
            answer = []


start = input("enter the start node ")
e = int(input("enter how many goals "))
goals = []
for i in range(e):
    g = input("enter the goal ")
    goals.append(g)

listofnodes = []
fhand = open("cities.txt")
cost = []
hcost = []
id = 0
for i in fhand:
    i = i.rstrip()
    n = i.split(":")
    n = n[0]
    listofnodes.append(Node(n.lower(), id, None, None, None))
    id = id + 1
    i = i.split(":")
    i = i[1]
    i = i.split(",")
    temp = []
    htemp = []
    for j in range(0, len(i), 2):
        temp.append(int(i[j]))
        htemp.append(int(i[j + 1]))
    cost.append(temp)
    hcost.append(htemp)
names = []
for i in listofnodes:
    names.append(i.cityname)

while start not in names:
    print(start, "not a city")
    start = input("enter the start node again ")
for i in goals:
    if i not in names:
        print(i, "not a city")
        goals.remove(i)
if len(goals) == 0:
    print("no goals")
    exit()

while True:
    x = int(input(
        "************\nenter the algorithem \n1.For the optimal way\n2.For Uniform cost search\n3.For iterative Deepening\n4.For Greedy search\n5.For Breadth search\n6.exit\n************\n"))
    if x == 1:
        optimalway(start, goals)
    if x == 2:
        ucl(start, goals)
    if x == 3:
        dic = {}
        for k in range(len(listofnodes)):
            dic[k] = listofnodes[k].get_cityname()
        goalspath = []
        for g in goals:
            if g.lower() == start.lower():
                goalspath.append(g)
                goals.remove(g)

        paths = []
        if len(goalspath) != 0:
            paths.append(goalspath)

        level = int(1)
        visitedcities = 0  # root will be incremented later
        numofgoals = len(goals)

        while visitedcities != len(listofnodes):  # check if levels ends
            flag, visitedcities, path, found = DFS(level, listofnodes, cost, start, goals)
            level = level + 1
            # print(path)
            if flag == numofgoals:  # all goals found
                break

        printed = []
        print("iterative deepening path is: ")
        if len(goalspath) != 0:
            for city in goalspath:
                print(city, end="->")
                printed.append(city)
        for index in range(len(path)):
            if path[index] not in printed:
                if index == len(path) - 1:
                    print(path[index])
                    printed.append(path[index])
                else:
                    print(path[index], end="->")
                    printed.append(path[index])
        if len(found) != len(goalspath) + len(goals):
            for city in goals:
                if city not in found:
                    print(city, "not found")
    if x == 4:
        greedy(start, goals)
    if x == 5:
        breadth(start,goals)
    if x == 6:
        exit()
