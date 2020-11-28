from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import argparse

parser = argparse.ArgumentParser(description="Mass mailer script")
parser.add_argument("-msg",dest="messg",help=" -msg + message to send")
parser.add_argument("-directions",dest="filename",help= "filename or path")
params = parser.parse_args()


user = "eric.valenzuelascd@uanl.edu.mx"
passwd = "c7qoNsZX"

message = params.messg
file_dirs = params.filename
destinatarios = []
direcciones = open(file_dirs,"r")
lines = direcciones.readlines()
for line in lines:
    destinatarios.append(line)
    
 # send the message via the server.
for destinatario in destinatarios:
    # create message object instance
    msg = MIMEMultipart()
    msg['To'] = destinatario
    # setup the parameters of the message
    msg['From'] = user
    msg['Subject'] = "PruebaLab"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.office365.com:587')

    server.starttls()
    # Login Credentials for sending the mail
    server.login(user, passwd)
    server.sendmail( msg['From'],msg['To'], msg.as_string())
    print("successfully sent email to:",destinatario)   
    server.quit()       
            
           


           
    

 

        



 


 



 


 
