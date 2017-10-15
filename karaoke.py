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
            stringtag += tag + '\t'
            for attr in self.tags[tag]:
                stringtag += attr + '\t'
            stringtag += "\n"
        return stringtag

if __name__ == '__main__':

    k = KaraokeLocal()
    print(k.__str__())
