import urllib as ub
from bs4 import BeautifulSoup
import ssl

# Test link: http://www.dr-chuck.com/page1.htm

# This ignores SSL certificate errors, meaning https will work now.
new_context = ssl.create_default_context()
new_context.check_hostname = False
new_context.verify_mode = ssl.CERT_NONE


url = input("URL: ")
html_data = ub.request.urlopen(url, context = new_context).read()
thai = BeautifulSoup(html_data, 'html.parser') #This scrapes the text

tags = thai('a') #'a' represents the anchor tag of the html body which contains
                 #              a hyperlink. So, this brings out all the hrefs.
for tag in tags:
    print(tag.get('href'))