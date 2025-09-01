import smtplib
from email.mime.text import MIMEText # Importing MIMEText for email body
from email.mime.multipart import MIMEMultipart # Importing MIMEMultipart for email with attachments
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    #Email Details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    
    #Email content
    subject = f"Workflow {workflow_name} failed for Repository {repo_name}"

    body = f" The workflow {workflow_name} has failed for the repository {repo_name}. Please check the details and take necessary actions.\n More Details: Run_ID: {workflow_run_id} "

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) # Using Gmail SMTP server
        server.starttls() # Starting TLS for security
        server.login(sender_email, sender_password) # Logging in to the email account
        text = msg.as_string() # Converting the message to a string
        server.sendmail(sender_email, receiver_email, text) # Sending the email
        server.quit() # Quitting the server

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))
