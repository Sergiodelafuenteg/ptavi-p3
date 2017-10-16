#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import json

class KaraokeLocal(SmallSMILHandler):

    def __init__(self):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('karaoke.smil'))
        self.tags = sHandler.get_tags()

    def __str__(self):

        list_lines = []
        list_attri = []
        for tag in self.tags:
            for attri in tag:
                for cont in tag[attri]:
                    linea = "{}='{}'".format(cont, tag[attri][cont])
                    list_attri.append(linea)
                linea = "{}\t{}".format(attri, '\t'.join(list_attri))
                list_lines.append(linea)
        stringtag = '\n'.join(list_lines)

        return stringtag

        #tag + '\t' + attr + "=" + cont + \n
        #Elemento1\tAtributo11="Valor11"\tAtributo12="Valor12"\t...\n
        #root-layout\twidth="248"\theight="300"\tbackground-color="blue"\n
    def to_json(self):
        with open('karaoke.json', 'w') as outfile:
            json.dump(self.tags, outfile)

if __name__ == '__main__':

    karaoke = KaraokeLocal()
    karaoke.to_json()
