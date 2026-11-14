# polymorphism: Different object types responding to the same method call. this allows uniformly interaction with different objects.

# Duck Typing: is a programming principle in which an object's suitability is determined by the methods and attributes it provides, rather than its specific class or declared type.
# Analogy: If it looks like a duck and quacks like a duck, treat it like a duck.

class EmailNotification:
    def send(self):
        print("Sending Email notification..")
class WhatAppNotification:
    def send(self):
        print("Sending WhatApp notification...")

message1 = EmailNotification()
message2 = WhatAppNotification()

notifications = [message1, message2] 
for notification in notifications:
    notification.send()

