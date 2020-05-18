import xml.etree.ElementTree as et

# Creating a sample xml as a string
sample_xml = '''
<student>
 <student_id> 1234 </student_id>
 <year> 3rd </year>
 <session> 2017-18 </session>
 <e-mail hide = 'yes'/>
 <phone type = 'intl'>
  +8801711012345
 </phone>
</student> 
'''

# Creating the xml tree from the string
xml_tree = et.fromstring(sample_xml)
print('Year:', xml_tree.find('year').text, '\nSession:', xml_tree.find('session').text)
print('Phone Attribute:', xml_tree.find('phone').get('type'))
print('E-mail Attribute:', xml_tree.find('e-mail').get('hide'))