import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
import field_validation

import unittest


class TestFieldValidations(unittest.TestCase):
    # globally declare the validation and test_data classes
    validation_obj = field_validation.Validation()
    test_data_scenarios = {
        "email_content_success": {
            "email_body": "This is a sample of a successful email body",
            "email_subject": "Hello, how are you?",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Test Testerson",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_email": {
            "email_body": "This is a sample of a successful email body",
            "email_subject": "Hello, how are you?",
            "recipient_email": "test!@@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_name": {
            "email_body": "This is a sample of a successful email body",
            "email_subject": "Hello how are you",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_subject": {
            "email_body": "This is a sample of a successful email body",
            "email_subject": "Hello how are you",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        },
        "email_content_fail_body": {
            "email_body": "This is a sample of a successful email body",
            "email_subject": "Hello how are you",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Rec Mcgee",
            "sender_email": "test@test.com",
            "sender_name": "Sender Mcgee"
        }
    }

    def test_overall_validation_success(self):
        self.assertTrue(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_success']))

    def test_validation_email_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_email']), "Please enter a valid email.")

    def test_validation_name_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_email']), "Please enter a valid email.")

    def test_validation_subject_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_email']), "Please enter a valid email.")

    def test_validation_body_fail(self):
        self.assertEqual(self.validation_obj.data_validates_successfully(self.test_data_scenarios['email_content_fail_email']), "Please enter a valid email.")

    # def test_email_validation_success(self):
    #     for email in self.test_data['emails_good']:
    #         self.assertTrue(self.val.email_is_valid(email))

    # def test_email_validation_fail(self):
    #     for email in self.test_data['emails_bad']:
    #         self.assertFalse(self.val.email_is_valid(email))
    #
    #
    # def test_name_validation_success(self):
    #     for name in self.test_data['names_good']:
    #         self.assertTrue(self.val.name_is_valid(name))
    #
    # def test_name_validation_fail(self):
    #     for name in self.test_data['names_bad']:
    #         self.assertFalse(self.val.name_is_valid(name))
    #
    #
    # def test_subject_validation_success(self):
    #     for subject in self.test_data['subjects_good']:
    #             self.assertTrue(self.val.subject_is_valid(subject))
    #
    # def test_subject_validation_fail(self):
    #     for subject in self.test_data['subjects_bad']:
    #         self.assertFalse(self.val.subject_is_valid(subject))

    #
    # def test_body_validation_success(self):
    #     self.assertFalse(self.val.validate_body(self.email_content_success['email_body']))
    #
    # def test_body_validation_fail(self):
    #     self.assertFalse(self.val.validate_body(self.email_content_fail['email_body']))
    #
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
