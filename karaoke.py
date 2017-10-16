#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import json
from urllib.request import urlretrieve

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
            json.dump(self.tags, outfile, indent = 3)

    def do_local(self):

        for tag in self.tags:
            for attri in tag:
                for cont in tag[attri]:
                    if cont == 'src' and tag[attri][cont][:7] == "http://":
                        urlretrieve(tag[attri][cont],tag[attri][cont].split('/')[-1])
                        tag[attri][cont] = tag[attri][cont].split('/')[-1])

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    karaoke = KaraokeLocal()
    karaoke.do_local()
