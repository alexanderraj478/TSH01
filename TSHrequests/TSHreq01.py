'''
HashSet Class. Java HashSet is the basic implementation the Set interface that is backed by a HashMap. ...
TreeSet Class. A NavigableSet implementation based on a TreeMap . ...
ArrayList Class. ...
LinkedList Class. ...
HashMap Class. ...
TreeMap Class. ...
PriorityQueue Class.
https://www.journaldev.com/1260/collections-in-java-tutorial
'''
import requests
import pycurl
import numpy as np

import urllib.request
import urllib3
from bs4 import BeautifulSoup

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
    from io import BytesIO
    

class TSHreq01:
    def get(self):
        response = requests.get("http://api.open-notify.org/astros.json")
        print (response)
        
        print(response.json())
        #print(str(response.text()))
        #print(str(response.content()))
    
    def pycurlGet(self):
        buffer = StringIO()
        #buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://pycurl.io/')
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        print(body)
        pass
    
    def ex01(self):
        arr = []
        try:
            arr = np.array([1, 2, 3, 4], dtype='i4')
            print(arr.dtype)
        except ValueError:
            print("ValueError")
        except AttributeError:
            print("AttributeError")

        x="1,   3\n     4.5, 8"
        print(np.genfromtxt(StringIO(x), delimiter=",", autostrip=True))
        
    def helper01(self, x):
        return (x + x)
    
    def calculateSquare(self, n):
        return n*n

    def ex02(self):
        x=np.array(('abc', 'de', 'fghijk'), dtype=np.object)
        print(x[0])
        print(x[1])
        print(x[2])
        print(str(x))
        print(len(x))
        print(list(map(len, x)))
        j = map(type, x)
        print(list(j))
        y=np.array(('abc', 'de', 'fghijk'), dtype=np.object_)
        print(y)
        a = [4,5,6]
        z = [1,2,3]
        print(list(map(self.helper01, z)))
        
        print(list(map(lambda x: x + x, z)))
        print(list(map(lambda x, y: x+y, a, z)))
        
        print(list(map(list, y)))
        


        numbers = (1, 2, 3, 4)
        result = list(map(self.calculateSquare, numbers))
        print(result)
        
        # converting map object to set
        numbersSquare = set(result)
        print(numbersSquare)

    def ex03(self):
        # Program to show the use of lambda functions
        double = lambda x: x * 2
        print(double)
        #print(double())
        print(double(5))
        
    def ex04(self):
        vLst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        vLst2 = list(filter(lambda x: x%2 == 0, vLst1))
        print(vLst2)
    
    def ex05(self):
        response = urllib.request.urlopen('http://tutorialspoint.com/python/python_overview.htm')
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        strhtm = soup.prettify()
        print(strhtm[:2048])
if (__name__ == "__main__"):
    tshReq01 = TSHreq01()
    tshReq01.ex05()
    quit()
    tshReq01.ex03()
    tshReq01.ex04()
    #tshReq01.pycurlGet()
    #tshReq01.get()
    
    