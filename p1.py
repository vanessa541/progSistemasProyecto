# Importar bibliotecas

import json
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, \
    QLabel, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap


# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi buscador de peliculas")
        self.resize(2000, 1000)
        self.contenedor = QWidget()
        self.lytPrincipal = QGridLayout()

        lblBusca = QLabel("Palabras: ")
        self.lnedtTexto = QLineEdit()
        self.btnBusca = QPushButton("Buscar")
        self.btnBusca.clicked.connect(self.split_text)

        self.texto = QPlainTextEdit()

        leftcolumna = QWidget()
        centercolumna = QWidget()
        rightcolumna = QWidget()

        self.lytPrincipal.addWidget(lblBusca, 0, 0)
        self.lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        self.lytPrincipal.addWidget(self.btnBusca, 0, 2)
        self.lytPrincipal.addWidget(leftcolumna, 1, 0)
        self.lytPrincipal.addWidget(centercolumna, 1, 1)
        self.lytPrincipal.addWidget(rightcolumna, 1, 2)

        self.contenedor.setLayout(self.lytPrincipal)
        self.setCentralWidget(self.contenedor)

    def split_text(self):
        palabras = []
        lista = self.lnedtTexto.text()
        print(lista)
        for palabras in lista:
            palabras = lista.split(",")
        for i in palabras:
            self.get_movies(i)


    def get_movies(self, palabra):
        url_servicio = "http://clandestina-hds.com:80/movies/title?search="
        r = requests.get(url_servicio + palabra)
        peliculas_data = r.json()
        index = 0
        limit = 4
        short_data_peliculas = peliculas_data['results'][:3]
        for pelicula in short_data_peliculas:
            print("La pelicula de nombre: {} \n Tiene una URL de imagen: {} \n Resumen :{} \n Aritstas: {}" .format(pelicula['title'],
                                                                                    pelicula["image"],
                                                                                    pelicula['plot'],
                                                                                    pelicula['starList']))
            image = Poster(pelicula["image"])
            resume = QTextEdit()
            resume.setText(pelicula['plot'])
            self.lytPrincipal.addWidget(image)
            self.lytPrincipal.addWidget(resume)
            self.contenedor.setLayout(self.lytPrincipal)
            self.setCentralWidget(self.contenedor)
            index = index + 1
            if index == limit:
                break



    def serch_text(self):
        cursor = self.texto.textCursor()
        cursor.setPosition(0)
        self.texto.setTextCursor(cursor)
        cadena = self.lnedtTexto.text()
        escrito = self.texto.find(cadena)
        print("Película: ", escrito)

class Poster(QLabel):
    image_url: str

    def __init__(self, image_url: str):
        super().__init__()
        self.image_url = image_url
        image = QImage()
        image.loadFromData(requests.get(self.image_url).content)
        pixmap = QPixmap(image)
        pixmap = pixmap.scaledToWidth(200)
        self.setPixmap(pixmap)

    # def mouseDoubleClickEvent(self, event):
    #     if self.video_url is not None and self.video_url is not "":
    #         url = QUrl(self.video_url)
    #         QDesktopServices.openUrl(url)


app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()
