#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """
    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
            self.inRespuesta = False

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
