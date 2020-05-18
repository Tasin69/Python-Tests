import urllib as ub
from bs4 import BeautifulSoup
import ssl

# Test link: http://py4e-data.dr-chuck.net/comments_42.html

# This ignores SSL certificate errors, meaning https will work now.
new_context = ssl.create_default_context()
new_context.check_hostname = False
new_context.verify_mode = ssl.CERT_NONE


url = input("URL: ")
html_data = ub.request.urlopen(url, context = new_context).read()
thai = BeautifulSoup(html_data, 'html.parser') #This scrapes the html data

tags = thai('span') # This tag contains the data we need to scrape                    
print(sum([int(tag.contents[0]) for tag in tags]))