import unittest
from user import User

class UserTest(unittest.TestCase):

    def test_user_creation(self):
        u = User('A')
        self.assertEqual(u.get_name(), 'A')
        self.assertEqual(u.get_status(), 'Clean')
        v = User('B')
        u.add_student(v)
        self.assertTrue(v in u.get_students())

    def test_user_add(self):
        a = User()
        b = User()
        c = User()
        d = User()
        a.add_student(b)
        b.add_coach(c)
        c.add_students([d])
        c.add_students([d])
        self.assertEqual(a.get_num_students(), 1)
        self.assertEqual(c.get_num_students(), 2)
        self.assertEqual(b.get_num_coaches(), 2)
        self.assertEqual(d.get_num_coaches(), 1)

    def test_user_infect(self):
        a = User()
        a.infect()
        self.assertEqual(a.get_status(), 'Infected')
        b = User(None, a)
        self.assertEqual(b.get_status(), 'Infected')

if __name__ == '__main__':
    unittest.main()
