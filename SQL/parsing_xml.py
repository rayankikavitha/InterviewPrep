"""
https://docs.python.org/2/library/xml.etree.elementtree.html

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""




import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
print "root, root attributes and root childresn = "
print root.tag, root.attrib, root.getchildren()
print "Parse the children"
for each in root.getchildren():
	print each.tag, each.attrib

print " displaying first childeren's second attribute"
print root[0][1].text

print " Display all the neighbors"
for each in root.iter('neighbor'):
	print each.attrib
	

print "Display the neighbors for Panama country"
for each in root.getchildren():
	if each.attrib['name'] =='Panama':
		for child in each.iter('neighbor'):
			print child.attrib['name']
		

# print total countries in the xml document.
print "*****************"
c = 0
for each in root.iter('country'):
	c +=1
print "total countries = "+ str(c)


# using xpath
#root1 = ET.fromstring('test.xml')

#print root1.findall("./country/neighbor")
