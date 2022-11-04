# Importar bibliotecas

import json
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, \
    QLabel, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
import threading


def custom_hook(args):
    print(f'Thread failed: {args.exc_value}')


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
        self.leftcolumna = QVBoxLayout()
        self.centercolumna = QVBoxLayout()
        self.rightcolumna = QVBoxLayout()
        self.lytPrincipal.addWidget(lblBusca, 0, 0)
        self.lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        self.lytPrincipal.addWidget(self.btnBusca, 0, 2)
        self.lytPrincipal.addLayout(self.leftcolumna, 1, 0)
        self.lytPrincipal.addLayout(self.centercolumna, 1, 1)
        self.lytPrincipal.addLayout(self.rightcolumna, 1, 2)
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

    def split_texto(self):
        peliculas = []
        palabras = []
        index = 0
        threading.excepthook = custom_hook
        lista = self.inlineText.text()
        for palabras in lista:
            palabras = lista.split(",")
        thread_lst = [threading.Thread(target=self.get_movie, args=(k, index)) for k in palabras]
        for i in thread_lst:
            i.start()
            index += 3
            print("Start")
        for i in thread_lst:
            peliculas.append(i.join())
            print("Return")
        self.resize(750, 800)
        print(self.data_movies)
        # self.draw_movies(self.data_movies, index)


    def get_movies(self, palabra):
            url_servicio = "http://clandestina-hds.com:80/movies/title?search="
            r = requests.get(url_servicio + palabra)
            peliculas_data = r.json()
            index = 0
            limit = 4
            short_data_peliculas = peliculas_data['results'][:4]
            for pelicula in short_data_peliculas:
                print("La pelicula de nombre: {} \n Tiene una URL de imagen: {} \n Resumen :{} \n Aritstas: {}" .format(pelicula['title'],
                                                                                        pelicula["image"],
                                                                                        pelicula['plot'],
                                                                                        pelicula['starList']))
                if 0 <= index < 4:
                    self.leftcolumna.addWidget(image)
                    self.leftcolumna.addWidget(resume)
                if 4 <= index < 8:
                    self.centercolumna.addWidget(image)
                    self.centercolumna.addWidget(resume)
                if index >= 8:
                    self.rightcolumna.addWidget(image)
                    self.rightcolumna.addWidget(resume)
                index += 1
                print(index)
                self.setCentralWidget(self.contenedor)

                # image = Poster(pelicula["image"])
                # resume = QTextEdit()
                # resume.setText(pelicula['plot'])
                # self.lytPrincipal.addWidget(image)
                # self.lytPrincipal.addWidget(resume)
                # self.contenedor.setLayout(self.lytPrincipal)
                # self.setCentralWidget(self.contenedor)
                # index = index + 1
                # if index == limit:
                #     break

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
        pixmap = pixmap.scaledToWidth(300)
        self.setPixmap(pixmap)


app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()
