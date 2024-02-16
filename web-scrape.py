# Tool indented to look inside Web HTML files and save as output URLs and email patterns to a .csv file
import requests
import re
import csv
import logging
logging.basicConfig(level=logging.INFO)

print("Please enter the main domain http:// or https:// url to be analyzed: ", end="")
# Getting url from prompt
url = input()
domain = requests.get(url)
#Retriving HTML file
html = domain.text

#filtered information
target_url = re.findall("(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+", html)
logging.info('Full list of urls')
print(target_url)
target_email = re.findall("/^[^\.\s][\w\-]+(\.[\w\-]+)*@([\w-]+\.)+[\w-]{2,}$/gm", html)
logging.info('Full list of e-mails')
print(target_email)

filtered = []
filtered_all = []
#Common url extensions
keys = ['.com', '.net', '.io', '.html', 'htm']

#Adding extra filters to data cleasing
def clear_list(list, keys):
    for l in list:
        for k in keys:
            if k in l:
                if l not in filtered:
                    filtered.append (l)

#Filter results to get more common urls
clear_list (target_url, keys)
filtered_all = filtered + target_email
print (filtered_all)

#Write urls to file
print("Wrinting the URLs and emails found to output.csv file")
logging.info('Writing found entries to output.csv')

with open('output.csv', 'w', newline='') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(filtered_all)
