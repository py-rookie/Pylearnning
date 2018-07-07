#! python 
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:37:58 2018
@author: Chen YC
"""

import pyperclip
import re



text = pyperclip.paste()

patternPhone = r'.?(\d\d.?\d\d\d\d?-?\d\d\d\d)'
patternEmail=r'([A-Za-z0-9\._%]+@.+\w)'

patternPhone=re.compile(patternPhone)
patternEmail = re.compile(patternEmail)

moPhone=patternPhone.findall(text)
moEmail=patternEmail.findall(text)

textPhone=','.join(moPhone)
textEmail=','.join(moEmail)
print(moPhone)
print(moEmail)

pyperclip.copy(textPhone)
pyperclip.copy(textEmail)

print('the phone and email are copied to the clipboard')