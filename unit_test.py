import unittest
from user import User
import infections

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

    def test_total_infection1(self):
        a = User()
        b = User()
        c = User()
        d = User()
        e = User()
        f = User()
        e.add_student(f)
        a.add_coach(b)
        b.add_student(c)
        d.add_student(a)
        self.assertEqual(a.get_status(), 'Clean')
        self.assertEqual(b.get_status(), 'Clean')
        self.assertEqual(c.get_status(), 'Clean')
        self.assertEqual(d.get_status(), 'Clean')
        self.assertEqual(e.get_status(), 'Clean')
        self.assertEqual(f.get_status(), 'Clean')
        infections.total_infection(a)
        self.assertEqual(a.get_status(), 'Infected')
        self.assertEqual(b.get_status(), 'Infected')
        self.assertEqual(c.get_status(), 'Infected')
        self.assertEqual(d.get_status(), 'Infected')
        self.assertEqual(e.get_status(), 'Clean')
        self.assertEqual(f.get_status(), 'Clean')
        infections.total_infection(f)
        self.assertEqual(e.get_status(), 'Infected')
        self.assertEqual(f.get_status(), 'Infected')

if __name__ == '__main__':
    unittest.main()
