import user
import infections
import sys

users = []
def info_printer(user):
    print 'Name:'
    print user.get_name()
    print 'Id:'
    print len(users) - 1
    print 'Status:'
    print user.get_status()

for line in sys.stdin:
    words = line.split()
    command = words[0].lower()
    if command == 'add':
        new_user = user.User(words[1])
        users.append(new_user)
        info_printer(new_user)
    elif command == 'coach':
        user1 = users[int(words[1])]
        user2 = users[int(words[2])]
        user1.add_student(user2)
        action = user1.get_name() + 'coaches' + user2.get_name()
        print action
    elif command == 'get':
        user = users[int(words[1])]
        info_printer(user)
    elif command == 'total_infection':
        user = users[int(words[1])]
        if infections.total_infection(user):
            print 'Infection Successful'
        else:
            print 'Infection Failed'
    elif command == 'limited_infection':
        user = users[int(words[1])]
        num = int(words[2])
        if infections.limited_infection(user, num):
            print 'Infection Successful'
        else:
            print 'Infection Failed'
    elif command == 'exact_infection':
        user = users[int(words[1])]
        num = int(words[2])
        if infections.exact_infection(user, num):
            print 'Infection Successful'
        else:
            print 'Infection Failed'
    else:
        print 'Invalid Command'

