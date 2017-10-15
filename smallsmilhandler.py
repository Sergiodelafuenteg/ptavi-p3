#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """Clase para manejar SMIL"""
    def __init__ (self):
        """Constructor. Inicializamos las variables"""

        self.tags = {
            'root-layout': {'width':'', 'height':'', 'background-color':''},
            'region': {'id':'', 'top':'', 'bottom':'', 'left':'', 'right':''},
            'img': {'src':'', 'region':'', 'begin':'', 'dur':''},
            'audio': {'src':'', 'begin':'', 'dur':''},
            'textstream': {'src':'', 'region':''}
        }

    def startElement(self, name, attrs):
        """Método que se llama cuando se abre una etiqueta"""

        if name in self.tags:
            attribs = attrs.getNames()
            for attrib in attribs:
                self.tags[name][attrib] = attrs.get(attrib, "")

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
