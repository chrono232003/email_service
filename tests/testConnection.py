# list of mail service priority first to last
email_service_json = [
    {
        "service": "self.send_via_mail_gun",
        "success_code": "const.MAIL_GUN_SUCCESS_CODE",
        "success_response": "const.SUCCESS_MESSAGE_TO_USER_MAIL_GUN"
    },
    {
        "service": "self.send_via_sendgrid",
        "success_code": "const.SEND_GRID_SUCCESS_CODE"
    }
]


for service in email_service_json:
    print(service['service'])