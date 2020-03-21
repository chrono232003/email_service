import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import field_validation
import const

import unittest


class TestFieldValidations(unittest.TestCase):
    # globally declare the validation and test_data classes
    validation_obj = field_validation.Validation()
    test_data_scenarios = {
        "email_content_success": {
            "email_body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "Hello, how are you?",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Test Testerson",
            "sender_email": "okay@gmail.com.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_email": {
            "email_body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "Testing the subject line!",
            "recipient_email": "test!@@gmail.com",
            "recipient_name": "Lance",
            "sender_email": "test@test.com",
            "sender_name": "Dan Fuller"
        },
        "email_content_fail_name": {
            "email_body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "Hello, how are you?",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec/Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_subject": {
            "email_body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "This@@is /\Spam",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_body": {
            "email_body": "<h1\\>This is a title section</h1>#$<div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "Hello how are you",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        }
    }

    def test_overall_validation_success(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_success']), 'Valid')

    def test_validation_email_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_email']), const.VALIDATION_FAIL_EMAIL_STRING)

    def test_validation_name_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_name']), const.VALIDATION_FAIL_NAME_STRING)

    def test_validation_subject_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_subject']), const.VALIDATION_FAIL_SUBJECT_STRING)

    def test_validation_body_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_body']), const.VALIDATION_FAIL_BODY_STRING)

if __name__ == '__main__':
    unittest.main()
