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
target_email = re.findall("/^[^\.\s][\w\-]+(\.[\w\-]+)*@([\w-]+\.)+[\w-]{2,}$/gm", html)
print(target_email)
filtered = []
keys = ['.com', '.net', '.io', '.html', 'htm']

def clear_list(list, keys):
    for l in list:
        for k in keys:
            if k in l:
                if l not in filtered:
                    filtered.append (l)

# Filter results to get more common urls
clear_list (target_url, keys)
print (filtered)