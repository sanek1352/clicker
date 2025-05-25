import sys

from PyQt5.QtWidgets import *

class clicked(QWidget):
    def __init__(self) ->None:
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.button = QPushButton("+1")

        self.button.clicked.connect(self.on_click)

        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
    def on_click(self) -> None:
        ...

app = QApplication(sys.argv)
window = clicked()
sys.exit(app.exec_())