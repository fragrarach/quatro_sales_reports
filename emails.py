import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email(email_body, salesman, attachments=None, subject=None):
    from_str = 'noreply@quatroair.com'
    # to_list = [salesman['email']]
    to_list = ['jan.z@quatroair.com']
    # cc_list = ['sanjay.m@quatroair.com']
    cc_list = ['jan.z@quatroair.com']
    bcc_list = ['jan.z@quatroair.com']

    to_str = ', '.join(to_list)
    cc_str = ', '.join(cc_list)

    subject_str = subject if subject else "Weekly Sales Report"

    msg = MIMEMultipart('alternative')
    msg['From'] = from_str
    msg['To'] = to_str
    msg['CC'] = cc_str
    msg['Subject'] = subject_str
    msg.attach(MIMEText(email_body, 'html'))

    if attachments:
        for attachment in attachments:
            fp = open(attachment['file'], 'rb')
            att = MIMEApplication(fp.read(), _subtype="pdf")
            fp.close()
            att.add_header('Content-Disposition', 'attachment', filename=attachment['name'])
            msg.attach(att)

    s = smtplib.SMTP('aerofil-ca.mail.protection.outlook.com')
    s.starttls()

    s.sendmail(from_str, to_list + cc_list + bcc_list, msg.as_string())
    s.quit()
