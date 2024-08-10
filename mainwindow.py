# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsPixmapItem ,QGraphicsScene,QGraphicsView
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QTimer
from DAFAM.ui_form import Ui_MainWindow
import logging, sys, time 

from concurrent.futures import ThreadPoolExecutor
from logger import setup_logger
from PreDefAlgs import Algoritma
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decoder import AST
from comments import api_key, GEMINI


setup_logger() #logging configure
logger = logging.getLogger(__file__) #loggin - process

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.icon_path = "DAFAM//sources//"
        self.setWindowTitle("DAFAM CONTROLLER")
        self.setWindowIcon(QIcon(self.icon_path+"dafam.png"))
        self._gemini_model = GEMINI(api_key, "gemini-1.5-flash") #api and name
        self._definetions()#defs
        self._icons_png() #fill the graphics
        self.listen_states()#listen the buttons and events
        
    




    def _icons_png(self):
        _scene = self._return_scene(self.icon_path+"dafam.png", 300,200)
        self.ui.graphicsView.setScene(_scene)

        _icon = self._return_icon(self.icon_path+"next_button.png", 32,32)
        self.ui.home_next_button.setIcon(_icon)

        _icon = self._return_icon(self.icon_path+"back-button.png", 32,32)
        self.ui.code_back_button.setIcon(_icon)

        _icon = self._return_icon(self.icon_path+"diskette.png", 32,32)
        self.ui.home_save_button.setIcon(_icon)

        _icon = self._return_icon(self.icon_path+"compile.png", 54,54)
        self.ui.code_run_button.setIcon(_icon)


    def _definetions(self): #definations and self metods are there

        self.model_path = "" #path veriables
        self.schema = """email: {} passwd: {}""" #list view schema
        self._accounts = [] #accounts infos
        self.current_row_list = 0 #current list index
        self.accounts_dic = {} # accounts infos but in dict

    def _return_scene(self, _path, sizex, sizey):

        image = QPixmap(_path)
        resized = image.scaled(sizex,sizey)
        item = QGraphicsPixmapItem(resized)
        scene = QGraphicsScene()
        scene.addItem(item)

        return scene
    

    def _return_icon(self, _path, sizex, sizey):
        image = QPixmap(_path)
        resized = image.scaled(sizex,sizey)
        
        return resized



    def _notif(self, _text):  #use for notifications for page code 

        self.ui.code_notif.setText(_text)
        self.ui.code_notif.setVisible(True)
        QTimer.singleShot(2000,self._notif_clear) # 2000ms


    def _notif_clear(self): #notification clear 
        self.ui.code_notif.setVisible(False)


    def show_accounts(self):  #for add accounts from accounts.txt

        with open(f'{self.model_path}') as file:
            
            lines = file.readlines() 

            for line in lines:
                if len(lines) == 0:
                    continue

                words = line.split(' : ')
                words = [str.strip(word) for word in words]

                if len(words) == 2 and len(words[0].split('@')) == 2:
                    
                    if words[0].split('@')[1] == 'outlook.de': self.accounts_dic[f'{words[0]}'] = words[1]
                    # {'xxxxx@outlook.de' : 'passwd'}

                    _formatted = self.schema.format(words[0], words[1])
                    #'email: xxxx, passwd: xxxxx'

                    self._accounts.append(_formatted)
            

            self.ui.home_list.addItems(self._accounts) #fill the list view
            file.close()

    def listen_states(self):

        
        #---page home ----------
        self.ui.home_next_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.home_show_account.clicked.connect(self.get_file) #fill the user list
        self.ui.home_list.itemClicked.connect(self.item_clicked) #####
        self.ui.home_save_button.clicked.connect(self.save_plain_text)
        self.ui.home_run.clicked.connect(self.run)#run planned scenario
        #--- icon
        
        #----page code -----------
        
        self.ui.code_back_button.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.code_file_open.clicked.connect(self.code_file_open)
        self.ui.code_save_button.clicked.connect(self.code_file_save) 
        self.ui.code_run_button.clicked.connect(self.code_file_run)
        self.ui.code_generate_button.clicked.connect(self.generate_comment)
        

    #--------------------code run - save - open


    #------generate GEMINI

    def generate_comment(self):
        _text = self.ui.code_prompt.toPlainText()
        self._gemini_model.set_text(_text)
        QTimer.singleShot(2000, self.fill_prompt_label)

    def fill_prompt_label(self):
        _text = self._gemini_model.get_text()
        self.ui.plainTextEdit.setPlainText(_text)
    
    #that is planned scenario pls don't change
    def run(self):

        link = "https://trustpilot.com/users/connect?redirect=%2F&source_cta=header"

        #registed base scanerio
        
        with ThreadPoolExecutor(max_workers=3) as executor:
        # Her hesap için iş parçacığı oluştur ve çalıştır
            for account in self.accounts_dic:
                logging.info(f"names: {account}")
                executor.submit(self.run_algorithm, account, link)

                
    def run_algorithm(self, account, link):
        logging.info(f"process established for {account} ")
        proxy = "109.94.182.128:4145"
        prog = Algoritma(link=link, type="chrome" , proxy=proxy)
        prog['email'] = account
        prog['passwd'] = self.accounts_dic[account]
        prog.start()

    #
    def code_file_run(self):

        self.code_file_save()
        _text = self.ui.code_code_label.toPlainText()
        #AST for decode .dfm
        _ast = AST(_text)
        #------------ get control about wrote code
        _ast.decode()
        print(_ast.base_code)
        exec(_ast.base_code)
        #----------------

    def code_file_save(self):
        try:

            with open(self.model_path, "w") as _file:
                
                _text = self.ui.code_code_label.toPlainText()
                _file.write(_text)
                self._notif("kaydedildi..")
            
        except Exception as e:
            logger.warning(f"{e}")
            self._notif("bir dosya seçin")

    def code_file_open(self):

        self.model_path , _ = QFileDialog.getOpenFileName(self, 'code dosyası giriniz', '', '*.dfm')
        
        with open(self.model_path) as file:
            
            _read = file.read()
            self.ui.code_code_label.setPlainText(_read)
            file.close()
    #---------------------------------------------------------------------------------------------------------


    def save_plain_text(self):
        _text = self.ui.home_plain_text.toPlainText()

        try:
                
            self._accounts.pop(self.current_row_list)
            self._accounts.insert(self.current_row_list, _text)
            self.ui.home_list.clear()
            self.ui.home_list.addItems(self._accounts)
        
        except Exception as e:
            logger.warning(f"{e}")
            self._notif(f'save işlemi gerçekleşmedi.')


    def item_clicked(self, item):
        _text = item.text()
        self.current_row_list = self.ui.home_list.currentRow()
        self.ui.home_plain_text.setPlainText(_text)
        
    def get_file(self):
        self.model_path, _ = QFileDialog.getOpenFileName(self, "bir kullanıcı dosyası seçin", ".txt")

        self.show_accounts()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())