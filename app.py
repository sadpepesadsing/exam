from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QTextEdit, QLabel, QWidget


class Calc(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 400)

        # Компоновка
        self.layout = QVBoxLayout(self)

        # Поле редактирования текста
        self.text_edit1 = QTextEdit(self)
        self.layout.addWidget(self.text_edit1)

        self.text_edit2 = QTextEdit(self)
        self.layout.addWidget(self.text_edit2)

        # Кнопки "Сохранить" и "Отмена"
        save_button = QPushButton("перевести", self)
        self.layout.addWidget(save_button)

        # Подключение сигналов
        save_button.clicked.connect(self.go)

    def go(self):
        a = 0
        if self.text_edit2.toPlainText().lower() == 'f':
            a = int(self.text_edit1.toPlainText()) * 9 / 5 + 32
        elif self.text_edit2.toPlainText().lower() == 'k':
            a = int(self.text_edit1.toPlainText()) + 273.5
        else:
            a = 'Введите f или k'
        widget = QWidget()

        self.textLabel = QLabel(widget)
        self.textLabel.setText(str(a))
        self.layout.addWidget(self.textLabel)
