import urllib as ub
from bs4 import BeautifulSoup
import ssl
import re

# Test link: http://py4e-data.dr-chuck.net/known_by_Fikret.htm

# This ignores SSL certificate errors, meaning https will work now.
new_context = ssl.create_default_context()
new_context.check_hostname = False
new_context.verify_mode = ssl.CERT_NONE


url = input("URL: ")
html_data = ub.request.urlopen(url, context = new_context).read()
thai = BeautifulSoup(html_data, 'html.parser') 
    
for i in range(4):
    tags = thai('a')
    links = [tag.get('href') for tag in tags]
    print(re.findall('by_(.+).html', links[2]))
    url = links[2]
    html_data = ub.request.urlopen(url, context = new_context).read()
    thai = BeautifulSoup(html_data, 'html.parser') 

# In every iteration, we're finding out the anchor tags followed by the links.
# We then create a list of links and scrape the name from our desired link.
# The desired link is sent as the url for the next iteration.