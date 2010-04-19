#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import string
from string import *


class ScritParserOutputHTML:
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


class ScriptParser:
        
    __context = None
    __output = "html"
    __Buffer = ""
    __outputHandler = None

    __headerTitle = ""
    __headerIssue = ""
    __headerAuthor = ""
    __headerAddress = ""

    def __init__(self, filename):
        self._scriptFilename = filename
        print self._scriptFilename
#td       check if file exists
        self.Parse()

    def __removeComments(self, line):
        pattern = '^;' 
        if re.search(pattern, line):
            return None
        else:
            return line


    def __parseHeader(self):
        pattern_author = '^author: +'
        pattern_title = '^title: +'
        pattern_issue = '^issue: +'
        pattern_address = '^address: +'
        remove = []

        for part in self.__lines:
            if re.search(pattern_author, part):
                self.__headerAuthor = re.sub(pattern_author, '', part)
                remove.append(part)
            elif re.search(pattern_title, part):
                self.__headerTitle = re.sub(pattern_title, '', part)
                remove.append(part)
            elif re.search(pattern_issue, part):
                self.__headerIssue = re.sub(pattern_issue, '', part)
                remove.append(part)
            elif re.search(pattern_address, part):
                self.__headerAddress = re.sub(pattern_address, '', part)
                remove.append(part)
        for rem in remove:
            self.__lines.remove(rem)
    
    def __parseBody(self):
        pattern_page = '^PAGE:'
        pattern_panel = '^PANEL:'
        pattern_dialog = '^([A-Za-z]{1,}) :: '
        remove = []

        for part in self.__lines:
            if re.search(pattern_page, part):
                self.__Buffer += self.__outputHandler.Page()
                remove.append(part)
            if re.search(pattern_panel, part):
                self.__Buffer += self.__outputHandler.Panel()
                remove.append(part)
        
        for rem in remove:
            self.__lines.remove(rem)
        

    def Parse(self):
        fd = open(self._scriptFilename)
        self._scriptString = fd.read()
        fd.close()

        parts = string.split(self._scriptString, "\n")
        #parts = map(parts, strip)
        parts = map(string.strip, parts)
        parts = map(self.__removeComments, parts)
        parts = filter(None, parts)
#        print parts
       
        self.__lines = parts
        
        self.__outputHandler = ScritParserOutputHTML()
        self.__parseHeader()
        self.__parseBody()
        
        print self.__lines

        self.__buffer  = self.__outputHandler.Header(self.__headerTitle, self.__headerIssue, self.__headerAuthor, self.__headerAddress)
        self.__buffer += self.__Buffer
        self.__buffer += self.__outputHandler.Footer()
        
        print self.__buffer;

if __name__ == '__main__':
    parser = ScriptParser(sys.argv[1])
