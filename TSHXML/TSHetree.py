import xml.etree.ElementTree as ET

class TSHetree:
    def __init__(self):
        self.fileName = '/home/alex/learn/python/data/xslt/cdcat2.xml'
        self.tree = None
        self.root = None
        self.XMLDoc = """\
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>
<catalog>
  <cd>
    <title>Empire Burlesque 01</title>
    <artist>Bob Dylan 01</artist>
    <country>USA</country>
    <company>Columbia</company>
    <price>10</price>
    <year>1985</year>
  </cd>
  <cd>
    <title>Empire Burlesque 02</title>
    <artist>Bob Dylan 02</artist>
    <country>USA</country>
    <company>Columbia</company>
    <price>20</price>
    <year>1986</year>
  </cd>
</catalog>
"""
        pass
        
    def XMLFileGetDOM(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        
    def XMLStringGetDOM(self):
        f = open(self.fileName, 'r')
        XMLStr = f.read()
        f.close()
        self.root = ET.fromstring(XMLStr)

    def DisplayXML(self, heading):
        print("===============    "+ heading +"    ===============")
        print(self.root.tag)
        for child in self.root:
            print(child.tag, child.attrib)
        print (self.root[0][0].text)
        print (self.root[0][1].text)
        for cd in self.root.iter('cd'):
            print(cd.tag, cd.attrib)
        
        for cd in self.root.find('cd'):
            print(cd.tag)
            
        for cd in self.root.findall('cd'):
            t = cd.find('title')
            title = cd.find('title').text
            artist = t.get('a')
            print(title, artist)
            
        #ic = self.root.find('cd')
#        for num in ic:
#            #title = num. getElementsByTagName('title')[0].firstChild.nodeValue
#            title = "ale"
#            print(title)
        print("===============    EOD    ===============")
#>>> root.tag
#'data'
#>>> root.attrib
#{}
#It also has children nodes over which we can iterate:

#>>>
#>>> for child in root:
#...     print(child.tag, child.attrib)

if (__name__ == "__main__"):
    tshETTree = TSHetree()
    tshETTree.XMLStringGetDOM()
    tshETTree.DisplayXML("XMLFileObjectGetDOM")
    