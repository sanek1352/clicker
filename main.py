
import sys
from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

USERS_FILE = 'users.txt'
CLICKS_FILE = 'clicks.txt'

class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Реєстрація")
        self.setGeometry(100, 100, 300, 150)
        self.login = None

        self.layout = QVBoxLayout()

        self.login_label = QLabel("Логін:")
        self.login_input = QLineEdit()

        self.pass_label = QLabel("Пароль:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Зареєструватися")
        self.register_button.clicked.connect(self.register_user)

        self.layout.addWidget(self.login_label)
        self.layout.addWidget(self.login_input)
        self.layout.addWidget(self.pass_label)
        self.layout.addWidget(self.pass_input)
        self.layout.addWidget(self.register_button)


        self.setLayout(self.layout)

    def register_user(self):
        login = self.login_input.text().strip()
        password = self.pass_input.text().strip()

        if not login or not password:
            QMessageBox.warning(self, "Помилка", "Будь ласка, заповніть усі поля.")
            return

        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    saved_login = line.split(':')[0]
                    if login == saved_login:
                        QMessageBox.warning(self, "Помилка", "Користувач з таким логіном вже існує.")
                        return
        except FileNotFoundError:
            pass

        with open(USERS_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{login}:{password}\n")

        self.login = login
        QMessageBox.information(self, "Успіх", "Реєстрація пройшла успішно!")
        self.accept()


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизація")
        self.setGeometry(100, 100, 300, 150)
        self.login = None
        self.password = None

        self.layout = QVBoxLayout()

        self.login_label = QLabel("Логін:")
        self.login_input = QLineEdit()

        self.pass_label = QLabel("Пароль:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Увійти")
        self.login_button.clicked.connect(self.login_user)

        self.layout.addWidget(self.login_label)
        self.layout.addWidget(self.login_input)
        self.layout.addWidget(self.pass_label)
        self.layout.addWidget(self.pass_input)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login_user(self):
        login = self.login_input.text().strip()
        password = self.pass_input.text().strip()

        if not login or not password:
            QMessageBox.warning(self, "Помилка", "Будь ласка, заповніть усі поля.")
            return

        # Перевірка на існуючий логін і пароль в users.txt
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                users = f.readlines()
                found_user = False
                for line in users:
                    saved_login, saved_password = line.strip().split(':')
                    if saved_login == login and saved_password == password:
                        found_user = True
                        self.login = login
                        self.password = password
                        break
                if not found_user:
                    QMessageBox.warning(self, "Помилка", "Невірний логін або пароль.")
                    return
        except FileNotFoundError:
            QMessageBox.warning(self, "Помилка", "Файл користувачів не знайдено.")
            return

        # Завантаження кількості кліків після успішної авторизації


        QMessageBox.information(self, "Успіх", "Ви успішно авторизувалися!")
        self.accept()




class clicked(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.click = 0
        self.upgrade = 1
        self.rebirth = 2
        self.rebirth_mult = 1
        self.rebirth_price = 100
        self.price = 10
        self.current_user = None

        try:
            with open("stule.css") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            pass

        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_field = QLabel("Clicks : 0")
        self.upgrade_label = QLabel("Upgrade : 1")
        self.user_label = QLabel("Користувач: Не зареєстровано")

        self.button = QPushButton("")
        self.upgrade_button = QPushButton("")
        self.rebirth_button = QPushButton("")
        self.register_button = QPushButton("")
        self.login_button = QPushButton("")

        self.button.setIcon(QIcon('s.png'))
        self.upgrade_button.setIcon(QIcon('c.jpg'))
        self.rebirth_button.setIcon(QIcon('a.jfif'))
        self.login_button.setIcon(QIcon('n.jpg'))
        self.register_button.setIcon(QIcon('y.jpg'))

        self.button.setIconSize(QSize(150, 150))
        self.upgrade_button.setIconSize(QSize(150, 150))
        self.rebirth_button.setIconSize(QSize(100, 100))
        self.login_button.setIconSize(QSize(100, 100))
        self.register_button.setIconSize(QSize(100, 100))

        self.button.clicked.connect(self.on_click)
        self.button.clicked.connect(lambda: self.animate_button(self.button))
        self.upgrade_button.clicked.connect(self.on_upgrate)
        self.rebirth_button.clicked.connect(self.on_rebirth)
        self.register_button.clicked.connect(self.open_register_dialog)
        self.login_button.clicked.connect(self.open_login_dialog)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.upgrade_button)
        self.layout.addWidget(self.upgrade_label)
        self.layout.addWidget(self.rebirth_button)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.login_button)

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
        anim.setEndValue(QSize(150, 150))
        anim.start()
        button.anim = anim

    def on_upgrate(self) -> None:
        if self.click >= self.price:
            self.click -= self.price
            self.price *= 4
            self.upgrade *= 2
            self.upgrade_label.setText(f"Upgrade : {self.upgrade}")
            self.input_field.setText(f"Clicks : {self.click}")

    def on_rebirth(self) -> None:
        if self.click >= self.rebirth_price:
            self.rebirth *= 100
            self.click = 0
            self.upgrade = 1
            self.rebirth_mult = 20
            self.rebirth_price *= 2  # Можна додати збільшення ціни rebirth
            self.upgrade_label.setText(f"Upgrade : {self.upgrade}")
            self.input_field.setText(f"Clicks : {self.click}")
            self.button.setIcon(QIcon('b.jfif'))

    def open_register_dialog(self):
        dialog = RegisterWindow()
        if dialog.exec_() == QDialog.Accepted:
            self.current_user = dialog.login
            self.user_label.setText(f"Користувач: {dialog.login}")
            self.load_user_data()

    def open_login_dialog(self):
        dialog = LoginWindow()
        if dialog.exec_() == QDialog.Accepted:
            self.current_user = dialog.login
            self.user_label.setText(f"Користувач: {dialog.login}")
            self.load_user_data()

    def load_user_data(self):
        try:
            with open(CLICKS_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    login, click, upgrade, rebirth, rebirth_mult, rebirth_price, price = line.strip().split(':')
                    if login == self.current_user:
                        self.click = int(click)
                        self.upgrade = int(upgrade)
                        self.rebirth = int(rebirth)
                        self.rebirth_mult = int(rebirth_mult)
                        self.rebirth_price = int(rebirth_price)
                        self.price = int(price)
                        break
        except FileNotFoundError:
            pass

        self.update_ui()

    def save_user_data(self):
        if not self.current_user:
            return
        lines = []
        try:
            with open(CLICKS_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            pass

        with open(CLICKS_FILE, 'w', encoding='utf-8') as f:
            found = False
            for line in lines:
                login, *_ = line.strip().split(':')
                if login == self.current_user:
                    f.write(f"{self.current_user}:{self.click}:{self.upgrade}:{self.rebirth}:{self.rebirth_mult}:{self.rebirth_price}:{self.price}\n")
                    found = True
                else:
                    f.write(line)
            if not found:
                f.write(f"{self.current_user}:{self.click}:{self.upgrade}:{self.rebirth}:{self.rebirth_mult}:{self.rebirth_price}:{self.price}\n")

    def update_ui(self):
        self.input_field.setText(f"Clicks : {self.click}")
        self.upgrade_label.setText(f"Upgrade : {self.upgrade}")

    def closeEvent(self, event):
        self.save_user_data()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = clicked()
    window.show()
    sys.exit(app.exec_())