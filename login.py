""" This page created by Bedir Karaabali  04.08.2024 
        it's contain trustpilot and outlook.de login process. """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from logger import setup_logger
import time, re, logging

setup_logger()
logging.getLogger(__file__)



def find_clickable_content(func):
    def wrapper(self, *args, **kwargs):

        _driver = args[0]
        _timeout = args[1]
        _finder = args[3]

        se_list = {
            '0':By.ID,
            '1':By.NAME,
            '2':By.CSS_SELECTOR,
            '3':By.CLASS_NAME
        }

        _selector = se_list[f'{args[2]}'] 
        _req = (_selector, _finder)

        logging.info("find_clickable_content basladi")

        try:
            _find_item = WebDriverWait(_driver, timeout=_timeout).until(
                EC.element_to_be_clickable((_req))
            )
            _find_item.click()

        except TimeoutException as t:
            logging.error(f"time out {t} \n\n")
            
        
        except NoSuchElementException as e:
            logging.error(f"no element find {e}")
        
        
        return func(self, *args, **kwargs)
    
    return wrapper


def find_fillable_content(func):
    def wrapper(self, *args, **kwargs):

        _driver = args[0]
        _timeout = args[1]
        _finder = args[3]

        se_list = {
            '0':By.ID,
            '1':By.NAME,
            '2':By.CSS_SELECTOR,
            '3':By.CLASS_NAME
        }
        
        _selector = se_list[f'{args[2]}'] 
        _req = (_selector, _finder)

        logging.info("find_fillable_content basladi")

        try:
            _find_item = WebDriverWait(_driver, timeout=_timeout).until(
                EC.presence_of_element_located((_req))
            )

            for key, value in kwargs.items():
                if value != None or value != '':
                    if hasattr(_find_item, 'send_keys'):
                        _find_item.send_keys(value)
                    else:
                        logging.error(f"{key} wrong process.")

            

        except TimeoutException as t:
            print(f"time out {t} \n\n")
            logging.error(f"time out {_finder}")
        
        except NoSuchElementException as e:
            logging.error(f"no element find {e}")
        
        return func(self, *args, **kwargs)
    
    return wrapper



def get_knowledge(func):
    def wrapper(self, *args, **kwargs):

        _driver = args[0]
        _timeout = args[1]
        _finder = args[3]

        se_list = {
            '0':By.ID,
            '1':By.NAME,
            '2':By.CSS_SELECTOR,
            '3':By.CLASS_NAME
        }
        
        _selector = se_list[f'{args[2]}'] 
        _req = (_selector, _finder)

        logging.info("get_knowledge basladi")

        try:
            _find_item = WebDriverWait(_driver, timeout=_timeout).until(
                EC.presence_of_element_located((_req))
            )

            return _find_item.text

        except TimeoutException as t:
            logging.error(f"time out {t} \n\n")
        
        except NoSuchElementException as e:
            logging.error(f"element bulunamadi {_finder}")
        
        return func(self, *args, **kwargs)
    
    return wrapper





class TrustPilot:

    def __init__(self, _main_link, _browser_type, _proxy:str) -> None:

        self.current_page = 0
        self.result = ''

        self.proxy = _proxy

        self.selectors = {
            'id':0,
            'name':1,
            'css':2,
            'class':3
        }

        self.pages = {}

        self._link = _main_link
        self._browser_type = _browser_type

        self._web_driver = None
        self._cookie_menagement = None
        self.chrome_options = None

        self.preprocess()
        self.request_web_main_page(_main_link)
        self.cookies_control()
        self.pages_update()



    def set_settings(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(f'--proxy-server={self.proxy}')
        logging.info("proxy ayarlandi")


    def extract_numbers(self, text):
        numbers = re.findall(r'\d', text)
        logging.info(f"onay sifresi elde edildi {numbers}")
        return ''.join(numbers)

    def pages_update(self):
        pages = self._web_driver.window_handles
        self.pages = {index: value for index, value in enumerate(pages)}
        logging.info("sayfa degisti")

    def preprocess(self):
        self._web_driver = webdriver.Chrome(options=self.chrome_options) if self._browser_type == "chrome" else webdriver.Firefox()  #now just 2 browser Google Chrome and FireFox

    def request_web_main_page(self, link):
        try:
            self._web_driver.get(link)
            time.sleep(.5)
        except WebDriverException as w:
            logging.error(f"Failed to get the page: {link}. Exception: {w}")

    
    @find_clickable_content
    def pass_cookie(self, driver, timeout, by, value):
        pass


    def cookies_control(self):
        self._cookie_menagement = self._web_driver.get_cookies()
        if self._cookie_menagement:
            self.pass_cookie(self._web_driver, 10, self.selectors['id'], "onetrust-accept-btn-handler")

    
    @find_clickable_content
    def _find_and_click(self, driver, timeout, by, value):
        pass

    def find_and_click(self, timeout=10, by=None, value=None):
        self._find_and_click(self._web_driver, timeout, self.selectors[f'{by}'], value)



    @find_fillable_content
    def _find_and_fill(self, driver, timeout, by, value, **kwargs):
        pass


    def find_and_fill(self, timeout=10, by=None, value=None, text='None', command=None):
        if command != None: self._find_and_fill(self._web_driver,timeout, self.selectors[f'{by}'], value, text=text, command=command)
        else :self._find_and_fill(self._web_driver,timeout, self.selectors[f'{by}'], value, text=text)



    def add_page(self, link):
        self._web_driver.execute_script(f"window.open('{link}');")
        self.pages_update()

    def pages_to(self, page_num):
        self.current_page = page_num
        self._web_driver.switch_to.window(f'{self._web_driver.window_handles[page_num]}')

    def home(self):
        self.pages_to(0)
        self.current_page = 0


    def active_element_click(self):
        active_element = self._web_driver.execute_script("return document.activeElement;")
        time.sleep(.9)
        active_element.send_keys(Keys.ENTER)

    @get_knowledge    
    def _get_knowledge(self, driver, timeout, by, value, **kwargs):
        pass

    def get_knowledge(self, by, value):
        text = self._get_knowledge(self._web_driver, 10, self.selectors[f'{by}'], value)
        self.result = self.extract_numbers(text)

    def end(self):
        logging.info("quiting")
        self._web_driver.quit()


"""
class find_and_fill(object):

    def __init__ (self, selector, value):
        
        self.selector = selector
        self.value = value


    def __call__(self, driver):
        element = driver.find_element(*self.selector)
        if self.value in element.get_attribute('id'):
            return element
        
        else: return False

link = "https://trustpilot.com/users/connect?redirect=%2F&source_cta=header"

if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    driver.get(link)

    element = WebDriverWait(driver, 10).until(
        find_and_fill((By.ID, 'input'), 'input')
    )

    print(element)



"""
    

    







