import requests

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import key_constants

class Send_Email:

        to_email = ""
        to_name = ""
        from_email = ""
        from_name = ""
        subject = ""
        body = ""

        def __init__(self, email_content):
            self.to_email = email_content['recipient_email']
            self.to_name = email_content['recipient_name']
            self.from_email = email_content['sender_email']
            self.from_name = email_content['sender_name']
            self.subject = email_content['email_subject']
            self.body = email_content['email_body']

        # def send_email():
        #     #validate the fields to make sure we want to send the email_body
        #
        #     #send the email via one of the available services. They are ordered by priority.
        #     try:
        #
        #     catch:

        def send_via_mail_gun(self):
            resp = requests.post(
		          "https://api.mailgun.net/v3/sandbox81a896c981834ea09476e7b153d9ba24.mailgun.org/messages",
		          auth=("api", key_constants.MAIL_GUN_API_KEY),
		          data={"from": self.from_name + " " + "<"+self.from_email+">",
			      "to": [self.to_name, self.to_email],
			      "subject": self.subject,
			      "text": self.body})

            return {
                "status_code": resp.status_code,
                "message": resp.json()['message']
            }

        def send_via_sendgrid(self):

            mail_data = {
            "url": "https://api.sendgrid.com/v3/mail/send",
            "headers": {'Authorization': 'Bearer ' + key_constants.SEND_GRID_API_KEY},
            "body": {
                      "personalizations": [
                        {
                          "to": [
                            {
                              "name": "Rob",
                              "email": "chrono232003@yahoo.com"
                            }
                          ],
                          "subject": "Hello, World!"
                        }
                      ],
                      "from": {
                        "name": "Lance",
                        "email": "from_address@example.com"
                      },
                      "content": [
                        {
                          "type": "text/plain",
                          "value": "Hello, World!"
                        }
                      ]
                    }
            }

            resp = requests.post(mail_data["url"], json=mail_data["body"], headers=mail_data["headers"])

            return {
                "status_code": resp.status_code,
                "message": resp.json()['message']
            }
