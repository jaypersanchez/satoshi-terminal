import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit, QDesktopWidget, QTableView
from openbb_terminal.sdk import openbb
import requests
import itertools
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt

class Satoshi(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('The Satoshi Terminal')

        # discovery coins
        self.button_discovery_coins = QPushButton('Discover Coins')
        self.button_discovery_coins.clicked.connect(self.discover_coins)

        # DeFi data
        self.button_coins_list = QPushButton('DeFi')
        self.button_coins_list.clicked.connect(self.coins_list)

        # Exit application
        self.button_exit = QPushButton('Exit')
        self.button_exit.clicked.connect(self.close_application)

        # Create a label to display the message. Used for any error messages
        self.label = QLabel('')

        # Create a layout to organize the UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.button_discovery_coins)
        layout.addWidget(self.button_coins_list)
        layout.addWidget(self.label) #display error messages
        self.textarea = QTextEdit()
        self.textarea.setOverwriteMode(True)
        self.textarea.toHtml()
        layout.addWidget(self.textarea)
        layout.addWidget(self.button_exit)
        self.setLayout(layout)
        

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

