import requests
import os, sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import const

load_dotenv()

# send the actual email once all the validations are met.
class Send_Email:
    MAIL_GUN_API_KEY = os.getenv('MAIL_GUN_API_KEY')
    SEND_GRID_API_KEY = os.getenv('SEND_GRID_API_KEY')

    SEND_GRID_ENDPOINT = os.getenv('SEND_GRID_ENDPOINT')
    MAIL_GUN_ENDPOINT = os.getenv('MAIL_GUN_ENDPOINT')

    DEFAULT_MAIL_SERVICE = os.getenv('MAIL_SERVICE_PROVIDER')

    def __init__(self, data):
        self.data = data

        self.email_service_obj = {
            "mailgun": {
                "service": self.send_via_mail_gun(),
                "success_code": const.MAIL_GUN_SUCCESS_CODE,
                "success_response": const.SUCCESS_MESSAGE_TO_USER_MAIL_GUN
            },
            "sendgrid": {
                "service": self.send_via_sendgrid(),
                "success_code": const.SEND_GRID_SUCCESS_CODE,
                "success_response": const.SUCCESS_MESSAGE_TO_USER_SEND_GRID
            }
        }

    def send_via_mail_gun(self):
        try:
            mail_data = {
                "url": self.MAIL_GUN_ENDPOINT,
                "auth": ("api", self.MAIL_GUN_API_KEY),
                "body": {"from": self.data.get_from_name() + " " + "<" + self.data.get_from_email() + ">",
                         "to": [self.data.get_to_name(), self.data.get_to_email()],
                         "subject": self.data.get_subject(),
                         "text": self.data.get_body()}
            }
            resp = requests.post(mail_data["url"], auth=mail_data["auth"], data=mail_data["body"])

            return {
                "status_code": resp.status_code,
                "message": resp.json()['message']
            }
        except Exception as e:
            return const.TECHNICAL_ERROR_MESSAGE

    def send_via_sendgrid(self):
        try:
            mail_data = {
                "url": self.SEND_GRID_ENDPOINT,
                "headers": {'Authorization': 'Bearer ' + self.SEND_GRID_API_KEY},
                "body": {
                    "personalizations": [
                        {
                            "to": [
                                {
                                    "name": self.data.get_to_name(),
                                    "email": self.data.get_to_email()
                                }
                            ],
                            "subject": self.data.get_subject()
                        }
                    ],
                    "from": {
                        "name": self.data.get_from_name(),
                        "email": self.data.get_from_email()
                    },
                    "content": [
                        {
                            "type": "text/plain",
                            "value": self.data.get_body()
                        }
                    ]
                }
            }

            resp = requests.post(mail_data["url"], json=mail_data["body"], headers=mail_data["headers"])

            return {
                "status_code": resp.status_code
            }
        except Exception as e:
            return const.TECHNICAL_ERROR_MESSAGE

    def send_email(self):
        try:
            service = self.email_service_obj[self.DEFAULT_MAIL_SERVICE]
            response = service['service']
            if response['status_code'] == service['success_code']:
                return service["success_response"]
            else:
                return const.EMAIL_FAILED_TO_SEND_MESSAGE

        # technical error on our end
        except Exception as e:
            return const.TECHNICAL_ERROR_MESSAGE + str(e)
