from bs4 import BeautifulSoup
import requests
import re

def get_honor(username):
    soup = BeautifulSoup(requests.get('https://www.codewars.com/users/'+username).text, 'html.parser')
    dataset = soup.findAll("div", {"class" : "stat"})
    regexHandler = re.compile('<div class="stat"><b>Honor:</b>(.*?)</div>')
    return int(regexHandler.search(str(dataset)).groups()[0].replace(',',''))

#<div class="stat"><b>Honor:</b>762</div>

print(get_honor('Anayat'))

'''
Description:

Task:

Write a function get_honor which accepts a username from someone at Codewars and returns an integer containing the
user's honor. If input is invalid, raise an error.

If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though
because the server may time out.

Example¹:
>>> get_honor('dpleshkov')
4418
>>> get_honor('jhoffner')
21949
¹ Honor may or may not be current to the user

Libraries/Recommendations:

Python:
urllib.request.urlopen: Opens up a webpage.
re: The RegEx library for Python.
bs4(BeautifulSoup): A tool for scraping HTML and XML.
Notes:

While this kata is in beta, please vote on it and give your rank assessment.
Feel free to voice your comments and concerns in the discourse area.
There is no example tests. Sorry, the honor may vary from time to time. I apologize for the inconvenience.
'''