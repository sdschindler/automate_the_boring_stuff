#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:10:53 2023

@author: stevenschindler
"""


import re, pyperclip
# Creeate a regex for phone numbers
phoneRegex = re.compile(r'''
                        (
 ((\d\d\d)|(\(\d\d\d\)))?    #area code(optional)
    (\s|-)      #first separator
   \d\d\d       #first 3 digits
     -     #separator
     \d\d\d\d     #last 4 digits
    ( ((ext(\.)?\s)|x)   # extension(optional)
     (\d{2,5}))? #exteension number part (optional)
    )
           
           ''',re.VERBOSE)
           
           
           #TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
                         
      [a-zA-Z0-9_.+] +      # name part
        @                   # @ symbol
      [a-zA-Z0-9_.+] +       # domain name part
                         
                         
                         
                         ''',re.VERBOSE)
           #TODO: get the text off the clipboard
           
           
text =  pyperclip.paste()
           #TODO: Extract the email/phone from this text
           
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbeers = []
for phoneNumber in extractedPhone:
    allPhoneNumbeers.append(phoneNumber[0])

           #TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbeers) +'\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)