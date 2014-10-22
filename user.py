class User:
    """
    Class that represents a User
    """

    def __init__(self, name = None, coach = None):
        """
        Initializes a user.

        name -- a string that is the name of the user
        coach -- a User that coaches this User.
        """
        self.name = name
        self.students = set()
        self.coaches = set()
        if not coach:
            self.status_num = 0
        else:
            self.status_num = coach.get_status_num()
            coach.add_student(self)

    def __repr__(self):
        return str(self.get_name())

    def get_name(self):
        """
        Returns the name of the User.
        """
        return self.name

    def get_students(self):
        """
        Returns a set of User objects which are the students of the User.
        """
        return self.students

    def get_num_students(self):
        """
        Returns the number of students this User has.
        """
        return len(self.get_students())

    def get_num_coaches(self):
        """
        Returns the number of coaches this User has.
        """
        return len(self.get_coaches())

    def get_coaches(self):
        """
        Returns a set of User objects which are the coaches of the User.
        """
        return self.coaches

    def get_status_num(self):
        """
        Returns the status_num of the User.
        """
        return self.status_num

    def get_status(self):
        """
        Returns the status of the User.  If status_num is 0
        then it returns 'Clean', else it returns 'Infected'
        """
        if not self.status_num:
            return 'Clean'
        else:
            return 'Infected'

    def add_student(self, student):
        """
        Add's a student of the User.

        student -- A User object that is the student of this User
        """
        self.students.add(student)
        student.get_coaches().add(self)

    def add_students(self, students):
        """
        Add's students of the User.

        students -- A set of User object that contain
                    the students of this User
        """
        for student in students:
          self.add_student(student)

    def add_coach(self, coach):
        """
        Add's a coach of the User.

        coach -- A User object who coaches this User
        """
        coach.add_student(self)

    def add_coaces(self, coaches):
        """
        Add's a coach of the User.

        coach -- A User object who coaches this User
        """
        for coach in coaches:
            coach.add_student(self)

    def infect(self):
        """
        Infects the User (sets status_num to 1)
        """
        self.status_num = 1

