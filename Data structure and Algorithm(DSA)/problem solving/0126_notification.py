#                              notification system using @abstractmethod

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, massage):
        pass

class EmailNotifiction(Notification):
    def send(self, massage):
        print("Email send : ", massage)

class SMSNotification(Notification):
    def send(self, massage):
        print("sms send : ", massage)

email = EmailNotifiction()
sms = SMSNotification()

email.send("welcome to python!")
sms.send("Your otp is 1234")
