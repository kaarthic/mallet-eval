#!/usr/bin/python
# convert hit xml to mallet compatible test input 
# XXX: must encode to utf-8 

import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
  def __init__(self):
    self.inTitle = 0                                # handle XML parser events
    self.mapping = {}                               # a state machine model

  def startElement(self, name, attributes):
    if name == "word":                              # on word tag
      print (attributes["cont"]).encode('utf-8')
    if name == "sent":
      print ''

import xml.sax
import os, stat

parser = xml.sax.make_parser( )
handler = BookHandler( )
parser.setContentHandler(handler)
for item in os.listdir("."):
  path = "." + os.sep + item
  if r"xml" in path:
    parser.parse(path)



