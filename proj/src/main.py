import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGraphicsDropShadowEffect, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QCursor, QColor, QFont
from PyQt5 import QtGui, QtCore


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Book Scanning')
    window.setFixedWidth(800)
    window.setFixedHeight(600)
    window.setStyleSheet('background: #3d314a;')
    window.setWindowIcon(QtGui.QIcon('proj/assets/books.png'))

    main_layout = QVBoxLayout()
    main_layout.setSpacing(35)

    image = QPixmap('proj/assets/books.png')
    image = image.scaled(120, 120)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setStyleSheet('margin-left: 120px;')

    title = QLabel('Book Scanning')
    title.setStyleSheet('font-size: 50px; font-weight: bold; color: white; margin-right: 120px;')
    title.setFont(QFont('Segoe UI Black', 50))

    title_layout = QHBoxLayout()
    title_layout.addWidget(logo, alignment=QtCore.Qt.AlignCenter)
    title_layout.addWidget(title, alignment=QtCore.Qt.AlignCenter)

    main_layout.addLayout(title_layout)

    import_libraries = QPushButton('Import Libraries')
    import_libraries.setFont(QFont('Segoe UI Black', 30))
    import_libraries.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    import_libraries.setStyleSheet('QPushButton{ color: white; background: #684756; font-size: 30px; font-weight: bold; padding: 15px 30px; border-radius: 25px;} QPushButton:hover{background: #705665;}')

    quit_button = QPushButton('Quit')
    quit_button.setFont(QFont('Segoe UI Black', 30))
    quit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    quit_button.setStyleSheet('QPushButton{ color: white; background: #684756; font-size: 30px; font-weight: bold; padding: 15px 30px; border-radius: 25px;} QPushButton:hover{background: #705665;}')

    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    import_libraries.setGraphicsEffect(effect)
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    quit_button.setGraphicsEffect(effect)

    button_layout = QVBoxLayout()
    button_layout.addWidget(import_libraries, alignment=QtCore.Qt.AlignCenter)
    button_layout.addWidget(quit_button, alignment=QtCore.Qt.AlignCenter)

    main_layout.addLayout(button_layout)
    main_layout.setAlignment(QtCore.Qt.AlignCenter)

    window.setLayout(main_layout)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
