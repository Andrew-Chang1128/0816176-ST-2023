import unittest
from Students import Students

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

        result = self.students.set_name('John')
        for user in enumerate(self.user_id):
            # print(f'result: {result}, user id in user list:{user[1]}')
            self.assertNotEqual(user[1],result)
        self.user_id.append(result)
        result = self.students.set_name('Mary')
        for user in enumerate(self.user_id):
            # print(f'result: {result}, user id in user list:{user[1]}')
            self.assertNotEqual(user[1],result)
        self.user_id.append(result)
        result = self.students.set_name('Thomas')
        for user in enumerate(self.user_id):
            # print(f'result: {result}, user id in user list:{user[1]}')
            self.assertNotEqual(user[1],result)
        self.user_id.append(result)
        result = self.students.set_name('Jane')
        for user in enumerate(self.user_id):
            # print(f'result: {result}, user id in user list:{user[1]}')
            self.assertNotEqual(user[1],result)
        self.user_id.append(result)
   
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
        # print(f'mex:  {mex}')
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


if __name__ == '__main__':
    unittest.main() # pragma: no cover
else:# pragma: no cover
    pass
   


