import smtplib, ssl

port = 465  # For SSL
receiver_email = "testsmtp631@gmail.com"

sender_email = "testsmtp631@gmail.com"
password = "testsmtp123456"
message = "test message"

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
