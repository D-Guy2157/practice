import smtplib

sender = "ddcool535@gmail.com"
receiver = "dharve2005@gmail.com"
password = "i see u peekin"
subject = "Python Email Test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")  # either incorrect login details or less secure apps is turned off
                                # as of May 30, 2022, Google no longer supports the use of third-party apps or devices
                                # which ask you to sign in to your Google Account using only your username and password.
