import oyaml as yaml

class TSHoyaml:
    def __init__(self):
        #self.yaml = yaml()
        #yaml = YAML(typ="safe")
        self.data = None
        
    def TSHYAMLLoad01(self):
        with open('/home/alex/test/mongo.yaml') as fp:
            self.data = self.yaml.load(fp)
    
    def TSHYAMLLoad02(self):
        with open('mongo.yaml') as fp:
            self.data = self.yaml.safe_load(fp)

    def TSHYAMLStore01(self):
        with open('/home/alex/test/op.yml', 'w') as f:
                self.yaml.dump(self.data, f)

        
if __name__ == "__main__":
    tshOyaml = TSHoyaml()
    
    tshOyaml.TSHYAMLLoad01()
    print(tshOyaml.data)
    tshOyaml.TSHYAMLStore01()

    