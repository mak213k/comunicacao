import smtplib
from email.message import EmailMessage

# Create the email message
msg = EmailMessage()
msg['Subject'] = "Test Email from Python"
msg['From'] = "maksistemasti@gmail.com"
msg['To'] = "makrrc@gmail.com"
msg.set_content("This is a test email sent using Python.")

# Connect to the SMTP server
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: # Use SMTP_SSL for secure connection
        server.login("", "") # Replace with your credentials
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")