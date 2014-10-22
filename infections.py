from user import User

def total_infection(user):
    """
    Infects the whole connected graph of the user.

    user -- A user object.
    """
    stack = [user]
    visited = set()
    while stack:
        current_user = stack.pop()
        current_user.infect()
        students = current_user.get_students()
        coaches = current_user.get_coaches()
        connections = list(students.union(coaches))
        for connection in connections:
            if connection not in visited:
                visited.add(connection)
                stack.append(connection)

