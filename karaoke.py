#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal(SmallSMILHandler):

    def __init__(self):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('karaoke.smil'))
        self.tags = sHandler.get_tags()

    def __str__(self):

        stringtag = ""
        for tag in self.tags:
            for attr in self.tags[tag]:
                stringtag = "{}".format('\t'.join(self.tags))

        return stringtag

        #tag + '\t' + attr + "=" + cont + \n
        #Elemento1\tAtributo11="Valor11"\tAtributo12="Valor12"\t...\n
        #root-layout\twidth="248"\theight="300"\tbackground-color="blue"\n
if __name__ == '__main__':

    k = KaraokeLocal()
    print(k)
