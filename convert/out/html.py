#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import string
from string import *


class ScritParserOutput:
    def __init__(self):
        self.__pageCounter = 0

    def Header(self, title, issue, author, address):
        ret = "<title>\n<head>\n<title>%s :: %s</title>\n</head>\n<body>\n" % (title, issue)
        ret += "<div id=\"cover\">\n"
        ret += "<h1 class=\"title\">%s # %s</h1>\n" % (title, issue)
        ret += "<h2 class=\"author\">by %s</h2>\n" % author
        ret += "<div class=\"address\">%s</div>\n" % address
        ret += "</div>\n"
        return ret
    def Footer(self):
        ret = "\n</body>\n</html>\n"
        return ret

    def Page(self):
        self.__panelCounter = 0
        self.__pageCounter += 1
        return "<h2>PAGE %s</h2>\n" % self.__pageCounter

    def Panel(self):
        self.__panelCounter += 1
        return "<h2>PANEL %s</h2>\n" % self.__panelCounter

    def Slug(self, location, place, time):
        return "<h2>%s :: %s :: %s</h2>\n" % (location, place, time)

    def Dialog(self, character, dialog):
        return "<p>%s :: %s </p>\n" % (character, dialog)

    def Thought(self, character, dialog):
        return "<p>%s (THOUGHT):: %s </p>\n" % (character, dialog)

    def Wavery(self, character, dialog):
        return "<p>%s (WAVERY):: %s </p>\n" % (character, dialog)

    def Frosted(self, character, dialog):
        return "<p>%s (FROSTED):: %s </p>\n" % (character, dialog)

    def Whisper(self, character, dialog):
        return "<p>%s (WHISPER):: %s </p>\n" % (character, dialog)

    def Burst(self, character, dialog):
        return "<p>%s (BURST):: %s </p>\n" % (character, dialog)

    def CCaption(self, character, dialog):
        return "<p>%s (CAPTION):: %s </p>\n" % (character, dialog)

    def Text(self, text):
        return "<p>%s</p>\n" % text
    
    def Caption(self, text):
        return "<p>CAPTION: %s</p>\n" % text

    def Sfx(self, text):
        return "<p>SFX: %s</p>\n" % text


