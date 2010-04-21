#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import string
from string import *


class ScritParserOutput:
    def __init__(self):
        self.__pageCounter = 0
        self.__pageOpen = False
        self.__panelOpen = False

    def Header(self, title, issue, author, address):
        ret = "\\documentclass{comicsscript}[2010/04/15]\n"
        ret += "\\usepackage[utf8]{inputenc}\n"
        ret += "\\title{%s \#%s}\n" % (title, issue)
        ret += "\\author{%s}\n" % author
        ret += "\\address{%s\n}\n" % address
        ret += "\\begin{document}\n"
        ret += "\\coverpage\n"
        return ret

    def Footer(self):
        ret = ""
        if self.__panelOpen is True:
            ret += "\n\\end{painel}\n"
            self.__panelOpen = False
        if self.__pageOpen is True:
            ret += "\n\\end{pagina}\n"
            self.__pageOpen = False
        ret += "\\end{document}\n"
        return ret

    def Page(self):
        ret = ""
        if self.__panelOpen is True:
            ret += "\n\\end{painel}\n"
            self.__panelOpen = False
        if self.__pageOpen is True:
            ret += "\n\\end{pagina}\n"
            self.__pageOpen = False
        ret += "\\begin{pagina}\n"
        self.__pageOpen = True
        return ret 


    def Panel(self):
        ret = ""
        if self.__panelOpen is True:
            ret += "\n\\end{painel}\n"
            self.__panelOpen = False
        ret += "\\begin{painel}\n"
        self.__panelOpen = True
        return ret

    def Slug(self, location, place, time):
        #return "<h2>%s :: %s :: %s</h2>\n" % (location, place, time)
        
        ret = "\\intslug[%s]{%s}\n" % (time, place)
        return ret

    def Dialog(self, character, dialog):
        ret = "\\begin{dialogue}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{dialogue}\n"
        return ret

    def Whisper(self, character, dialog):
        ret = "\\begin{whisper}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{whisper}\n"
        return ret

    def Burst(self, character, dialog):
        ret = "\\begin{burst}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{burst}\n"
        return ret

    def Text(self, text):
        return "\n%s\n" % text

    def Caption(self, text):
        ret = "\n\\begin{ncaption}\n" 
        ret += text
        ret += "\n\\end{ncaption}\n"
        return ret

    def Sfx(self, text):
        ret = "\n\\begin{sfx}\n" 
        ret += text
        ret += "\n\\end{sfx}\n"
        return ret

    def Thought(self, character, dialog):
        ret = "\\begin{thought}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{thought}\n"
        return ret

    def CCaption(self, character, dialog):
        ret = "\\begin{ccaption}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{ccaption}\n"
        return ret

    def Wavery(self, character, dialog):
        ret = "\\begin{wavery}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{wavery}\n"
        return ret

    def Frosted(self, character, dialog):
        ret = "\\begin{frosted}{%s}\n" % character
        ret += dialog
        ret += "\n\\end{frosted}\n"
        return ret

    def Text(self, text):
        return "\n%s\n" % text
