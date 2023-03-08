import unittest
from unittest.mock import patch
from unittest.mock import Mock
import app

class ApplicationTest(unittest.TestCase):

    @patch('app.Application.get_names')
    def setUp(self, mockGetNames):
        # stub
        mockGetNames.return_value = (["William", "Oliver", "Henry", "Liam"], ["William", "Oliver", "Henry"])
        self.App = app.Application()
        print(f'people stubbed {self.App.people}, selected stubbed: {self.App.selected}')

        pass

    @patch('app.MailSystem.send')
    @patch('app.Application.get_random_person', side_effect = ["William", "Oliver", "Henry", "Liam"])
    def test_app(self, mockGetRandomPerson, mockSend):
        # spy on Sendmain function
        def mockSend_side_effect(*args, **kwargs):
            print(args[1])
        mockSend.side_effect = mockSend_side_effect
        # mock get random person
        nextPerson = self.App.select_next_person()
        self.assertEqual(nextPerson, 'Liam')
        print(f'{nextPerson} selected!')
        self.App.notify_selected()
        self.assertEqual(mockSend.call_count,4)
        pass


if __name__ == "__main__":
    unittest.main()
