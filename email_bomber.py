
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("**********Welcome to Email Bomber Type-1 **************")

print("Please create a fake gmail ID and disable its security to work properly")
print("Create a file 'mycontacts.txt' and enter name and email id in the format shown below")
print("name name@mail.com")
print("-----------------------")

message_template = '''Dear ${PERSON_NAME}, 

This is a test message. 
Have a great weekend! 

Yours Truly'''
print("Create a file 'message.txt' and enter content similar to below format ")
print(message_template)
print("=====================\n\n\n")


MY_ADDRESS = str(input("Enter Your email id : "))
PASSWORD = input("Enter Your password: ")

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# def get_host():
#     smtp_provider = input("select your email provider\n1)GMAIL\n2)OUTLOOK")

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        #print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']= "Important Notice"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        print("Message sent to {}".format(msg['To']))
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()