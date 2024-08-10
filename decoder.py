from login import TrustPilot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, threading
from concurrent.futures import ThreadPoolExecutor
from logger import setup_logger
import logging


class AST:

    def __init__ (self, all_lines):
        
        self.all_lines = all_lines
        self.lines = []

        self._keys = {
            "ok": "Keys.RETURN",
            'none':"Keys.ENTER"
        }

        self.process_order = {}
        self.base_code = """\n"""


        self.special_keys = ['driver', 'bas', 'doldur']

    def decode(self):

        _split_lines = self.all_lines.split('\n')
       
        for line in _split_lines:

            line = str.strip(line)
            words = line.split('  ')

            """  driver
                 bas
                 doldur
                 yeni_sayfa
                 sayfa_degistir
                 aktif_elemana_tikla
                 eve_don
                 bilgi_al
            
            """

            if words[0] not in self.special_keys:
                return 0

            elif words[0] in "driver":
                self.base_code+=f"alg = Algoritma(link={words[1]}, type='{words[2]}')\ntime.sleep(0.5)\n"
            elif words[0] in "bas":
                self.base_code+=f"alg.click(10, '{words[1]}', {words[2]})\ntime.sleep(0.5)\n"
            elif words[0] in "doldur":
                self.base_code+=f"alg.fill(10, '{words[1]}', {words[2]}, {words[3]}, {self._keys[words[4]]})\n"
