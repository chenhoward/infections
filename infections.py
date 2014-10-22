from user import User

def total_infection(user):
    """
    Infects the whole connected graph of the user.
    Returns True if infection occurs.

    user -- A user object.
    """
    def always_true(visited):
        return True

    def visit(user):
        user.infect()

    def add_to_fringe(user, fringe):
        students = user.get_students()
        coaches = user.get_coaches()
        connections = list(students.union(coaches))
        fringe += connections

    graph_search(user, always_true, visit, add_to_fringe, True)
    return True

def limited_infection(user, num):
    """
    Infects approximately num users.
    Returns True if any users are infected.

    user -- A user object.
    num -- the approximate number of users to be infected
    """
    if not num:
        return False

    count = [1]

    def add_to_fringe(user, fringe):
        if count[0] < num:
            coaches = user.get_coaches()
            fringe += list(coaches)
            count[0] += len(coaches)
        if count[0] < num:
            students = user.get_students()
            fringe += list(students)
            count[0] += len(students)
    graph_search(user, always_true, visit, add_to_fringe, False)
    return True

def exact_infection(starting_user, num):
    fringe = [starting_user]
    visited = set()
    while fringe:
        user = fringe.pop()
        if user not in visited:
            visited.add(user)
            students = user.get_students()
            coaches = user.get_coaches()
            connections = list(students.union(coaches))
            fringe += connections
    graph_size = len(visited)
    if len(visited) < num:
        return false
    elif len(visited) is num:
        for user in len(visited):
            user.infect()
    else:
        fringe = [starting_user]
        visited = set()
        while fringe and len(visited) <= num:
            user = fringe.pop()
            if user not in visited:
                visited.add(user)
                students = user.get_students()
                coaches = user.get_coaches()
                connections = list(students.union(coaches))
                fringe += connections

def graph_search(starting_user, cond, visit, add_to_fringe, stack = True):
    fringe = [starting_user]
    visited = set()
    while fringe and cond(visited):
        if stack:
            user = fringe.pop()
        else:
            user = fringe.pop(0)
        if user not in visited:
            visit(user)
            add_to_fringe(user, fringe)
            visited.add(user)

def always_true(visited):
    return True

def visit(user):
    user.infect()

