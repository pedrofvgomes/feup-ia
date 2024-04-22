import sys, os
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont, QCursor, QColor
from PyQt5 import QtGui, QtCore
from models import Book, Library
from algorithms import read_input_file, apply_greedy_algorithm, apply_simulated_annealing, apply_hill_climbing, apply_genetic_algorithm

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
    global layout
    for widget in widgets:
        if isinstance(widget, QWidget):
            layout.removeWidget(widget)
            widget.deleteLater()
    widgets.clear()

def show_main_menu(error=""):
    clear_widgets()
    main_menu(error)

def create_button(text):
    button = QPushButton(text)
    button.setFont(QFont('Segoe UI Black', 30))
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('QPushButton{ color: white; background: #684756; font-size: 30px; font-weight: bold; padding: 15px 30px; border-radius: 25px; margin-bottom: 20px; } QPushButton:hover{background: #705665;}')
    return button

def import_libraries():
    filename = QFileDialog.getOpenFileName(window, 'Import Libraries', 'proj/data', 'Text Files (*.txt)')[0]
    if filename:
        clear_widgets()
        num_days, libraries = read_input_file(filename)
        if libraries:
            books = get_books_list(libraries)
            library_menu(books, libraries, num_days, filename)
        else:
            show_main_menu('Error: Invalid file')

def get_books_list(libraries):
    # Assuming each library has a 'books' attribute which is a list of Book objects
    books = set()
    for library in libraries:
        books.update(library.books)  # Add books from each library to the set to avoid duplicates
    return list(books)  # Convert the set to a list and return

def apply_algorithm_and_exit(algorithm, input_file, algorithm_name):
    score = algorithm(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    show_main_menu(f'{base_name}_{algorithm_name} successfully created - Score: {score}')

def algorithm_choice_menu(input_file):
    clear_widgets()
    
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(60, 60)
    logo = QLabel()
    logo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet('margin-bottom: 20px;')
    widgets.append(logo)
    layout.addWidget(logo)
    
    logo.mousePressEvent = lambda _: show_main_menu()
    
    label = QLabel("Choose an algorithm")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet('font-size: 25px; color: white;')
    widgets.append(label)
    layout.addWidget(label)

    greddy_button = create_button('Greedy Algorithm')
    greddy_button.clicked.connect(lambda: apply_algorithm_and_exit(apply_greedy_algorithm, input_file, 'greedy'))
    widgets.append(greddy_button)
    layout.addWidget(greddy_button, alignment=QtCore.Qt.AlignCenter)

    simulated_annealing_button = create_button('Simulated Annealing Algorithm')
    simulated_annealing_button.clicked.connect(lambda: apply_algorithm_and_exit(apply_simulated_annealing, input_file, 'simulated_annealing'))
    widgets.append(simulated_annealing_button)
    layout.addWidget(simulated_annealing_button, alignment=QtCore.Qt.AlignCenter)
    
    hill_climbing_button = create_button('Hill Climbing Algorithm')
    hill_climbing_button.clicked.connect(lambda: apply_algorithm_and_exit(apply_hill_climbing, input_file, 'hill_climbing'))
    widgets.append(hill_climbing_button)
    layout.addWidget(hill_climbing_button, alignment=QtCore.Qt.AlignCenter)
    
    genetic_algorithm_button = create_button('Genetic Algorithm')
    genetic_algorithm_button.clicked.connect(lambda: apply_algorithm_and_exit(apply_genetic_algorithm, input_file, 'genetic_algorithm'))
    widgets.append(genetic_algorithm_button)
    layout.addWidget(genetic_algorithm_button, alignment=QtCore.Qt.AlignCenter)

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
        color = 'red' if 'Error' in error else 'green'
        error_label.setStyleSheet(f'font-size: 20px; font-weight: bold; color: {color}; margin-bottom: 20px;')
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
    
def library_menu(books, libraries, num_days, input_name):  
    # logo
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(60, 60)
    logo = QLabel()
    logo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet('margin-bottom: 20px;')
    widgets.append(logo)
    layout.addWidget(logo)
    
    logo.mousePressEvent = lambda _: show_main_menu()
    
    # general info  
    general_info = QLabel(f'Number of books: {len(books)}\nNumber of libraries: {len(libraries)}\nNumber of days: {num_days}')
    general_info.setStyleSheet('font-size: 25px; font-weight: bold; color: white; margin-bottom: 20px;')
    general_info.setAlignment(QtCore.Qt.AlignCenter)
    widgets.append(general_info)
    layout.addWidget(general_info)
    
    # scan button
    scan_button = create_button('Apply Algorithm')
    scan_button.clicked.connect(lambda: algorithm_choice_menu(input_name))
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    scan_button.setGraphicsEffect(effect)
    widgets.append(scan_button)
    layout.addWidget(scan_button, alignment=QtCore.Qt.AlignRight)

main_menu()

window.setLayout(layout)

window.show()
sys.exit(app.exec())
