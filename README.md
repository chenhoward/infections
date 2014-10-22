Infections
==========

Project for Khan Academy.

In user.py we have the User class to model a user

In infections.py we have the 3 types of infections, the total, limited, and exact.

In unit_test.py we have unit test for the user class and the infection functions.

To use the project, one can run run.py, which takes in from standard input.

Each command is in this format:

command arg0 arg1

Where command is the name of the command and arg0 and arg 1 are arguments for the command.  The commands are not case
sensitive.  There is also no error handling for the wrong number or type of arguments.

The commands are:

add

coach

get

total_infection

limited_infection

exact_infection


Guide:

add: a 1 argument command where arg0 is the name of the User that will be created.
Prints out their information.  Gives user an Id.


coach: a 2 argument command where arg0 is the Id of the User that will coach the user with the Id arg1.

get: a 1 argument command where arg0 is the Id of the User we want to get information about.

total_infection: a 1 argument function where arg0 is the Id of the User we want to infect.

limited_infection: a 2 argument function where arg0 is the Id of the User we want to infect and arg1 is the
approximate number.

total_infection: a 2 argument function where arg0 is the Id of the User we want to infect and arg1 is the exact
number we want to infect.

Extra information:

limited infection:  I spread the infection by dividing the students and coaches of a User and adding the sets with coaches
being first until it past the target number, then we stop adding these sets of Users to the fringe of the graph
search.  I added them in sets to keep a sense of uniformness while I made propagating the infeciton upward a priority
because the people who are coaching should be more adept in general at reacting to change.  Worst case is if we start
at a User who is coached by the rest or most of the Users which means we add all the coaches of the current User we 
are looking at.

exact infection:  Did a BFS until the number of people that need to be infected are infected.  That keeps anyone who is
infected close to the others, which would match the shape of infection we would like to keep.  It also checks to see if
there are enough Users to infect first.
