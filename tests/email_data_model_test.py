import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import email_data_model
import const

import unittest


class TestFieldValidations(unittest.TestCase):
    # globally declare the validation and test_data classes
    test_data_scenarios = {
        "data_content_success": {
            "email_body": "<h1>This is a title section</h1><div><p>This is a sample of a successful email body<p></div>",
            "email_subject": "Hello, how are you?",
            "recipient_email": "test@gmail.com",
            "recipient_name": "Test Testerson",
            "sender_email": "okay@gmail.com",
            "sender_name": "Sender Mcgee"
        }
    }

    def test_data_model_success(self):
        data_model = email_data_model.Data(self.test_data_scenarios['data_content_success'])
        self.assertEqual(data_model.get_to_email(), "test@gmail.com")
        self.assertEqual(data_model.get_to_name(), "Test Testerson")
        self.assertEqual(data_model.get_from_email(), "okay@gmail.com")
        self.assertEqual(data_model.get_from_name(), "Sender Mcgee")
        self.assertEqual(data_model.get_subject(), "Hello, how are you?")
        self.assertEqual(data_model.get_body(), "This is a title section This is a sample of a successful email body")


if __name__ == '__main__':
    unittest.main()
