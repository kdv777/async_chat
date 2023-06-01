import unittest
import json

from common.variables import USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING, BAD_REQUEST, GOOD_REQUEST
from common.utils import get_message, send_message


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class Tests(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.BAD_REQUEST = BAD_REQUEST
        self.GOOD_REQUEST = GOOD_REQUEST

    test_dict = {
        ACTION: PRESENCE,
        TIME: 22222.22222,
        USER: {
            ACCOUNT_NAME: 'test_user'
        }
    }

    def test_send_message(self):
        test_socket = TestSocket(self.test_dict)
        send_message(test_socket, self.test_dict)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):
        test_sock_ok = TestSocket(self.GOOD_REQUEST)
        test_sock_err = TestSocket(self.BAD_REQUEST)
        self.assertEqual(get_message(test_sock_ok), self.GOOD_REQUEST)
        self.assertEqual(get_message(test_sock_err), self.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()
