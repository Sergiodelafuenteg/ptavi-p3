#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import json
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fich):

        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fich))
        self.tags = sHandler.get_tags()

    def __str__(self):

        list_lines = []
        list_attri = []
        for tag in self.tags:
            for attri in tag:
                for cont in tag[attri]:
                    if tag[attri][cont] != '':
                        linea = ""
                        linea = "{}='{}'".format(cont, tag[attri][cont])
                        list_attri.append(linea)
                linea = "{}\t{}".format(attri, '\t'.join(list_attri))
                del list_attri[:]
                list_lines.append(linea)
        stringtag = '\n'.join(list_lines)
        return stringtag

    def to_json(self, name_smil, name_json=''):
        if name_json[-5:] != '.json':
            name_json = name_smil.split('.')[0] + '.json'
        with open(name_json, 'w') as outfile:
            json.dump(self.tags, outfile, indent=3)

    def do_local(self):

        for tag in self.tags:
            for attri in tag:
                for cont in tag[attri]:
                    if cont == 'src' and tag[attri][cont][:7] == "http://":
                        urlretrieve(tag[attri][cont], tag[attri][cont].split('/')[-1])
                        tag[attri][cont] = tag[attri][cont].split('/')[-1]

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    fich = sys.argv[1]
    karaoke = KaraokeLocal(fich)
    print(karaoke)
    karaoke.to_json(fich)
    karaoke.do_local()
    karaoke.to_json(fich, 'local.json')
    print(karaoke)
