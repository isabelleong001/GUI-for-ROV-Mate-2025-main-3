from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import time

# Step 1: Create a Worker class
class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    @Slot()
    def run(self):
        # Long-running task
        for i in range(5):
            time.sleep(1)  # Simulate work
            self.progress.emit(i + 1)
        self.finished.emit()

# Step 2: Create main application window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread Example")

        self.label = QLabel("Starting...")
        self.button = QPushButton("Start Thread")
        self.button.clicked.connect(self.start_thread)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.worker = None
        self.thread = None

    def start_thread(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.update_label)

        self.thread.start()
        self.button.setEnabled(False)

        self.thread.finished.connect(lambda: self.button.setEnabled(True))

    def update_label(self, value):
        self.label.setText(f"Progress: {value}/5")

# Step 3: Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()