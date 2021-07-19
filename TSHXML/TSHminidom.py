from xml.dom import minidom

class TSHminidom:
    def __init__(self):
        self.fileName = '/home/alex/learn/python/data/xslt/cdcat1.xml'
        self.dom = None
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
        self.XMLDoc2 = """\
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
        self.XSLTDoc =  """\
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
  <body>
  <h2>My CD Collection</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Title</th>
      <th>Artist</th>
    </tr>
    <xsl:for-each select="catalog/cd">
    <tr>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="artist"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>
"""
    def XMLFileGetDOM(self):
        self.dom = minidom.parse(self.fileName)

    def XMLFileObjectGetDOM(self):
        datasource = open(self.fileName)
        self.dom = minidom.parse(datasource)  # parse an open file

    def XMLStringGetDOM(self):
        f = open(self.fileName, 'r')
        data = f.read()
        f.close()
        self.dom = minidom.parseString(data)

    def XMLStringGetDOM2(self, XMLStr):
        self.dom = minidom.parseString(XMLStr)
        
    def toprettyxml(self, XMLDoc):
        print("===============    "+ "before" +"    ===============")
        print(XMLDoc)
        print("===============    "+ "after" +"    ===============")
        self.XMLStringGetDOM2(XMLDoc)
        prettyxml = self.dom.toprettyxml()
        print(prettyxml)
    
    def DisplayXML(self, heading):
        print("===============    "+ heading +"    ===============")
        ic = self.dom.getElementsByTagName('cd')
        for num in ic:
            title = num.getElementsByTagName('title')[0].firstChild.nodeValue
            print(title)
        print("===============    EOD    ===============")
    

if __name__ == "__main__":
    tshXML = TSHminidom()
    
    tshXML.XMLFileGetDOM()
    tshXML.DisplayXML("XMLFileGetDOM")
    
    tshXML.XMLFileObjectGetDOM()
    tshXML.DisplayXML("XMLFileObjectGetDOM")
    
    tshXML.XMLStringGetDOM()
    tshXML.DisplayXML("XMLStringGetDOM")
    
    tshXML.XMLStringGetDOM2(tshXML.XMLDoc)
    tshXML.DisplayXML("XMLStringGetDOM2")
    
    tshXML.toprettyxml(tshXML.XMLDoc)
    tshXML.toprettyxml(tshXML.XMLDoc2)