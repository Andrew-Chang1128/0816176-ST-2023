import unittest
from unittest.mock import patch
from unittest.mock import Mock
import course_scheduling_system

class CSSTest(unittest.TestCase):

    def setUp(self):
        self.css = course_scheduling_system.CSS()

        pass

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_1(self, mockCourseExist):
        print("----------------------------test_q1_1----------------------------")
        mockCourseExist.return_value = (True)
        courseToAdd = ('Algorithms', 'Monday', 3, 4) 
        returnValue = self.css.add_course(courseToAdd)
        print(returnValue)
        self.assertTrue(returnValue)
        # self.assertFalse(returnValue)
        courseList = self.css.get_course_list()
        print(courseList)
        self.assertEqual(courseList[0], courseToAdd)
        # self.assertNotEqual(courseList[0], courseToAdd)

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_2(self, mockCourseExist):
        print("----------------------------test_q1_2----------------------------")
        mockCourseExist.return_value = (True)
        courseToAdd1 = ('Algorithms', 'Monday', 3, 4) 
        courseToAdd2 = ('Math', 'Monday', 3, 5) 
        returnValue1 = self.css.add_course(courseToAdd1)
        returnValue2 = self.css.add_course(courseToAdd2)
        print(returnValue1)
        print(returnValue2)
        self.assertTrue(returnValue1)
        self.assertFalse(returnValue2)
        courseList = self.css.get_course_list()
        print(courseList)
        self.assertEqual(courseList[0], courseToAdd1)

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_3(self, mockCourseExist):
        print("----------------------------test_q1_3----------------------------")
        mockCourseExist.return_value = (False)
        courseToAdd = ('Algorithms', 'Monday', 3, 4) 
        returnValue = self.css.add_course(courseToAdd)
        print(returnValue)
        self.assertFalse(returnValue)
        courseList = self.css.get_course_list()
        print(courseList)
        self.assertEqual(courseList, [])

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_4(self, mockCourseExist):
        print("----------------------------test_q1_4----------------------------")
        mockCourseExist.return_value = (True)
        courseToAdd = ('Algorithms', 'Monday', 3, 10) 
        with self.assertRaises(TypeError):
            returnValue = self.css.add_course(courseToAdd)

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_5(self, mockCourseExist):
        print("----------------------------test_q1_5----------------------------")
        mockCourseExist.return_value = (True)
        courseToAdd1 = ('Algorithms', 'Monday', 3, 4)
        courseToAdd2 = ('Algorithms', 'Tuesday', 3, 4)
        courseToAdd3 = ('Algorithms', 'Wednesday', 3, 4) 
        returnValue1 = self.css.add_course(courseToAdd1)
        returnValue2 = self.css.add_course(courseToAdd2)
        returnValue3 = self.css.add_course(courseToAdd3)
        print(returnValue1)
        print(returnValue2)
        print(returnValue3)
        self.assertTrue(returnValue1)
        self.assertTrue(returnValue2)
        self.assertTrue(returnValue3)
        courseList = self.css.get_course_list()
        print(courseList)
        self.assertEqual(courseList[0], courseToAdd1)
        self.assertEqual(courseList[1], courseToAdd2)
        self.assertEqual(courseList[2], courseToAdd3)
        self.css.remove_course(courseToAdd2)
        print("courseList after removing second class")
        courseList = self.css.get_course_list()
        print(courseList)
        self.assertEqual(courseList[0], courseToAdd1)
        self.assertEqual(courseList[1], courseToAdd3)
        print(self.css.__str__())
        print(f'call count {mockCourseExist.call_count}')
        self.assertEqual(mockCourseExist.call_count,4)

    # @patch('course_scheduling_system.CSS.check_course_exist')
    # def test_q1_7(self, mockCourseExist):
    #     print("----------------------------test_q1_7----------------------------")
    #     mockCourseExist.return_value = (False)
    #     courseToAdd = ('Algorithms', 'Monday', 3, 10)
    #     courseList = self.css.get_course_list()
    #     print(courseList)
    #     self.assertEqual(courseList, [])
        
if __name__ == "__main__":
    unittest.main()# pragma: no cover
else:# pragma: no cover
    pass
