import configparser

config = configparser.RawConfigParser()

config.read("C:\\NopCommerce\\Configurations\\config.ini")



class Readconfig:

    @staticmethod
    def geturl():
        url = config.get("common info", "url")
        return url


    @staticmethod
    def getEmail():
        Email = config.get("common info", "Email")
        return Email

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password
