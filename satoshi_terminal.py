import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit, QDesktopWidget, QTableView, QPushButton
from PyQt5.QtGui import QColor, QPixmap
from openbb_terminal.sdk import openbb
#import requests
import itertools
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import request

class Satoshi(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('The Satoshi Terminal')
        '''
        self.setGeometry(100,100,800,600)
        logo = QLabel(self)
        pixmap = QPixmap("./Satoshi-logo.png")
        logo.setPixmap(pixmap)
        logo.setFixedSize(pixmap.width(), pixmap.height())
        '''
        # discovery coins
        self.button_discovery_coins = QPushButton('Discover Coins')
        self.button_discovery_coins.clicked.connect(self.discover_coins)

        # DeFi data
        self.button_coins_list = QPushButton('DeFi')
        self.button_coins_list.clicked.connect(self.coins_list)

        # Crypto headline
        self.button_headlines = QPushButton('Crypto Headlines')
        self.button_headlines.clicked.connect(self.crypto_headlines)

        # Economic News
        '''''
        self.button_news = QPushButton('Economic News')
        self.button_news.clicked.connect(self.economic_news)
        '''
        # Exit application
        self.button_exit = QPushButton('Exit')
        self.button_exit.clicked.connect(self.close_application)

        # Create a label to display the message. Used for any error messages
        self.label = QLabel('')
        color = QColor(255,0,0) # red color
        self.label.setStyleSheet("color: {}".format(color.name()))

        # Create a layout to organize the UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.button_discovery_coins)
        layout.addWidget(self.button_coins_list)
        layout.addWidget(self.button_headlines)
        layout.addWidget(self.label) #display error messages
        self.textarea = QTextEdit()
        self.textarea.setOverwriteMode(True)
        self.textarea.toHtml()
        layout.addWidget(self.textarea)
        layout.addWidget(self.button_exit)
        self.setLayout(layout)
    '''''    
    def economic_news(self):
        openbb.root.news(term: str="", sources: str="", sort: str="published")    
    '''''
    def crypto_headlines(self):
        result = request(f"https://api.finbrain.tech/v0/sentiments/USDC")
        sentiment = pd.DataFrame()
        if result.status_code != 200:
            #error message
            self.label.setText("Connection Error with status code " + str(result.status_code))
        else:
            self.label.setText("Displaying headlines on dataframe")

    def coins_list(self):
        coins_list = openbb.crypto.ov.coin_list()
        str_coins_list = str(coins_list)
        self.textarea.setText(str_coins_list)
        
    def discover_coins(self):
        '''
        self.label.setText('Welcome to Satoshi Terminal Beta Version Powered By OpenBB')
        '''
        coinstupple = openbb.crypto.disc.coins()
        str_coinstupple = str(coinstupple)
        #self.textarea.append(str_coinstupple)
        self.textarea.setText(str_coinstupple)
        '''
        view = QTableView()
        view.setModel(coinstupple)
        view.show()
        '''

    def close_application(self):
        window.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Satoshi()
    #screen = QDesktopWidget().screenGeometry()
    window.setGeometry(QDesktopWidget().screenGeometry())
    window.show()
    sys.exit(app.exec_())

