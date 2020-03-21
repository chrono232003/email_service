import unittest

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))

import send_email
import email_data_model

class TestEmailServices(unittest.TestCase):


    test_email_content = {
    "body": "<h1>Hi there!<h1><p>This is a sample of a successful email body</p>",
    "subject": "Hello, how are you?",
    "to": "chrono232003@yahoo.com",
    "to_name": "Rec Mcgee",
    "from": "chrono232003@yahoo.com",
    "from_name": "Lance Test"
    }


    #globally declare email and test_data classes
    data = email_data_model.Data(test_email_content)
    email = send_email.Send_Email(data)

    def test_mail_gun_success(self):
        self.assertEqual(self.email.send_via_mail_gun()['status_code'], 200)
        self.assertEqual(self.email.send_via_mail_gun()['message'], "Queued. Thank you.")

    def test_sendgrid_success(self):
        self.assertEqual(self.email.send_via_sendgrid()['status_code'], 202)


if __name__ == '__main__':
    unittest.main()
