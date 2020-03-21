import requests
import os, sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import const

load_dotenv()

class Send_Email:

        MAIL_GUN_API_KEY = os.getenv('MAIL_GUN_API_KEY')
        SEND_GRID_API_KEY = os.getenv('SEND_GRID_API_KEY')

        def __init__(self, data):
            self.data = data

            #list of mail service priority first to last
            self.email_service_obj = [
                {
                    "service": self.send_via_mail_gun(),
                    "success_code": const.MAIL_GUN_SUCCESS_CODE,
                    "success_response": const.SUCCESS_MESSAGE_TO_USER_MAIL_GUN
                },
                {
                    "service": self.send_via_sendgrid(),
                    "success_code": const.SEND_GRID_SUCCESS_CODE,
                    "success_response": const.SUCCESS_MESSAGE_TO_USER_SEND_GRID
                }
            ]

        def send_via_mail_gun(self):
            mail_data = {
            "url": "https://api.mailgun.net/v3/sandbox81a896c981834ea09476e7b153d9ba24.mailgun.org/messages",
            "auth": ("api", self.MAIL_GUN_API_KEY),
            "body": {"from": self.data.get_from_name() + " " + "<" + self.data.get_from_email() + ">",
                "to": [self.data.get_to_name(), self.data.get_to_email()],
                "subject": self.data.get_subject(),
                "text": self.data.get_body()}
            }
            resp = requests.post(mail_data["url"], auth=mail_data["auth"],data=mail_data["body"])

            return {
                "status_code": resp.status_code,
                "message": resp.json()['message']
            }

        def send_via_sendgrid(self):

            mail_data = {
            "url": "https://api.sendgrid.com/v3/mail/send",
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

        def send_email(self):
            try:
                for email_service in self.email_service_obj:
                    response = email_service['service']
                    if response['status_code'] == email_service['success_code']:
                        return email_service["success_response"]

                #All the email services failed to send an email
                return const.EMAIL_FAILED_TO_SEND_MESSAGE

            #technical error on our end
            except Exception as e:
                return const.TECHNICAL_ERROR_MESSAGE + str(e)
