import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont, QCursor, QColor
from PyQt5 import QtGui, QtCore
from utils import read_file

widgets = {
    "logo": [],
    "title": [],
    "import": [],
    "error": [],
    "quit": [],
}

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Book Scanning')
window.setFixedWidth(800)
window.setFixedHeight(600)
window.setStyleSheet('background: #3d314a;')
window.setWindowIcon(QtGui.QIcon('proj/assets/books.png'))

layout = QVBoxLayout()
layout.setAlignment(QtCore.Qt.AlignCenter)

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for _ in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_main_menu(error=""):
    clear_widgets()
    main_menu(error)
    
def show_library_menu(books, libraries, num_days):
    clear_widgets()
    library_menu(books, libraries, num_days)
    
def create_button(text):
    button = QPushButton(text)
    button.setFont(QFont('Segoe UI Black', 30))
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('QPushButton{ color: white; background: #684756; font-size: 30px; font-weight: bold; padding: 15px 30px; border-radius: 25px; margin-bottom: 20px; } QPushButton:hover{background: #705665;}')
    button.setFixedWidth(300)
    return button

def import_libraries():
    filename = QFileDialog.getOpenFileName(window, 'Import Libraries', 'proj/', 'Text Files (*.txt)')[0]
    if filename:
        clear_widgets()
        try:
            [books, libraries, num_days] = read_file(filename)
            if libraries:
                print('top!')
                show_library_menu(books, libraries, num_days)
            else:
                show_main_menu('Error: Invalid file')
        except:
            show_main_menu('Error: Invalid file')
             
def main_menu(error=""):
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(120, 120)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setStyleSheet('margin-left: 120px; margin-bottom: 20px;')
    widgets["logo"].append(logo)

    title = QLabel('Book Scanning')
    title.setStyleSheet('font-size: 50px; font-weight: bold; color: white; margin-right: 120px; margin-bottom: 20px;')
    title.setFont(QFont('Segoe UI Black', 50))
    widgets["title"].append(title)

    title_box = QHBoxLayout()
    title_box.addWidget(widgets["logo"][-1])
    title_box.addWidget(widgets["title"][-1])
    layout.addLayout(title_box)

    import_button = create_button('Import Libraries')
    import_button.clicked.connect(import_libraries)
    widgets["import"].append(import_button)
    layout.addWidget(widgets["import"][-1], alignment=QtCore.Qt.AlignCenter)
    
    if error:
        error_label = QLabel(error)
        error_label.setStyleSheet('font-size: 20px; font-weight: bold; color: red; margin-bottom: 20px;')
        widgets["error"].append(error_label)
        layout.addWidget(widgets["error"][-1], alignment=QtCore.Qt.AlignCenter)

    quit_button = create_button('Quit')
    quit_button.clicked.connect(app.quit)
    widgets["quit"].append(quit_button)
    layout.addWidget(widgets["quit"][-1], alignment=QtCore.Qt.AlignCenter)
    
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    import_button.setGraphicsEffect(effect)
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    quit_button.setGraphicsEffect(effect)
    
def library_menu(books, libraries, num_days):
    general_info = QLabel(f'Number of books: {len(books)}\nNumber of libraries: {len(libraries)}\nNumber of days: {num_days}')
    general_info.setStyleSheet('font-size: 20px; font-weight: bold; color: white; margin-bottom: 20px;')
    layout.addWidget(general_info, alignment=QtCore.Qt.AlignCenter)
    
        
main_menu()

window.setLayout(layout)

window.show()
sys.exit(app.exec())
