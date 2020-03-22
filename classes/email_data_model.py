import os, sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))

import const

# Store the user input into this structured data class for added structure to the program.
class Data:

    def get_to_email(self):
        return self.__to_email

    def get_to_name(self):
        return self.__to_name

    def get_from_email(self):
        return self.__from_email

    def get_from_name(self):
        return self.__from_name

    def get_subject(self):
        return self.__subject

    def get_body(self):
        return self.__body

    def __init__(self, email_content):

        self.__to_email = email_content[const.TO_EMAIL]
        self.__to_name = email_content[const.TO_NAME]
        self.__from_email = email_content[const.FROM_EMAIL]
        self.__from_name = email_content[const.FROM_NAME]
        self.__subject = email_content[const.SUBJECT]
        self.__body = self.__strip_html_from_body(email_content[const.BODY])

    #This function will strip the html tags and replace them with spaces.
    def __strip_html_from_body(self, body):
        content_no_tags = re.sub('<[^<]+?>', ' ', body)
        content_no_tags = re.sub(' +', ' ', content_no_tags)
        return content_no_tags.strip()
