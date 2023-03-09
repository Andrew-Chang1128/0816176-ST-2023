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

    @patch('app.MailSystem.write')
    @patch('app.MailSystem.send')
    @patch('app.Application.get_random_person', side_effect = ["William", "Oliver", "Henry", "Liam"])
    def test_app(self, mockGetRandomPerson, mockSend, mockWrite):
        # Mock Send function by creating a new func and assign it to side effect of Mocksend
        def mockSend_side_effect(*args, **kwargs):
            print(args[1])
        mockSend.side_effect = mockSend_side_effect
        # mock get_random_person func which will be called by select_next_person
        nextPerson = self.App.select_next_person()
        self.assertEqual(nextPerson, 'Liam')
        print(f'{nextPerson} selected!')
        self.App.notify_selected()
        self.assertEqual(mockSend.call_count,4)
        self.assertEqual(mockWrite.call_count,4)
        pass


if __name__ == "__main__":
    unittest.main()
