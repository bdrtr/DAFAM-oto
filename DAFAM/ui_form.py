# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 631)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"  background:#003049;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1231, 581))
        self.stackedWidget.setStyleSheet(u"QFrame {\n"
"  background-color:#001d3d;\n"
"  border-radius:10px;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_list = QListWidget(self.home_page)
        self.home_list.setObjectName(u"home_list")
        self.home_list.setGeometry(QRect(160, 20, 451, 551))
        self.home_list.setStyleSheet(u"QListWidget {\n"
"	font: 800 11pt \"Ubuntu Sans\";\n"
"	font: 500 11pt \"Ubuntu Sans\";\n"
"	color: rgb(0, 0, 0);\n"
"    background:rgb(255,255,255);\n"
"    border-radius:20px;\n"
"    text-align:  center;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"  text-align:center;\n"
"  color:black;\n"
"  margin:5px;\n"
"\n"
"\n"
"}")
        self.home_plain_text = QPlainTextEdit(self.home_page)
        self.home_plain_text.setObjectName(u"home_plain_text")
        self.home_plain_text.setGeometry(QRect(633, 29, 371, 161))
        self.home_plain_text.setStyleSheet(u"QPlainTextEdit {\n"
"background-color:#001d3d;\n"
"color:white;\n"
"}")
        self.home_save_button = QPushButton(self.home_page)
        self.home_save_button.setObjectName(u"home_save_button")
        self.home_save_button.setGeometry(QRect(1070, 50, 88, 26))
        self.home_save_button.setStyleSheet(u"QPushButton {\n"
"  background-color:white;\n"
"  color:black;\n"
"}")
        icon = QIcon()
        icon.addFile(u"sources/diskette.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_save_button.setIcon(icon)
        self.home_next_button = QPushButton(self.home_page)
        self.home_next_button.setObjectName(u"home_next_button")
        self.home_next_button.setGeometry(QRect(1070, 10, 88, 26))
        self.home_next_button.setStyleSheet(u"QPushButton {\n"
"  background-color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"sources/next_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_next_button.setIcon(icon1)
        self.widget = QWidget(self.home_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 141, 501))
        self.widget.setStyleSheet(u"QWidget {\n"
"  background-color:#003566;\n"
"  border-radius:50px;\n"
"}")
        self.home_widget_left = QWidget(self.widget)
        self.home_widget_left.setObjectName(u"home_widget_left")
        self.home_widget_left.setGeometry(QRect(10, 70, 121, 321))
        self.home_widget_left.setLayoutDirection(Qt.LeftToRight)
        self.home_widget_left.setAutoFillBackground(False)
        self.home_widget_left.setStyleSheet(u"QWidget {\n"
"  background:#fca311;\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"")
        self.home_show_account = QPushButton(self.home_widget_left)
        self.home_show_account.setObjectName(u"home_show_account")
        self.home_show_account.setGeometry(QRect(10, 70, 88, 26))
        self.home_show_account.setStyleSheet(u"QPushButton {\n"
"  background-color: #003566;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: rgb(246, 211, 45);\n"
"    color:#003566;\n"
"}")
        self.home_show_account.setAutoDefault(True)
        self.label = QLabel(self.home_widget_left)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 81, 18))
        self.label.setStyleSheet(u"QLabel {\n"
"  color:rgb(255,255,255);\n"
"}\n"
"QLabel:hover {\n"
"  \n"
"	color: rgb(26, 95, 180);\n"
"	font: 600 15pt \"Ubuntu Sans\";\n"
"   font-size:20pt;\n"
"}")
        self.home_run = QPushButton(self.home_widget_left)
        self.home_run.setObjectName(u"home_run")
        self.home_run.setGeometry(QRect(10, 130, 88, 26))
        self.home_run.setStyleSheet(u"QPushButton {\n"
"  background-color: #003566;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: rgb(246, 211, 45);\n"
"    color:#003566;\n"
"}")
        self.graphicsView = QGraphicsView(self.home_page)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(640, 230, 341, 201))
        self.graphicsView.setAutoFillBackground(False)
        self.stackedWidget.addWidget(self.home_page)
        self.widget.raise_()
        self.home_list.raise_()
        self.home_plain_text.raise_()
        self.home_save_button.raise_()
        self.home_next_button.raise_()
        self.graphicsView.raise_()
        self.code_page = QWidget()
        self.code_page.setObjectName(u"code_page")
        self.code_code_label = QPlainTextEdit(self.code_page)
        self.code_code_label.setObjectName(u"code_code_label")
        self.code_code_label.setGeometry(QRect(10, 10, 561, 551))
        self.code_code_label.setStyleSheet(u"QPlainTextEdit \n"
"{\n"
"  background-color:white;\n"
"  color:black;\n"
"  border-radius:10px;\n"
"	font: 600 12pt \"Ubuntu Sans\";\n"
"}\n"
"")
        self.code_save_button = QPushButton(self.code_page)
        self.code_save_button.setObjectName(u"code_save_button")
        self.code_save_button.setGeometry(QRect(990, 20, 88, 26))
        self.code_save_button.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"	color: black;\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: black;\n"
