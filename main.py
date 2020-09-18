from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def on_plus_clicked():
    task_label = QLabel()
    task_layout.addWidget(task_label)
    task_label.setText("Example String")

# Setting up Widgets
app = QApplication([])
window = QWidget()
add_widget = QWidget()
task_widget = QWidget()

# Setting up layouts
window_layout = QHBoxLayout()
add_layout = QVBoxLayout()
add_layout.setAlignment(Qt.AlignTop)
task_layout = QVBoxLayout()
task_layout.setAlignment(Qt.AlignTop)

# Setting up buttons & others
add_button = QPushButton("+")
add_button.setFixedSize(50,50)
add_button.clicked.connect(on_plus_clicked)
task_text_box = QTextEdit()
task_text_box.setFixedHeight(50)
task_text_box.setPlaceholderText("Type your task here...")

# Adding Widgets
window_layout.addWidget(add_widget)
window_layout.addWidget(task_widget)

# Adding to layouts
add_layout.addWidget(add_button)
task_layout.addWidget(task_text_box)

# Setting layouts
window.setLayout(window_layout)
add_widget.setLayout(add_layout)
task_widget.setLayout(task_layout)

window.setWindowTitle("PyToDo")
window.setMinimumSize(800,800)
window.show()
app.exec_()