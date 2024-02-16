# Tool indented to look inside Web HTML files and save as output URLs and email patterns to a .json file
import requests
import re
#import json
print("Please enter the main domain http:// or https:// url to be analysed: ", end="")
# Getting url from prompt
url = input()
domain = requests.get(url)
#Retriving HTML file
html = domain.text
#print(html)
#filtered information
target_url = re.findall("(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+", html)
print(target_url)
target_email = re.findall("\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", html)
print(target_email)