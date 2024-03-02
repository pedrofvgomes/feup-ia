import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QCursor, QColor
from PyQt5 import QtGui, QtCore


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Book Scanning')
    window.setFixedWidth(800)
    window.setFixedHeight(600)
    window.setStyleSheet('background: #3d314a;')
    window.setWindowIcon(QtGui.QIcon('proj/assets/books.png'))
    
    grid = QGridLayout()
    
    image = QPixmap('proj/assets/books.png')
    image = image.scaled(100, 100)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setStyleSheet('margin-left: 140px; margin-right: 20px;')
    
    title = QLabel('Book Scanning')
    title.setStyleSheet('font-size: 50px; font-weight: bold; color: white; margin-left: 0;')
        
    button = QPushButton('Import Libraries')
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('QPushButton{ color: white; background: #684756; font-size: 30px; font-weight: bold; padding: 15px 30px; border-radius: 25px; margin-top: 0;} QPushButton:hover{background: #705665;}')
    button.setFixedWidth(350)
    
    effect = QGraphicsDropShadowEffect()
    effect.setBlurRadius(30)
    effect.setColor(QColor(0, 0, 0, 50))
    effect.setOffset(0, 4)
    button.setGraphicsEffect(effect)
    
    logo_title_layout = QHBoxLayout()
    logo_title_layout.addWidget(logo)
    logo_title_layout.addWidget(title)
    logo_title_layout.setContentsMargins(0, 0, 0, 0)
    
    grid.addLayout(logo_title_layout, 0, 0, 1, 1)
    grid.addWidget(button, 1, 0, 1, 2, alignment=QtCore.Qt.AlignCenter)
    
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    main()
