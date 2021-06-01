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
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



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
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



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
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



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
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



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
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



def forgotPasswordMail(name, email, citizen_id, new_password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: New Login Password
Hi """ + name + """!

Your new login credentials is generated as per your request from the forgot password section of Pocket Certificate

Citizen ID: """ + citizen_id + """
Password: """ + new_password + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



def forgotAadhaarKeyMail(name, email, aadhaar_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Your Aadhaar Key
Hi """ + name + """!

The private key to download your Aadhaar is : """ + aadhaar_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



def forgotPanKeyMail(name, email, pan_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Your PAN Key
Hi """ + name + """!

The private key to download your PAN is : """ + pan_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



def forgotVoterKeyMail(name, email, voter_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Your Voter ID Key
Hi """ + name + """!

The private key to download your Voter ID is : """ + voter_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')



def forgotDrivingKeyMail(name, email, driving_key):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Ready to send mail...')
    s.starttls()
    s.login(admin_mail, admin_password)
    print('Mail Login successful...')
    message = """From: Pocket Certificate
To: """ + name + """<""" + email + """>
Subject: Your Driving Licence Key
Hi """ + name + """!

The private key to download your Driving Licence is : """ + driving_key + """

DO NOT SHARE OR FORWARD THIS MAIL.

Thanks & Regards
Admin
Pocket Certificate"""
    s.sendmail(admin_mail, email, message)
    print('Mail sent ...')
    s.quit()
    print('Mail Logout successful...')