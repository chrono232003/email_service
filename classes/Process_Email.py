import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))

import field_validation
import Send_Email
import email_data_model
import const

class Process:

    def __init__(self, email_content):
        #Check to make sure that we are getting email content here and that it is in json format
        if email_content:
            #validate incoming data
            validation = field_validation.Validation()
            if validation.data_validates_succesfully(self.data):
                # store information in a data model
                self.data = email_data.Data(email_content)
        else:
            return const.MISSING_EMAIL_CONTENT_STRING

    def response(self):
        send_email = Send_Email.Send_Email(self.data)
        return send_email.send_email()
