from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout, QLabel, QTabWidget, QLineEdit
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)

        self.setCentralWidget(self.lineedit)

    def return_pressed(self):
        print("Return pressed!")
        self.lineedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_changed(self, text):
        print("Text changed...")
        print(text)

    def text_edited(self, text):
        print("Text edited...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec())
