'''
Name: Rayyan Aamir
Date: June 11, 2022
Program: Python Web Scraping
'''

# Modules
from bs4 import BeautifulSoup

# Open the file 
with open("index.html", "r") as f: # Open html file in read mode
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify()) # prettify() gives indentation

