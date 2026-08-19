class Notification:
    def send(self):
        print("Sending a generic notification.")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()