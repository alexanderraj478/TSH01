import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from psh import TSHShell
from TSHGlobal.TSHGlobal import GetFunctionAddr
from TSHGlobal import constants as c
from TSHGlobal.constants import TSH_SEL_PRIV

def main():
    
    pass

class c1:
    def __init__(self):
        print("c1:init:")
    
class c2:
    def __init__(self, a, b):
        print("c2:init:" + a + ":" + b)
        
class c3:
    def c3Method1(self):
        print("c3:c3Method1:")
    
    def c3Method2(self, c, d):
        print("c3:c3Method2:" + c + ":" + d)

def func07(a, b=3, c=6, *hello, **kwargs):
    print ("func07")
    print ("a:" + str(a))
    print ("b:" + str(b))
    for i in (hello):
        print ("args" + str(i))

    if (None != kwargs):
        for key, val in kwargs.items():
            print (key + ":" + val)

def ExternalToClassSelenium():
    pass

class TSHAnotherClass:
    def TSHAnotherMethod(self):
        pass
    class TSHEmbedClass:
        def TSHEmbedMethod(self):
            pass

@staticmethod
def GetClassInfo1():
    tshExampleObj = TSHExampleClass()
    funcAddr = GetFunctionAddr(tshExampleObj, "TSHOSName")
    print("Global GetClassInfo1")
    print(funcAddr)
        
class TSHExampleClass:
    def GetClassInfo1(self):
        tshExampleObj = TSHExampleClass()
        funcAddr = GetFunctionAddr(tshExampleObj, "TSHSelFindElement")
        funcAddr = GetClassInfo1
        
        print("Class GetClassInfo1")
        print(funcAddr)

    @staticmethod
    def GetClassInfo():
        tshExampleObj = TSHExampleClass()
        funcAddr = GetFunctionAddr(tshExampleObj, "TSHSelFindElement")
        funcAddr = GetClassInfo1
        
        print("GetClassInfo1")
        print(funcAddr)
        
    def __init__(self):
        self.driver = None
        #options = webdriver.ChromeOptions()
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument("--test-type")
        #options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        #driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")  # Optional argument, if not specified will search path.
        #driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options=options)

class TSHSelenium:

    def TSHSelFindElement(self, **keyValDict):
            if keyValDict is not None:
                for key, val in keyValDict.items():
                    if (val in (None, '')):
                        pass
                    else:
                        if (c.TSH_SEL_NAME == key):
                            obj = self.driver.find_element_by_name(val)
                            break
                        elif (c.TSH_SEL_XPATH == key):
                            obj = self.driver.find_element_by_xpath(val)
                            break
                        elif (c.TSH_SEL_LNK_TXT == key):
                            obj = self.driver.find_element_by_link_text(val)
                            break
                            
                        elif (c.TSH_SEL_PARTIAL_LNK_TXT == key):
                            obj = self.driver.find_element_by_partial_link_text(val)
                            break
                        elif (c.TSH_SEL_TAG_NAME == key):
                            obj = self.driver.find_element_by_tag_name(val)
                            break
                        elif (c.TSH_SEL_CLS_NAME == key):
                            obj = self.driver.find_element_by_class_name(val)
                            break
                        elif (c.TSH_SEL_CSS_SEL == key):
                            obj = self.driver.find_element_by_css_selector(val)
                            break
                        elif (c.TSH_SEL_ID == key):
                            obj = self.driver.find.element_by_id(val)
                            break
                        elif (TSH_SEL_PRIV == key): # this key Name is made up for program design reason since key value is required in header
                            obj = self.driver.find_element(val)
                            break

#To find multiple elements (these methods will return a list):
                        
    def TSHSelFindElements(self, **keyValDict):
            if keyValDict is not None:
                for key, val in keyValDict.items():
                    if (val in (None, '')):
                        pass
                    else:
                        if (c.TSH_SEL_NAME == key):
                            obj = self.driver.find_elements_by_name(val)
                            break
                        elif (c.TSH_SEL_XPATH == key):
                            obj = self.driver.find_elements_by_xpath(val)
                            break
                        elif (c.TSH_SEL_LNK_TXT == key):
                            obj = self.driver.find_elements_by_link_text(val)
                            break
                        elif (c.TSH_SEL_PARTIAL_LNK_TXT == key):
                            obj = self.driver.find_elements_by_partial_link_text(val)
                            break
                        elif (c.TSH_SEL_TAG_NAME == key):
                            obj = self.driver.find_elements_by_tag_name(val)
                            break
                        elif (c.TSH_SEL_CLS_NAME == key):
                            obj = self.driver.find_elements_by_class_name(val)
                            break
                        elif (c.TSH_SEL_CSS_SEL == key):
                            obj = self.driver.find_elements_by_css_selector(val)
                            break
                            #private method
                        elif (c.TSH_SEL_ID == key):
                            obj = self.driver.find.elements_by_id(val)
                            break
                        elif (TSH_SEL_PRIV == key): # this key Name is made up for program design reason since key value is required in header
                            obj = self.driver.find_elements(val)
                            break
                        else:
                            pass

    def TSHSelSendKeys(self, vObj, val, **keyValDict):
        if keyValDict is not None:
            for key, val in keyValDict.items():
                if (val in (None, '')):
                    pass
        vObj.send_keys(val)
        
    
    def TSHSelIsDisplayed(self,  vObj):
        return (vObj.is_displayed())
    
    def TSHSelIsEnabled(self,  vObj):
        return (vObj.is_enabled())

    def TSHSelClick(self,  vObj):
        vObj.click()
    
    def TSHSelSubmit(self, **KVDict):
        print(KVDict)
        keyValDict = KVDict["keyValDict"]
        
        if keyValDict is not None:
            for key, val in keyValDict.items():
                if (val in (None, '')):
                    pass
                else:
                    print (key + ":" + str(val))

        sessionObj = keyValDict["DriverObj"]
        createMetadataOnTheFly = sessionObj.ProcessTSHGet(suiteName="TSH",
                                        functionName="TSH",
                                        parameterName="createMetadataOnTheFly")
        print(createMetadataOnTheFly)
        print("Hello")
        #vObj.submit()
        
    def TSHSelQuit(self):
        self.driver.quit()
        
    def TSHSelGet(self, url):
        self.driver.get(url)
        

    
    def sample01(self):
        #driver.get('https://python.org')
        #driver.get('https://youtube.com')

        sys.stdout.write("Hello Python: %s\n" % (sys.version))
        driver = webdriver.Chrome("C:\\araj\\python\\f7\\chromedriver.exe")
        #driver.get('http://www.google.com/xhtml');
        driver.get('https://fuscdrmsmc222-fa-ext.us.oracle.com/hcmUI/faces/FuseWelcome')
        time.sleep(5) # Let the user actually see something!
        search_box = driver.find_element_by_name('userid')
        search_box.send_keys('edwards')
        search_box = driver.find_element_by_name('password')
        search_box.send_keys('Welcome1')
        
        driver.find_element_by_name('btnActive').click()
        search_box.submit()
        time.sleep(5) # Let the user actually see something!
        driver.quit()

class Class10:
    def __init__(self):
        pass
    def method10(self):
        tshSel = TSHSelenium()
        driver = webdriver.Chrome()
        tshSel.TSHSelGet("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        tshSel.TSHSelQuit()
        driver.close()
    def method11(self):
        tshSel = TSHSelenium()
        driver = webdriver.Chrome()
        tshSel.TSHSelGet("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        tshSel.TSHSelQuit()
        driver.close()


if (__name__ == "__main__"):
    print("Being run standalone")
    cls10 = Class10()
    cls10.method10()