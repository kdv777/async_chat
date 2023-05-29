import unittest

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, PRESENCE, TIME, USER, BAD_REQUEST
from server import process_client_message


class TestServerFunction(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.BAD_REQUEST = BAD_REQUEST

    def test_user_unknown(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.BAD_REQUEST)

    def test_action_unknown(self):
        self.assertEqual(process_client_message(
            {ACTION: 'unknown', TIME: '1.0', USER: {ACCOUNT_NAME: 'Guest'}}), self.BAD_REQUEST)

    def test_no_action(self):
        self.assertEqual(process_client_message(
            {TIME: '1.0', USER: {ACCOUNT_NAME: 'Guest'}}), self.BAD_REQUEST)

    def test_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.BAD_REQUEST)

    def test_all_right(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}}), {RESPONSE: 200})


if __name__ == '__main__':
    unittest.main()
