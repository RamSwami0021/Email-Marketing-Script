#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 17:50:54 2024

@author: manasgargv6
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pandas as pd 
from time import sleep 


# Set up the email parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'ram.premad@gmail.com'
sender_password = 'dzotdlypvheodphw'

# Set up the email message




df1 = pd.read_csv('useList.csv')

for i in range(0,len(df1)):
    recipient_email = df1.loc[i,'email']
    name = df1.loc[i, 'name']
    link = df1.loc[i, 'link']
    msg = MIMEMultipart()
    msg['Subject'] = 'test17'
    msg['From'] = sender_email

    with open('/Users/ramswami/Desktop/MAILING-HTML/1.png', 'rb') as img_file:
        img3 = MIMEImage(img_file.read())
        img3.add_header('Content-ID', '<image3>')
        msg.attach(img3)
    with open('/Users/ramswami/Desktop/MAILING-HTML/2.png', 'rb') as img_file:
        img4 = MIMEImage(img_file.read())
        img4.add_header('Content-ID', '<image4>')
        msg.attach(img4)
    with open('/Users/ramswami/Desktop/MAILING-HTML/3.png', 'rb') as img_file:
        img5 = MIMEImage(img_file.read())
        img5.add_header('Content-ID', '<image5>')
        msg.attach(img5)
    with open('/Users/ramswami/Desktop/MAILING-HTML/4.png', 'rb') as img_file:
        img6 = MIMEImage(img_file.read())
        img6.add_header('Content-ID', '<image6>')
        msg.attach(img6)
    with open('/Users/ramswami/Desktop/MAILING-HTML/icon.png', 'rb') as img_file:
        img7 = MIMEImage(img_file.read())
        img7.add_header('Content-ID', '<image7>')
        msg.attach(img7)
    with open('/Users/ramswami/Desktop/MAILING-HTML/youtube.png', 'rb') as img_file:
        img8 = MIMEImage(img_file.read())
        img8.add_header('Content-ID', '<image8>')
        msg.attach(img8)
    with open('/Users/ramswami/Desktop/MAILING-HTML/insta.png', 'rb') as img_file:
        img9 = MIMEImage(img_file.read())
        img9.add_header('Content-ID', '<image9>')
        msg.attach(img9)
    with open('/Users/ramswami/Desktop/MAILING-HTML/linkedin.png', 'rb') as img_file:
        img10 = MIMEImage(img_file.read())
        img10.add_header('Content-ID', '<image10>')
        msg.attach(img10)
    with open('/Users/ramswami/Desktop/MAILING-HTML/12.png', 'rb') as img_file:
        img12 = MIMEImage(img_file.read())
        img12.add_header('Content-ID', '<image12>')
        msg.attach(img12)



  # Add the image reference to the email body
    # body = '''
    # <html>
    #     <body>
    #         <h1>Title</h1>
    #         <p>This is a paragraph.</p>
    #         <a href="https://khojope.com/"><img src="cid:image1"></a>
    #     </body>
    # </html>
    # '''
    body = '''
    <html>
            <body style="margin: 20px auto; text-align: center; color: #939393;
width: 650px;
font-family: 'outfit', sans-serif;
background-color: #F2E3D4;
display: block;
">
    <table align="center" border="0" cellpadding="0" cellspacing="0"
        style="background: #fff; width: 100%; box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);-webkit-box-shadow: 0px 0px 14px -4px rgba(0, 0, 0, 0.2705882353);">
        <tbody style="background-color: #f2e3d4;"">
            <tr>
                <td>
                    <table class="header-table" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="background: linear-gradient(to right, #cf4258, #f38d56);
                    ">
                    
                        <tr class="header" style="display: flex;align-items: center;justify-content: space-between;">

                            <td>
                                <a target="_blank" href="https://www.khojorightnow.com/">
                                    <img src="cid:image12" style="width: 100%;"/>
                                </a>
                            </td> 

                        </tr>
                    </table>

                    <table class="contant-table" style="margin-top: 40px;" align="center" border="0" cellpadding="0"
                        cellspacing="0" width="100%">
                        <thead>
                            <tr>
                                <td>
                                    <h3
                                        style="font-weight: 700; font-size: 20px; margin: 0;color: black;margin-bottom: 15px;">
                                        Hi {name}, Thank you for choosing KHOJO! <br> Here's your personalised link :<br> {link} </h3>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <a target="_blank" href="{link}"><img src="cid:image3" style="width: 100%;"/></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <a target="_blank" href="https://app.khojorightnow.com/"><img src="cid:image4" style="width: 100%; margin-top: -15px;"/></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <a target="_blank" href="https://www.youtube.com/watch?v=vmGzJsVwWp0"><img src="cid:image5" style="width: 100%; margin-top: -15px;"/></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <a target="_blank" href="https://rzp.io/l/CardJaipurCIRC"><img src="cid:image6" style="width: 100%; margin-top: -15px;"/></a>
                                </td>
                            </tr>
                        </thead>
                    </table>

                    <table class="text-center footer-table" align="center" border="0" cellpadding="0" cellspacing="0"
                        width="100%"
                        style="background: linear-gradient(to right, #cf4258, #f38d56);
                        color: white; padding: 24px; overflow: hidden; z-index: 0; margin-top: -15px;">
                        <tr>
                            <td>
                                <table border="0" cellpadding="0" cellspacing="0" class="footer-social-icon text-center"
                                    align="center" style="margin: 8px auto 11px;">
                                    <tr>
                                        <td>
                                            <h4 style="font-size: 19px; font-weight: 700; margin: 0;"> <a target="_blank" href="https://www.khojorightnow.com/" style="text-decoration: none; color: #fff;">Khojo Right Now</a></h4>
                                        </td>
                                    </tr>
                                </table>
                                <table border="0" cellpadding="0" cellspacing="0" class="footer-social-icon text-center"
                                    align="center" style="margin: 8px auto 20px;">
                                    <tr>
                                        <td>
                                            <a target="_blank" href="https://rzp.io/l/ProfileJaipurCIRC"
                                                style="font-size: 14px; font-weight: 600; color: #fff; text-decoration: none; text-transform: capitalize;">Smart AI Profile</a>
                                        </td>
                                        <td>
                                            <a target="_blank" href="https://rzp.io/l/CardJaipurCIRC"
                                                style="font-size: 14px; font-weight: 600; color: #fff; text-decoration: none; text-transform: capitalize; margin-left: 20px;">Smart Card</a>
                                        </td>
                                        <td>
                                            <a target="_blank" href="https://www.khojorightnow.com/contact.html"
                                                style="font-size: 14px; font-weight: 600; color: #fff; text-decoration: none; text-transform: capitalize; margin-left: 20px;">Contact
                                                Us</a>
                                        </td>
                                    </tr>
                                </table>
                                <table border="0" cellpadding="0" cellspacing="0" class="footer-social-icon text-center"
                                    align="center" style="margin: 23px auto;">
                                    <tr>
                                        <td>
                                            <a target="_blank" href="https://khojope.com/khojope">
                                                <img src="cid:image7"
                                                    style="font-size: 25px; margin: 0 18px 0 0;width: 22px;"
                                                    alt="">
                                            </a>
                                        </td>
                                        <td>
                                            <a target="_blank" href="https://www.youtube.com/@KhojoRightNow">
                                                <img src="cid:image8"
                                                    style="font-size: 25px; margin: 0 18px 0 0;width: 22px;"
                                                    alt="">
                                            </a>
                                        </td>
                                        <td>
                                            <a target="_blank" href="https://www.instagram.com/khojorightnow/">
                                                <img src="cid:image9"
                                                    style="font-size: 25px; margin: 0 18px 0 0;width: 22px;"
                                                    alt="">
                                            </a>
                                        </td>
                                        <td>
                                            <a target="_blank" href="https://www.linkedin.com/company/khojo-right-now/mycompany/verification/">
                                                <img src="cid:image10"
                                                    style="font-size: 25px; margin: 0 18px 0 0;width: 24px; color:white;"
                                                    alt="">
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td>
                                            <h5 style="font-size: 13px; text-transform: uppercase; margin: 10px 0 0; color:#ddd;
                                letter-spacing:1px; font-weight: 500;">Copyright © 2024 <a target="_blank" href="https://www.khojorightnow.com/" style="color: #fff;">Khojo Right Now</a></h5>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
        </body>
    </html>
    '''
    body = body.replace('{name}', name)
    body = body.replace('{link}', link)

   

   

    msg.attach(MIMEText(body, 'html'))
    msg['To'] = recipient_email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    # name = df1.loc[i,'name']
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Email sent to {recipient_email} for {name}")
    server.quit()
    sleep(4)
