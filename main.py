import sys

from PyQt6.QtWidgets import QApplication

from app import Calc


# Запуск приложения
app = QApplication(sys.argv)
window = Calc()
window.show()
sys.exit(app.exec())
