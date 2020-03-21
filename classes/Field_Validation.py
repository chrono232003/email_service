import re


class Validation:

    def data_validates_successfully(self, email_content):
        validation_arr = [self.__email_is_valid(email_content['recipient_email']),
                          self.__email_is_valid(email_content['sender_email']),
                          self.__name_is_valid(email_content['recipient_name']),
                          self.__name_is_valid(email_content['sender_name']),
                          self.__subject_is_valid(email_content['email_subject']),
                          self.__body_is_valid(email_content['email_body'])]


        # check each field individually
        for val_func_passed in validation_arr:
            print(val_func_passed)
            if val_func_passed is not None:
                return val_func_passed
        print("hit")
        return True

    # utility classes
    def __email_is_valid(self, email):
        regex = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
        return None if regex.search(email) else "Please enter a valid email."

    def __name_is_valid(self, name):
        regex = re.compile(r'^[aA-zZ\s]+$')
        return None if regex.match(name) else "Please enter a valid name."

    def __subject_is_valid(self, subject):
        regex = re.compile(r'^[\w\d\s_-]*$')
        return None if regex.match(subject) else "Please enter a valid subject."

    def __body_is_valid(self, body):
        regex = re.compile(r'^[\w\d\s_-]*$')
        return None if regex.search(body) else "Please enter a valid body."
