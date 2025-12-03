from SystemDesign.Creational.Factory.NotificationFactory import NotificationFactory

if __name__ == "__main__":
    factory = NotificationFactory()

    # Send email
    email = factory.create_notification(
        channel="email",
        recipient_email="user@example.com",
        subject="Welcome!",
        body="Thanks for signing up."
    )
    email.send()

    # Send SMS
    sms = factory.create_notification(
        channel="sms",
        phone_number="1234567890",
        message="Your OTP is 456789"
    )
    sms.send()

    # Send Push Notification
    push = factory.create_notification(
        channel="push",
        device_token="a" * 64,
        title="New Message",
        body="You have a new message!"
    )
    push.send()
