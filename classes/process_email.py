import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))

import field_validation
import send_email
import email_data_model
import const

# high level class that performs all the lower lever functions such as validation and triggering the email.
class Process:

    def __init__(self, email_content):
        #Check to make sure that we are getting email content here and that it is in json format
        if email_content:
            self.email_content = email_content

        else:
            return const.MISSING_EMAIL_CONTENT_STRING

    def response(self):
        # validate incoming data
        validation = field_validation.Validation()
        validation_response = validation.data_validates_successfully(self.email_content)
        if validation_response == 'Valid':
            # store information in a data model
            self.data = email_data_model.Data(self.email_content)
        else:
            return validation_response

        #send email
        email = send_email.Send_Email(self.data)
        return email.send_email()
