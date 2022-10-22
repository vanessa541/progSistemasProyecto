# Importar bibliotecas

import json
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, \
    QLabel
from PyQt5.QtGui import QImage, QPixmap

# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi buscador de peliculas")
        self.resize(1000, 800)
        contenedor = QWidget()
        lytPrincipal = QGridLayout()

        lblBusca = QLabel("Palabras: ")
        self.lnedtTexto = QLineEdit()
        btnBusca = QPushButton("Buscar")
        btnBusca.clicked.connect(self.buscarTexto)

        self.texto = QPlainTextEdit()

        lytPrincipal.addWidget(lblBusca, 0, 0)
        lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        lytPrincipal.addWidget(btnBusca, 0, 2)
        lytPrincipal.addWidget(self.texto, 1, 0, 1, 40)

        url_image = 'https://m.media-amazon.com/images/M/MV5BNjk2ODQzNDYxNV5BMl5BanBnXkFtZTgwMTcyNDg4NjE@._V1_Ratio0.6837_AL_.jpg'

        image = QImage()
        image.loadFromData(requests.get(url_image).content)

        image_label = QLabel()
        pixmap = QPixmap(image)
        pixmap2 = pixmap.scaledToWidth(200)
        image_label.setPixmap(pixmap2)
        lytPrincipal.addWidget(image_label)
        contenedor.setLayout(lytPrincipal)
        self.setCentralWidget(contenedor)


    def buscarTexto(self):

        cadena = self.lnedtTexto.text()
        print("Escrito: ", cadena)




app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()