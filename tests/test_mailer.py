import unittest

import mailer


class MailerTest(unittest.TestCase):
    def test_request_carries_the_note(self):
        req = mailer.build_request("ana@example.com", "Your note", "buy milk")
        self.assertIn(b"buy milk", req.data)


if __name__ == "__main__":
    unittest.main()
