#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler

if __name__ == '__main__':

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags()['img']['src'])
