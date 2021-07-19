import os
import sys
import fileinput
import importlib
import yaml
#import ruamel.yaml
#from ruamel.yaml import *
#import ruamel_yaml as yaml

#TriSHul harness specific imports
from TSHGlobal import *

class TSHyaml:
    def __init__(self):
        self.jsonIPFile = None
        self.jsonOPFile = None
        
        self.jsonIPStr = ""
        self.jsonOPStr = ""

        #cwd = os.getcwd()
        self.fileName = "" #cwd + "/fruits.yaml"
        self.sort_keys = False
        self.data = ""
    
    @property
    def jsonIPFile(self):
        return self.__jsonIPFile
    
    @jsonIPFile.setter
    def jsonIPFile(self, jsonIPFile):
        self.__jsonIPFile = jsonIPFile
        
    @property
    def jsonOPFile(self):
        return self.__jsonOPFile
    
    @jsonOPFile.setter
    def jsonOPFile(self, jsonOPFile):
        self.__jsonOPFile = jsonOPFile
    
    def FileNameSet(self, fileName):
        self.fileName = fileName
    
    def sort_keysSet(self, sort_keys):
        self.sort_keys = sort_keys
        print ("sort_keys" + str(self.sort_keys))
        
    def TSHYAMLLoad(self):        
        #cwd = os.getcwd()
        #fileName = cwd + "/fruits.yaml" 
        
        print(self.fileName)
        
        with open(self.fileName) as file:
                fruits_list = yaml.load (file, Loader=yaml.FullLoader)
                
        print(fruits_list)
        

    def TSHYAMLFullLoad(self):        
        #cwd = os.getcwd()
        #fileName = cwd + "/fruits.yaml" 
        
        print(self.fileName)
        
        with open(self.fileName) as file:
                documents = yaml.full_load (file)
        
        for item, doc in documents.items():
                print(item, ":", doc)
    
    def TSHYAMLDump(self):
        dict_file = [
                        {'sports':
                                    ['soccer', 'football']
                        },
                        {'countries':
                                    ['Pakistan', 'USA']
                        }
                    ]
        with open(self.fileName, 'w') as file:
                documents = yaml.dump(dict_file, file)
        
    def TSHYAMLDump02(self):        
        #cwd = os.getcwd()
        #fileName = cwd + "/fruits.yaml" 
        
        print(self.fileName)
        
        with open(self.fileName) as file:
                doc = yaml.load (file, Loader=yaml.FullLoader)
                #sort_file = yaml.dump(doc, sort_keys=self.sort_keys)
                sort_file = yaml.dump(doc, sort_keys=True)
                
        print(sort_file)

    def read_yaml(self):
        with open('/home/alex/test/mongo.yaml') as f:
            self.data = yaml.safe_load_all(f)
            print (self.data)
            config = list(self.data)
        print(config)
        with open('/home/alex/test/toyaml.yml', 'a') as f:
            yaml.dump_all(config, f, default_flow_style=False)

        return config
 
    def write_yaml(self):
        with open('/home/alex/test/toyaml.yml', 'w') as f:
            yaml.dump_all(self.data, f, default_flow_style=False)
            
            
        
if __name__ == "__main__":
    tshyaml = TSHyaml()
    print("Using yaml")    
    tshyaml.read_yaml()
    #tshyaml.write_yaml()
    
    