import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit
from openbb_terminal.sdk import openbb
import requests
import itertools

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



        # Create a label to display the message
        self.label = QLabel('asfsdaf')

        # Create a layout to organize the UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.button_discovery_coins)
        layout.addWidget(self.button_coins_list)
        #layout.addWidget(self.label)
        self.textarea = QTextEdit()
        self.textarea.setOverwriteMode(True)
        layout.addWidget(self.textarea)
        self.setLayout(layout)
        

    def coins_list(self):
        coins_list = openbb.crypto.ov.coin_list()
        str_coins_list = str(coins_list)
        #self.textarea.append(str_coins_list)
        self.textarea.setText(str_coins_list)
        #print(coins_list)    

    def discover_coins(self):
        '''
        self.label.setText('Welcome to Satoshi Terminal Beta Version Powered By OpenBB')
        '''
        coinstupple = openbb.crypto.disc.coins()
        str_coinstupple = str(coinstupple)
        #self.textarea.append(str_coinstupple)
        self.textarea.setText(str_coinstupple)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Satoshi()
    window.show()
    sys.exit(app.exec_())

