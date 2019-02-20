"""
<Users>
    <user>
        <uid>1</uid>
        <FirstName>testuser</FirstName>
        <LastName>testuser</LastName>
        <Email>testuser@test.com</Email>
        <state>xyz</state>
        <location>abc</location>
    </user>
</Users>

https://micropyramid.com/blog/building-and-parsing-xml-document-using-python/


"""


import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()