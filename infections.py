from user import User

def total_infection(user):
    """
    Infects the whole connected graph of the user.
    Returns True if infection occurs.

    user -- A user object.
    """

    graph_search(user, always_true, visit, add_to_fringe)
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

    def add_to_fringe_upwards(user, fringe):
        """
        The add_to_fringe function for the generalized graph_search
        that will update the fringe for the limited_infection.

        user -- User whose neighbors we are adding to the fringe
        fringe -- List of Users to explore
        """
        if count[0] < num:
            coaches = user.get_coaches()
            fringe += list(coaches)
            count[0] += len(coaches)
        if count[0] < num:
            students = user.get_students()
            fringe += list(students)
            count[0] += len(students)

    graph_search(user, always_true, visit, add_to_fringe_upwards, False)
    return True

def exact_infection(starting_user, num):
    """
    Infects exactly num users starting from starting_user.  Returns
    True if it succeeds, else we did not find enough users so no User
    is infected.

    starting_user -- the User object that is the origin of the infection
    num -- the number of Users infected if there are enough Users.
    """

    def upper_bound_cond(visited):
        """
        A cond for exact_infection to be used in the graph_search
        algorithm.  Returns true if the size of visited is less
        than the num given in the exact_infection arguments.

        visited -- visited User set
        """
        return len(visited) < num

    empty = lambda x: x
    visited = graph_search(starting_user, upper_bound_cond, empty, add_to_fringe, False)
    if len(visited) is num:
        for user in list(visited):
            user.infect()
        return True
    else:
        return False


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
    """
    A generalized graph search.  Returns the set of visited Users.

    starting_user -- The user we are starting on
    cond -- condition we continue the search that is a function
            that takes in the visited set
    visit -- function used when visiting the node
    add_to_fringe -- function that takes in the User being explored and
                     the fringe to determine what should be added to
                     the fringe
    stack -- True if we want our fringe to act as a stack
    """
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
    return visited

def always_true(visited):
    """
    Returns True always for the cond in graph_search

    visited -- set of visited users
    """
    return True

def visit(user):
    """
    Infects the user for the visit in graph_search

    user -- User currently being infected
    """
    user.infect()

def add_to_fringe(user, fringe):
    """
    Add's anything related to the user to the fringe.

    user -- User the search is visiting
    fringe -- a list of Users to be explored
    """
    students = user.get_students()
    coaches = user.get_coaches()
    connections = list(students.union(coaches))
    fringe += connections
