import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout, QGraphicsDropShadowEffect, QScrollArea
from PyQt5.QtGui import QPixmap, QFont, QCursor, QColor
from PyQt5 import QtGui, QtCore
from utils import read_file

widgets = []

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
    print(widgets)
    for widget in widgets:
        if isinstance(widget, QWidget) or isinstance(widget, QScrollArea):
            widget.deleteLater()
    widgets.clear() 
    
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
            
def scan_books(books, libraries, num_days):
    print('Starting the sign-up and scanning process...')
    # AQUI VAI SER A IMPLEMENTAÇÃO DO ALGORITMO DE SIGNUP E SCAN
             
def main_menu(error=""):
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(120, 120)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setStyleSheet('margin-left: 120px; margin-bottom: 20px;')
    widgets.append(logo)

    title = QLabel('Book Scanning')
    title.setStyleSheet('font-size: 50px; font-weight: bold; color: white; margin-right: 120px; margin-bottom: 20px;')
    title.setFont(QFont('Segoe UI Black', 50))
    widgets.append(title)

    title_box = QHBoxLayout()
    title_box.addWidget(logo)
    title_box.addWidget(title)
    layout.addLayout(title_box)

    import_button = create_button('Import Libraries')
    import_button.clicked.connect(import_libraries)
    widgets.append(import_button)
    layout.addWidget(import_button, alignment=QtCore.Qt.AlignCenter)
    
    if error:
        error_label = QLabel(error)
        error_label.setStyleSheet('font-size: 20px; font-weight: bold; color: red; margin-bottom: 20px;')
        widgets.append(error_label)
        layout.addWidget(error_label, alignment=QtCore.Qt.AlignCenter)

    quit_button = create_button('Quit')
    quit_button.clicked.connect(app.quit)
    widgets.append(quit_button)
    layout.addWidget(quit_button, alignment=QtCore.Qt.AlignCenter)
    
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
    # logo, general info and scan button
    top_layout = QHBoxLayout()
    
    # logo
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(60, 60)
    logo = QLabel()
    logo.setStyleSheet('margin-bottom: 30px;')
    logo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    logo.setPixmap(image)
    widgets.append(logo)
    top_layout.addWidget(logo)
    
    logo.mousePressEvent = lambda _: show_main_menu()
    
    # general info  
    general_info = QLabel(f'Number of books: {len(books)}\nNumber of libraries: {len(libraries)}\nNumber of days: {num_days}')
    general_info.setStyleSheet('font-size: 15px; font-weight: bold; color: white; margin-right: 150px; margin-left: 25px; margin-bottom: 30px;')
    widgets.append(general_info)
    top_layout.addWidget(general_info)
    
    # scan button
    scan_button = create_button('Scan Books')
    scan_button.clicked.connect(lambda: scan_books(books, libraries, num_days))
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    scan_button.setGraphicsEffect(effect)
    widgets.append(scan_button)
    top_layout.addWidget(scan_button, alignment=QtCore.Qt.AlignRight)
    
    # libraries and books
    bottom_layout = QHBoxLayout()
    
    # libraries (scrollable)
    libraries_layout = QVBoxLayout()  
    libraries_label = QLabel('Libraries')
    libraries_label.setStyleSheet('font-size: 25px; font-weight: bold; color: white;')
    libraries_layout.addWidget(libraries_label, alignment=QtCore.Qt.AlignCenter)
    widgets.append(libraries_label)

    libraries_list = QScrollArea()
    libraries_list.setFixedWidth(350)
    libraries_list.setFixedHeight(400)
    libraries_list.setWidgetResizable(True)
    libraries_list.setStyleSheet('background: #684756; margin-bottom: 20px; padding: 0; border: 0;')
    libraries_list_content = QWidget(libraries_list)
    widgets.append(libraries_list)
    libraries_list_content.setStyleSheet('padding: 0; margin: 0;')
    libraries_list_layout = QVBoxLayout(libraries_list_content)
    libraries_list_layout.setAlignment(QtCore.Qt.AlignTop)

    for i in range(len(libraries)):
        label = QLabel(f'Library {i}\nSignup time: {libraries[i].signup_time}\nBooks per day: {libraries[i].books_per_day}\n\nBooks: {", ".join([f"{book.id}" for book in libraries[i].books])}')
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)  
        label.setWordWrap(True)
        label_height = 93 + ((42 + 3*len(libraries[i].books)) // 36) * 18
        label.setStyleSheet('font-size: 15px; font-weight: bold; color: white; padding: 10px; border-radius: 10px; border: 2px solid white; margin-bottom: 10px;')
        label.setMinimumHeight(label_height)
        label.adjustSize()
        libraries_list_layout.addWidget(label)
        
    widgets.append(libraries_list_content)

    libraries_list_content.setLayout(libraries_list_layout)
    libraries_list.setWidget(libraries_list_content)
    
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    libraries_list.setGraphicsEffect(effect)
    
    libraries_layout.addWidget(libraries_list, alignment=QtCore.Qt.AlignCenter)

   # books (scrollable)
    books_layout = QVBoxLayout()  
    books_label = QLabel('Books')
    books_label.setStyleSheet('font-size: 25px; font-weight: bold; color: white;')
    books_layout.addWidget(books_label, alignment=QtCore.Qt.AlignCenter)
    widgets.append(books_label)
    
    books_list = QScrollArea()
    books_list.setFixedWidth(350)
    books_list.setFixedHeight(400)
    books_list.setWidgetResizable(True)
    books_list.setStyleSheet('background: #684756; margin-bottom: 20px; padding: 0; border: 0;')
    books_list_content = QWidget(books_list)
    books_list_content.setStyleSheet('padding: 0; margin: 0;')
    widgets.append(books_list)
    books_list_layout = QVBoxLayout(books_list_content)
    books_list_layout.setAlignment(QtCore.Qt.AlignTop)
    
    for i in range(len(books)):
        label = QLabel(f'Book {i}\nScore: {books[i].score}')
        label.setStyleSheet('font-size: 15px; font-weight: bold; color: white; padding: 10px; border-radius: 10px; border: 2px solid white; margin-bottom: 10px;')
        books_list_layout.addWidget(label)
        
    books_list_content.setLayout(books_list_layout)
    books_list.setWidget(books_list_content)
    
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    books_list.setGraphicsEffect(effect)
    
    books_layout.addWidget(books_list, alignment=QtCore.Qt.AlignCenter)
    
    bottom_layout.addLayout(libraries_layout)
    bottom_layout.addLayout(books_layout)    
          
    layout.addLayout(top_layout)
    layout.addLayout(bottom_layout)
        
main_menu()

window.setLayout(layout)

window.show()
sys.exit(app.exec())
