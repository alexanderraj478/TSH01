import sys
import ruamel_yaml

# yaml.preserve_quotes = True

class TSHruamel:
    def __init__(self):
        self.yaml = ruamel_yaml.YAML()
        #yaml = YAML(typ="safe")
        self.data = None
        
    def TSHYAMLLoad01(self):
        with open('/home/alex/test/mongo.yaml') as fp:
            self.data = self.yaml.load(fp)
    
    def TSHYAMLLoad02(self):
        with open('mongo.yaml') as fp:
            self.data = ruamel_yaml.safe_load(fp)

    def TSHYAMLStore01(self):
        with open('/home/alex/test/op.yml', 'w') as f:
                self.yaml.dump(self.data, f)

    def TSHYAMLStore02(self):
        f = open('/home/alex/test/op.yml', 'w')
        self.yaml.default_flow_style = False
        self.yaml.dump({'a': [1, 2]}, f)

    def TSHYAMLLoad03(self):
        yaml=ruamel_yaml.YAML(typ="safe")
        self.data = yaml.load("""a:\n  b: 2\n  c: 3\n""")
        print(self.data)
        
    def TSHYAMLLoad04(self):
        yaml=ruamel_yaml.YAML(typ="safe", pure=True)
        self.data = yaml.load("""a:\n  b: 2\n  c: 3\n""")
        print(self.data)

    def tr(self, s):
        return s.replace('\n', '<\n')  # such output is not valid YAML!

    def TSHYAMLStore03(self):
        f = open('/home/alex/test/op.yml', 'w')
        self.yaml.dump(self.data, sys.stdout, transform=self.tr)
        
if __name__ == "__main__":
    tshRuamel = TSHruamel()
    
    tshRuamel.TSHYAMLLoad01()
    print(tshRuamel.data)
    tshRuamel.TSHYAMLLoad03()
    tshRuamel.TSHYAMLLoad04()

    