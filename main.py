import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QCheckBox, QRadioButton, QMessageBox
)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Простое приложение на PyQt5')
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)

        # Создание виджетов
        self.label_name = QLabel('Имя:')
        self.input_name = QLineEdit()

        self.label_age = QLabel('Возраст:')
        self.input_age = QLineEdit()

        self.label_email = QLabel('Email:')
        self.input_email = QLineEdit()

        self.checkbox_terms = QCheckBox('Согласен с условиями')
        self.radiobutton_male = QRadioButton('Мужской')
        self.radiobutton_female = QRadioButton('Женский')

        self.button_submit = QPushButton('Отправить')
        self.button_clear = QPushButton('Очистить')

        # Установка обработчиков событий
        self.button_submit.clicked.connect(self.submit_form)
        self.button_clear.clicked.connect(self.clear_form)

        # Установка компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.label_age)
        layout.addWidget(self.input_age)
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(self.checkbox_terms)
        layout.addWidget(self.radiobutton_male)
        layout.addWidget(self.radiobutton_female)
        layout.addWidget(self.button_submit)
        layout.addWidget(self.button_clear)

        self.setLayout(layout)

    def submit_form(self):
        try:
            name = self.input_name.text()
            age = int(self.input_age.text())
            email = self.input_email.text()

            if not self.checkbox_terms.isChecked():
                raise ValueError("Необходимо согласие с условиями")

            QMessageBox.information(self, 'Успех', f'Имя: {name}\nВозраст: {age}\nEmail: {email}')
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', 'Произошла ошибка: ' + str(e))

    def clear_form(self):
        self.input_name.clear()
        self.input_age.clear()
        self.input_email.clear()
        self.checkbox_terms.setChecked(False)
        self.radiobutton_male.setChecked(False)
        self.radiobutton_female.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
