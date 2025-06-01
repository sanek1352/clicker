import sys

from PyQt5.QtWidgets import *

class clicked(QWidget):
    def __init__(self) ->None:
        super().__init__()
        self.click = 0
        self.upgrade = 1
        self.price = 10
        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_field = QLabel("Clicks : 0")
        self.upgrade_label = QLabel("Upgrade : 1")

        self.button = QPushButton("+1")
        self.upgrade_button = QPushButton("upgrade")

        self.button.clicked.connect(self.on_click)
         # self.input_field.clicked.connect(self.click)
        self.upgrade_button.clicked.connect(self.on_upgrate)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.upgrade_button)
        self.layout.addWidget(self.upgrade_label)

        self.setLayout(self.layout)
    def on_click(self) -> None:
        self.click += self.upgrade

        self.input_field.setText(f"Clicks : {self.click}")

    def on_upgrate(self) -> None:
        if self.click > self.price:
           self.click -= self.price
           self.price *=4
           self.upgrade = self.upgrade * 2
           self.upgrade_label.setText(f"upgrate : {self.upgrade}")


app = QApplication(sys.argv)
window = clicked()
sys.exit(app.exec_())