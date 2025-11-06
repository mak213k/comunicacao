# Para executar esta atividade. 
# É necesário criar uma conta ou senha app 
# na plataforma que vai fazer o disparo do email
# pelo protocolo SMTP.
# Veja o procedimento na sua lataforma de email

import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD_APP = os.getenv("PASSWORD_APP")
FROM = os.getenv("FROM")
TO = "EMAIL DESTINO"

# Create the email message
msg = EmailMessage()
msg['Subject'] = "Test Email from Python"
msg['From'] = FROM
msg['To'] = FROM
msg.set_content("This is a test email sent using Python.")

# Connect to the SMTP server
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: # Use SMTP_SSL for secure connection
        server.login(EMAIL, PASSWORD_APP) # Replace with your credentials
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")