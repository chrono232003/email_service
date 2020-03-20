import re

class Validation:

    def validateData():
        #check each field individually
        return "nothing yet"

    #utility classes
    def email_is_valid(self, email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.search(regex,email)

    def name_is_valid(self, name):
        return re.match(r'^[aA-zZ\s]+$', name)


    def subject_is_valid(self, subject):
        regex = '/[|&;$%@"<>()+,]/g'
        return re.search(regex,subject)

    def body_is_valid(self, body):
        regex = '/[|&;$%@"<>()+,]/g'
        if(re.search(regex,email)):
            print("Valid Body")
        else:
            print("Invalid Body")
