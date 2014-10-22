from user import User

def total_infection(user):
    """
    Infects the whole connected graph of the user.

    user -- A user object.
    """
    if not user.get_status_num():
        user.infect()
        students = user.get_students()
        coaches = user.get_coaches()
        connections = list(students.union(coaches))
        for connection in connections:
            total_infection(connection)

def limited_infection(user, num):
    fringe = [user]
    visited = set()
    count = 1
    while fringe and num:
        user = fringe.pop(0)
        if user not in visited:
            visited.add(user)
            user.infect()
            if count < num:
                coaches = user.get_coaches()
                fringe = fringe + list(coaches)
                count += len(coaches)
            if count < num:
                students = user.get_students()
                fringe = fringe + list(students)
                count += len(students)
