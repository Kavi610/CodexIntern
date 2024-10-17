import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    try:
        # Create a MIME message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach file if provided
        if attachment_path:
            attachment_name = os.path.basename(attachment_path)
            with open(attachment_path, "rb") as attachment_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {attachment_name}',
                )
                msg.attach(part)

        # Log in to the server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
        
        print(f"Email sent successfully to {receiver_email}.")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Main program to gather user input and send email
def main():
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    receiver_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Ask for attachment (optional)
    attachment = input("Enter file path for attachment (or leave empty if no attachment): ")
    if attachment.strip() == '':
        attachment = None

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body, attachment)

if __name__ == "__main__":
    main()
