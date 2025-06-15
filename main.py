import sys

from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *

class clicked(QWidget):
    def __init__(self) ->None:
        super().__init__()
        self.click = 0
        self.upgrade = 1
        self.rebirth = 2
        self.rebirth_mult = 1
        self.rebirth_price = 100
        self.price = 10
        with open("stule.css") as f:
            self.setStyleSheet(f.read())
        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_field = QLabel("Clicks : 0")
        self.upgrade_label = QLabel("Upgrade : 1")

        self.button = QPushButton("")
        self.upgrade_button = QPushButton("")
        self.rebirth_button = QPushButton("")
        self.label = QLabel(self)
        self.button.setIcon(QIcon('s.png'))
        self.upgrade_button.setIcon(QIcon('c.jpg'))
        self.rebirth_button.setIcon(QIcon('a.jfif'))
        self.button.setIconSize(QSize(150, 150))
        self.upgrade_button.setIconSize(QSize(150, 150))
        self.rebirth_button.setIconSize(QSize(100, 100))

        # self.pixmap = QPixmap('s.png')


        # self.label.setPixmap(self.pixmap)

        self.button.clicked.connect(self.on_click)
        self.button.clicked.connect(lambda: self.animate_button(self.button))
         # self.input_field.clicked.connect(self.click)
        self.upgrade_button.clicked.connect(self.on_upgrate)
        self.rebirth_button.clicked.connect(self.on_rebirth)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.upgrade_button)
        self.layout.addWidget(self.upgrade_label)
        self.layout.addWidget(self.rebirth_button)
        # self.layout.addWidget(self.label)
        # self.label.setFixedSize(10,10)
        self.setLayout(self.layout)
    def on_click(self) -> None:
        self.click += self.upgrade * self.rebirth_mult

        self.input_field.setText(f"Clicks : {self.click}")
    @staticmethod
    def animate_button(button):
        anim = QPropertyAnimation(button, b"iconSize")
        anim.setDuration(100)
        anim.setStartValue(QSize(150, 150))
        anim.setKeyValueAt(0.5, QSize(130, 130))
        anim.setEndValue(QSize(150,150))
        anim.start()
        button.anim = anim

    def on_upgrate(self) -> None:
        if self.click > self.price:
           self.click -= self.price
           self.price *=4
           self.upgrade = self.upgrade * 2
           self.upgrade_label.setText(f"upgrate : {self.upgrade}")

    def on_rebirth(self) -> None:
        if self.click > self.rebirth:
            self.rebirth = self.rebirth * 100
            self.click = 0
            self.upgrade = 1
            self.rebirth_mult = 20
            self.upgrade_label.setText(f"upgrate : {self.upgrade}")
            self.button.setIcon(QIcon('b.jfif'))


app = QApplication(sys.argv)
window = clicked()
sys.exit(app.exec_())