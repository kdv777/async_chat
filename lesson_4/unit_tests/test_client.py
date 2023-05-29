import unittest
from common.variables import ACTION, PRESENCE, TIME, TYPE, STATUS, USER, ACCOUNT_NAME, RESPONSE, ERROR
from client import create_presence, process_ans


class TestClientFunction(unittest.TestCase):

    def test_create_presence(self):
        test_presence = create_presence()
        test_presence[TIME] = 1.0
        self.assertEqual(test_presence, {
            ACTION: PRESENCE,
            TIME: 1.0,
            TYPE: STATUS,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        })

    def test_responce(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

    def test_process_ans_200(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_ans_400(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')


if __name__ == '__main__':
    unittest.main()
