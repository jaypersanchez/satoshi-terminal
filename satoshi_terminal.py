import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from openbb_terminal.sdk import openbb
import requests

class Satoshi(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('The Satoshi Terminal')

        # Create a button
        self.button_discovery_coins = QPushButton('Discover Coins')
        self.button_discovery_coins.clicked.connect(self.discover_coins)


        # Create a label to display the message
        self.label = QLabel('')

        # Create a layout to organize the UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.button_discovery_coins)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def discover_coins(self):
        '''
        self.label.setText('Welcome to Satoshi Terminal Beta Version Powered By OpenBB')
        '''
        coinstupple = openbb.crypto.disc.coins()
        print(coinstupple)
        '''
        for x in coinstupple:
            print(x)
        '''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Satoshi()
    window.show()
    sys.exit(app.exec_())

