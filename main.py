'''
Name: Rayyan Aamir
Date: June 14, 2022
Program: Python Web Scraping
'''

# Modules
from bs4 import BeautifulSoup
import requests

# Web scraping a file in same directory

'''
with open("index.html", "r") as f: # Open html file in read mode
    doc = BeautifulSoup(f, "html.parser")
'''

# print(doc.prettify()) # prettify() gives indentation

# To find the target information from a website, search for a tag that it will likely be under
''' # Tag methods
tag = doc.title # Find the first occurence of "<title>"
print(tag) # Print the text within its tags
print(tag.string) # Get the text only 
tag.string = "hello" # Change the tag in the document

tags = doc.find_all("p") # Get all <p> tags
print(tags.find_all("b")) # Get the <b> tags nested within the <p> tags
'''

# Web scraping a file from browser
url = ""
result = requests.get(url) # Send an http get-request and return contents of the page
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$") # Find all prices
parent = prices[0].parent # Returns the tag that hosts the "$"
strong = parent.find("strong")
print(strong.string)
