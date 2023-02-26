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
        self.user_name = ['John', 'Mary','Thomas','Jane']

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        #TODO
        print("start set_name test")
        self.user_id.append(self.students.set_name('John'))
        self.user_id.append(self.students.set_name('Mary'))
        self.user_id.append(self.students.set_name('Thomas'))
        self.user_id.append(self.students.set_name('Jane'))
        
        self.assertEqual(0,self.user_id[0])
        self.assertEqual(1,self.user_id[1])
        self.assertEqual(2,self.user_id[2])
        self.assertEqual(3,self.user_id[3])

        print(f'{self.user_id[0]} {self.user_name[0]}')
        print(f'{self.user_id[1]} {self.user_name[1]}')
        print(f'{self.user_id[2]} {self.user_name[2]}')
        print(f'{self.user_id[3]} {self.user_name[3]}')
        print('Finish set_name test')
    # test case function to check the Students.get_name function
    def get_mex(self):
        mex = -1
        for item in enumerate(self.user_id):
            if mex < item[1]:
                mex = item[1]
        mex = mex + 1
        return mex
        
    def test_1_get_name(self):

        print('start get_name test')
        print(f'user_id length =  {len(self.user_id)}')
        print(f'user_name length =  {len(self.user_name)}')
        mex = self.get_mex()
        for id in self.user_id:
            print(f'id {id} {self.user_name[id]}')
        print(f'id {mex} {self.students.get_name(mex)}')
        #TODO
        self.assertEqual(self.students.get_name(0), self.user_name[0])
        self.assertEqual(self.students.get_name(1), self.user_name[1])
        self.assertEqual(self.students.get_name(2), self.user_name[2])
        self.assertEqual(self.students.get_name(3), self.user_name[3])
        # Test getting an invalid student
        
        self.assertEqual(self.students.get_name(mex), 'There is no such user')


if __name__ == '__main__':# pragma: no cover
    unittest.main(verbosity = 2)
   


