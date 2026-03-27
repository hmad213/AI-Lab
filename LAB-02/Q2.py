class Notification:
    def send_message(self):
        print("Sending generic information")

class EmailNotification(Notification):
    def send_message(self):
        print("Sending email to user@example.com.")

class SMSNotification(Notification):
    def send_message(self):
        print("Sending SMS to =923001234567")

a = EmailNotification()
b = SMSNotification()
a.send_message()
b.send_message()