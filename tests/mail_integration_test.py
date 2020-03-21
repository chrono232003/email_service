import unittest

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))

import Send_Email
import email_data

class TestEmailServices(unittest.TestCase):


    test_email_content = {
    "email_body": "<h1>Hi there!<h1><p>This is a sample of a successful email body</p>",
    "email_subject": "Hello, how are you?",
    "recipient_email": "chrono232003@yahoo.com",
    "recipient_name": "Rec Mcgee",
    "sender_email": "chrono232003@yahoo.com",
    "sender_name": "Lance Test"
    }


    #globally declare email and test_data classes
    data = email_data.Data(test_email_content)
    email = Send_Email.Send_Email(data)

    def test_mail_gun_success(self):
        self.assertEqual(self.email.send_via_mail_gun()['status_code'], 200)
        self.assertEqual(self.email.send_via_mail_gun()['message'], "Queued. Thank you.")

    def test_sendgrid_success(self):
        self.assertEqual(self.email.send_via_sendgrid()['status_code'], 202)


if __name__ == '__main__':
    unittest.main()
