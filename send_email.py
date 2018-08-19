
from email.mime.text import MIMEText
import smtplib

def send_email(email, height, count, average_height):
	from_email="sharinatech@gmail.com"
	from_password="learningnew8"
	to_email=email

	subject="Height Data"  
	message='''Hi there, your height is <strong>%s
	inches</strong>. The average height of the population, gathered from the
	<strong>%s people</strong> who have submitted height data thus far, is <strong>%s
	inches</strong>. <br>Thanks for contributing some data!''' % (height, count, average_height)

	msg=MIMEText(message, 'html')
	msg['Subject']=subject
	msg['To']=to_email
	msg['From']=from_email

	gmail=smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)