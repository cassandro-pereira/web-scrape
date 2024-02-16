# Tool indented to look inside Web HTML files and save as output URLs and email patterns to a .json file
import requests
#import json
print("Please enter the main domain http:// or https:// url to be analysed: ", end="")
# Getting url from prompt
url = input()
domain = requests.get(url)
#Retriving HTML file
html = domain.text
print(html)