import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import process_email
import const

import unittest


class TestFieldValidations(unittest.TestCase):
    # globally declare the validation and test_data classes
    test_data_scenarios = {
        "email_content_success": {
            "body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "subject": "Hello, how are you?",
            "to": "test@gmail.com",
            "to_name": "Test Testerson",
            "from": "okay@gmail.com.com",
            "from_name": "Sender Mcgee"
        },
        "email_content_fail_email": {
            "body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "subject": "Testing the subject line!",
            "to": "test!@@gmail.com",
            "to_name": "Lance",
            "from": "test@test.com",
            "from_name": "Dan Fuller"
        },
        "email_content_fail_name": {
            "body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "subject": "Hello, how are you?",
            "to": "test@gmail.com",
            "to_name": "Rec/Mcgee",
            "from": "test@test.com",
            "from_name": "Sender Mcgee"
        },
        "email_content_fail_subject": {
            "body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "subject": "This@@is /\Spam",
            "to": "test@gmail.com",
            "to_name": "Rec Mcgee",
            "from": "test@test.com",
            "from_name": "Sender Mcgee"
        },
        "email_content_fail_body": {
            "body": "<h1\\>This is a title section</h1>#$<div><p>This is a sample of a successful email body<p></div>",
            "subject": "Hello how are you",
            "to": "test@gmail.com",
            "to_name": "Rec Mcgee",
            "from": "test@test.com",
            "from_name": "Sender Mcgee"
        }
    }

    def test_overall_process_success(self):
        proc = process_email.Process(self.test_data_scenarios['email_content_success'])
        self.assertTrue('Your Email was sent successfully' in proc.response())

    def test_process_fail_email(self):
        proc = process_email.Process(self.test_data_scenarios['email_content_fail_email'])
        self.assertEqual(proc.response(), 'Please enter a valid email.')

    def test_process_fail_name(self):
        proc = process_email.Process(self.test_data_scenarios['email_content_fail_name'])
        self.assertEqual(proc.response(), 'Please enter a valid name.')

    def test_process_fail_subject(self):
        proc = process_email.Process(self.test_data_scenarios['email_content_fail_subject'])
        self.assertEqual(proc.response(), 'Please enter a valid subject.')

    def test_process_fail_body(self):
        proc = process_email.Process(self.test_data_scenarios['email_content_fail_body'])
        self.assertEqual(proc.response(), 'Please enter a valid body.')

if __name__ == '__main__':
    unittest.main()
