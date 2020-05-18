import xml.etree.ElementTree as et

sample_xml = '''
<students>
 <student x = "10">
     <id> 1234 </id>
     <year> 3rd </year>
     <session> 2017-18 </session>
      <e-mail hide = 'yes'/>
      <phone type = 'intl'>
       +8801711012345
      </phone>
 </student>
 <student x = "42">
     <id> 4312 </id>
     <year> 3rd </year>
     <session> 2017-18 </session>
      <e-mail hide = 'no'/>
      <phone type = 'intl'>
       +8801919012387
      </phone>
 </student>
</students> 
'''

xml_tree = et.fromstring(sample_xml)
item_list = xml_tree.findall('student') # Creating a list of tags 'student'.
i = 1                                   # Each tag 'student' contains a sub-tree.
for item in item_list:
    print(f'Student {i}:', '\nID:',item.find('id').text,'\nSession:', item.find('session').text, '\nContact No.', item.find('phone').text)
    print(f'St attr {i}:',item.get('x'), '\nE-mail addr:', item.find('e-mail').get('hide'), '\n')
    i += 1