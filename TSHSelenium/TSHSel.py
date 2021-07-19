import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
#from psh import TSHShell

def ExternalToClassSelenium():
    pass

class TSHSeleniumClass:
    def __init__(self):
        self.driver = None
        #options = webdriver.ChromeOptions()
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument("--test-type")
        #options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        #driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")  # Optional argument, if not specified will search path.
        #driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options=options)


    def TSHSelFindElement(self, **keyValDict):
            if keyValDict is not None:
                for key, val in keyValDict.items():
                    if (val in (None, '')):
                        pass
                    else:
                        if ("name" == key):
                            obj = self.driver.find_element_by_name(val)
                        elif ("xpath" == key):
                            obj = self.driver.find_element_by_xpath(val)
                        elif ("link_text" == key):
                            obj = self.driver.find_element_by_link_text(val)
                        elif ("partial_link_text" == key):
                            obj = self.driver.find_element_by_partial_link_text(val)
                        elif ("tag_name" == key):
                            obj = self.driver.find_element_by_tag_name(val)
                        elif ("class_name" == key):
                            obj = self.driver.find_element_by_class_name(val)
                        elif ("css_selector" == key):
                            obj = self.driver.find_element_by_css_selector(val)
                        elif ("id" == key):
                            obj = self.driver.find.element_by_id(val)
                        elif ("private" == key): # this key Name is made up for program design reason since key value is required in header
                            obj = self.driver.find_element(val)

#To find multiple elements (these methods will return a list):
                        
    def TSHSelFindElements(self, **keyValDict):
            if keyValDict is not None:
                for key, val in keyValDict.items():
                    if (val in (None, '')):
                        pass
                    else:
                        if ("name" == key):
                            obj = self.driver.find_elements_by_name(val)
                        elif ("xpath" == key):
                            obj = self.driver.find_elements_by_xpath(val)
                        elif ("link_text" == key):
                            obj = self.driver.find_elements_by_link_text(val)
                        elif ("partial_link_text" == key):
                            obj = self.driver.find_elements_by_partial_link_text(val)
                        elif ("tag_name" == key):
                            obj = self.driver.find_elements_by_tag_name(val)
                        elif ("class_name" == key):
                            obj = self.driver.find_elements_by_class_name(val)
                        elif ("css_selector" == key):
                            obj = self.driver.find_elements_by_css_selector(val)
                            #private method
                        elif ("id" == key):
                            obj = self.driver.find.elements_by_id(val)
                        elif ("private" == key): # this key Name is made up for program design reason since key value is required in header
                            obj = self.driver.find_elements(val)
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
        
    def sample(self):
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
