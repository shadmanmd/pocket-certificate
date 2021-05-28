import smtplib

admin_mail = ''
admin_password = ''

def accountCreatedMail(name, email, citizen_id, password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: You are registered
Hi """ + name + """!

You have been registered as a citizen on Pocket Certificate.

Please note your credentials to login to the same.
Citizen ID: """ + citizen_id + """
Password: """ + password + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail('mdshadmancrj@gmail.com', email, message)
    print('mail sent')
    s.quit()



def aadhaarAddedMail(name, email, doc_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Aadhaar Card Added
Hi """ + name + """!

Your Aadhaar Card has been added to your profile. You can download it by logging in & going to "View Documents" section.

Please note the private key to download the same.
Private Key: """ + doc_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail('mdshadmancrj@gmail.com', email, message)
    print('mail sent')
    s.quit()



def panAddedMail(name, email, doc_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: PAN Card Added
Hi """ + name + """!

Your PAN Card has been added to your profile. You can download it by logging in & going to "View Documents" section.

Please note the private key to download the same.
Private Key: """ + doc_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail('mdshadmancrj@gmail.com', email, message)
    print('mail sent')
    s.quit()



def voterAddedMail(name, email, doc_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Voter ID Added
Hi """ + name + """!

Your Voter ID has been added to your profile. You can download it by logging in & going to "View Documents" section.

Please note the private key to download the same.
Private Key: """ + doc_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail('mdshadmancrj@gmail.com', email, message)
    print('mail sent')
    s.quit()



def drivingAddedMail(name, email, doc_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Driving Licence Added
Hi """ + name + """!

Your Driving Licence has been added to your profile. You can download it by logging in & going to "View Documents" section.

Please note the private key to download the same.
Private Key: """ + doc_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail('mdshadmancrj@gmail.com', email, message)
    print('mail sent')
    s.quit()