"    color:white;\n"
"}")
        self.code_file_open = QPushButton(self.code_page)
        self.code_file_open.setObjectName(u"code_file_open")
        self.code_file_open.setGeometry(QRect(990, 60, 88, 26))
        self.code_file_open.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"	color: black;\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: black;\n"
"    color:white;\n"
"}")
        self.code_info_label = QLabel(self.code_page)
        self.code_info_label.setObjectName(u"code_info_label")
        self.code_info_label.setGeometry(QRect(600, 270, 601, 291))
        self.code_info_label.setStyleSheet(u"QLabel \n"
"{\n"
"  background-color:white;\n"
"  color:black;\n"
"  border-radius:10px;\n"
"	font: 600 12pt \"Ubuntu Sans\";\n"
"}\n"
"")
        self.code_back_button = QPushButton(self.code_page)
        self.code_back_button.setObjectName(u"code_back_button")
        self.code_back_button.setGeometry(QRect(1100, 20, 88, 26))
        self.code_back_button.setStyleSheet(u"QPushButton {\n"
"  background-color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"sources/back-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.code_back_button.setIcon(icon2)
        self.code_run_button = QPushButton(self.code_page)
        self.code_run_button.setObjectName(u"code_run_button")
        self.code_run_button.setGeometry(QRect(990, 120, 88, 71))
        self.code_run_button.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"	color: black;\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: black;\n"
"    color:white;\n"
"}")
        self.code_generate_button = QPushButton(self.code_page)
        self.code_generate_button.setObjectName(u"code_generate_button")
        self.code_generate_button.setGeometry(QRect(730, 230, 88, 26))
        self.code_generate_button.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"	color: black;\n"
"	font: 600 11pt \"URW Bookman\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"	background-color: black;\n"
"    color:white;\n"
"}")
        self.code_prompt = QPlainTextEdit(self.code_page)
        self.code_prompt.setObjectName(u"code_prompt")
        self.code_prompt.setGeometry(QRect(603, 150, 351, 70))
        self.code_prompt.setStyleSheet(u"QPlainTextEdit \n"
"{\n"
"  background-color:white;\n"
"  color:black;\n"
"  border-radius:10px;\n"
"	font: 600 12pt \"Ubuntu Sans\";\n"
"}\n"
"")
        self.plainTextEdit = QPlainTextEdit(self.code_page)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(603, 10, 341, 121))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"  background-color:white;\n"
" border-radius:2px;\n"
" color:black;\n"
"}")
        self.stackedWidget.addWidget(self.code_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.code_notif = QLabel(self.centralwidget)
        self.code_notif.setObjectName(u"code_notif")
        self.code_notif.setGeometry(QRect(500, 590, 281, 18))
        self.code_notif.setStyleSheet(u"QLabel \n"
"{\n"
"  color:white;\n"
"  border-radius:10px;\n"
"	font: 600 12pt \"Ubuntu Sans\";\n"
"}\n"
"")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(70, 600, 1101, 71))
        self.widget_2.setStyleSheet(u"QWidget {\n"
"background-color:#fca311;\n"
"border-radius:20px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_save_button.setText(QCoreApplication.translate("MainWindow", u"   save", None))
        self.home_next_button.setText("")
        self.home_show_account.setText(QCoreApplication.translate("MainWindow", u"show", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ACCOUNTS", None))
        self.home_run.setText(QCoreApplication.translate("MainWindow", u"run", None))
        self.code_code_label.setPlainText(QCoreApplication.translate("MainWindow", u"code is here", None))
        self.code_save_button.setText(QCoreApplication.translate("MainWindow", u"kaydet", None))
        self.code_file_open.setText(QCoreApplication.translate("MainWindow", u"dosya a\u00e7", None))
        self.code_info_label.setText("")
        self.code_back_button.setText("")
        self.code_run_button.setText(QCoreApplication.translate("MainWindow", u"\u00e7al\u0131\u015ft\u0131r", None))
        self.code_generate_button.setText(QCoreApplication.translate("MainWindow", u"\u00fcret", None))
        self.code_prompt.setPlainText(QCoreApplication.translate("MainWindow", u"(prompt) >> ", None))
        self.code_notif.setText("")
    # retranslateUi

