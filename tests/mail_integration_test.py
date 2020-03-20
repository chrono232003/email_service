import unittest

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))

import Send_Email
import email_data

class TestEmailServices(unittest.TestCase):

    test_data = {
        "email_content_success":{
        "email_body": "This is a sample of a successful email body",
        "email_subject": "Hello, how are you?",
        "recipient_email": "chrono232003@yahoo.com",
        "recipient_name": "Rec Mcgee",
        "sender_email": "info@greatoldgames.com",
        "sender_name": "Lance Test"
        },
        "email_content_fail":{
        "email_body": "This is a \\ /sample of a successful email body][\\]",
        "email_subject": "Hello, \\/:][how are you?",
        "recipient_email": "test2",
        "recipient_name": "Rec Mcgee %",
        "sender_email": "test@.$test.com",
        "sender_name": "Sender ./"
        }
    }

    #globally declare email and test_data classes
    data = email_data.Data(test_data['email_content_success'])
    email = Send_Email.Send_Email(data)

    def test_mail_gun_success(self):
        self.assertEqual(self.email.send_via_mail_gun()['status_code'], 200)
        self.assertEqual(self.email.send_via_mail_gun()['message'], "Queued. Thank you.")

    # def test_sendgrid_success(self):
    #     self.assertEqual(self.email.send_via_sendgrid()['status_code'], 202)


if __name__ == '__main__':
    unittest.main()
