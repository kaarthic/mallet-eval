#!/usr/bin/python
# convert hit xml to mallet compatible formats 

import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
  def startElement(self, name, attributes):
    if name == "word":                              # on word tag
      print (attributes["cont"] + " " + attributes['pos'] + " "+ attributes["ne"]).encode('utf-8')
    if name == "sent":                              # on a sentence tag
      print ''

import xml.sax
import os, stat

parser = xml.sax.make_parser( )
handler = BookHandler( )
parser.setContentHandler(handler)
for item in os.listdir("."):
  path = "." + os.sep + item
  if r".xml" in path:
    parser.parse(path)

