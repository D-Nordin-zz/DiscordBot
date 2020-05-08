import json

#the class used to gather the config
class configUtil():

    def loadConfig(self):
        print('loading config file')
        with open('appconfig.json', 'r') as file:
            self.config = json.load(file)
            print('cofig loaded')

    #get a property from the config. if empty return null
    def getProperty(self, property):
        return self.config[property] if self.config[property] else ''
