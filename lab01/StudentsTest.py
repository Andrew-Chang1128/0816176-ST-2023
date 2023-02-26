import unittest
from Students import Students
# import sys
# sys.path.append('../lab1')

class Test(unittest.TestCase):
    students = Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []
    def setUp(self):
        self.students = Students()

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        #TODO
        self.assertEqual(self.students.set_name('John'),0)
        self.assertEqual(self.students.set_name('Mary'),1)
        self.assertEqual(self.students.set_name('Thomas'),2)
        self.assertEqual(self.students.set_name('Jane'),3)
    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        #TODO
        self.assertEqual(self.students.get_name(0), 'John')
        self.assertEqual(self.students.get_name(1), 'Mary')
        self.assertEqual(self.students.get_name(2), 'Thomas')
        self.assertEqual(self.students.get_name(3), 'Jane')
        # Test getting an invalid student
        self.assertEqual(self.students.get_name(4), 'There is no such user')

if __name__ == '__main__':# pragma: no cover
    unittest.main(verbosity = 2)


