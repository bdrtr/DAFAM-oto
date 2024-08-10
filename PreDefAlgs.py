from login import TrustPilot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Algoritma():

    def __init__ (self, link, type, proxy = None):

        self.platform = TrustPilot(link, type, proxy)
        self.email = ''
        self.passwd = ''

    def __setitem__(self, key, value):

        if key == 'email': self.email = value
        
        elif key == 'passwd': self.passwd = value


    def click(self, timeout, type, value):
        self.platform.find_and_click(timeout, type, value)

    def fill(self, timeout, type, value, text, num):
        self.platform.find_and_fill(timeout, type, value, text, num) 


    def start(self):
        #that scenario is already created for programmer and not will be change
        
        mail = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=157&ct=1722797878&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3den-us%26country%3dus%26RpsCsrfState%3dc34ac037-be32-3b76-76f2-2cc383370e56&id=292841&aadredir=1&whr=outlook.de&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c"

        self.platform.find_and_click(10,'css', "span.typography_body-l__KUYFJ.typography_appearance-action__9NNRY.link_link__IZzHN.link_underlined__OXYVM")
        time.sleep(.7)
        self.platform.find_and_fill(10, 'id', "email-lookup",f"{self.email}",Keys.RETURN)
        self.platform.add_page(mail)
        self.platform.pages_to(1)
        self.platform.find_and_fill(10, 'name', "loginfmt", f"{self.email}", Keys.RETURN)
        self.platform.find_and_fill(10, 'name', "passwd", f"{self.passwd}", Keys.RETURN)
        self.platform.find_and_click(10,'id', "acceptButton")
        self.platform.active_element_click()
        time.sleep(0.5)
        self.platform.get_knowledge('class', "JdFsz")
        self.platform.home()
        self.platform.find_and_fill(10, 'id', "verification-code-input", self.platform.result)
        time.sleep(2)
        self.platform.end()