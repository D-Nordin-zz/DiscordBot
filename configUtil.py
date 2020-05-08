import json

#the class used to gather the config
class configUtil():

    def loadConfig(self):
        print('loading config file')
        with open('appconfig.json', 'r') as file:
            self.config = json.load(file)
            print('cofig loaded')
            return self.config

