#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import string
import os
from string import *

sys.path.append('out')

class ScriptParser:
        
    __context = None
    __output = "html"
    __Buffer = ""
    __outputHandler = None

    __headerTitle = ""
    __headerIssue = ""
    __headerAuthor = ""
    __headerAddress = ""


    def __init__(self, filename, output = 'html'):
        self._scriptFilename = filename
#td       check if file exists
        self._outputModules = {}
        self.Parse(output)

    def __fileNameToModuleName(self, f):
        return os.path.splitext(f)[0] 


    def __loadOutputFilters(self):
        path = 'out'
        files = os.listdir(path)
        test = re.compile("\.py$", re.IGNORECASE)  
        files = filter(test.search, files) 
        moduleNames = map(self.__fileNameToModuleName, files) 
        modules = map(__import__, moduleNames)  

        for module in moduleNames:
            self._outputModules[module] = __import__(module)


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
        pattern_slug = '^(INT|EXT)\.(.*) - (DAY|NIGHT)'
        pattern_dialog = '^([A-Za-z]{1,}) :: (.*)$'
        pattern_caption = '^CAPTION: (.*)$'
        pattern_sfx = '^SFX: (.*)$'
        pattern_thought = '^([A-Za-z]{1,}) :T: (.*)$'
        pattern_ccaption = '^([A-Za-z]{1,}) :C: (.*)$'
        pattern_burst = '^([A-Za-z]{1,}) :B: (.*)$'
        pattern_whisper = '^([A-Za-z]{1,}) :W: (.*)$'
        pattern_wavery = '^([A-Za-z]{1,}) :V: (.*)$'
        pattern_frosted = '^([A-Za-z]{1,}) :F: (.*)$'
        remove = []

        for part in self.__lines:
            if re.search(pattern_page, part):
                self.__Buffer += self.__outputHandler.Page()
                remove.append(part)
            elif re.search(pattern_panel, part):
                self.__Buffer += self.__outputHandler.Panel()
                remove.append(part)
            elif re.search(pattern_slug, part):
                res = re.search(pattern_slug, part)
                slug = res.groups()
                self.__Buffer += self.__outputHandler.Slug(slug[0].strip(), slug[1].strip(), slug[2].strip())
                remove.append(part)
            elif re.search(pattern_dialog, part):
                res = re.search(pattern_dialog, part)
                dialog = res.groups()
                self.__Buffer += self.__outputHandler.Dialog(dialog[0].strip(), dialog[1].strip())
                remove.append(part)
            elif re.search(pattern_caption, part):
                res = re.search(pattern_caption, part)
                caption = res.groups()
                self.__Buffer += self.__outputHandler.Caption(caption[0].strip())
                remove.append(part)
            elif re.search(pattern_sfx, part):
                res = re.search(pattern_sfx, part)
                sfx = res.groups()
                self.__Buffer += self.__outputHandler.Sfx(sfx[0].strip())
                remove.append(part)
            elif re.search(pattern_thought, part):
                res = re.search(pattern_thought, part)
                thought = res.groups()
                self.__Buffer += self.__outputHandler.Thought(thought[0].strip(), thought[1].strip())
                remove.append(part)
            elif re.search(pattern_ccaption, part):
                res = re.search(pattern_ccaption, part)
                ccaption = res.groups()
                self.__Buffer += self.__outputHandler.CCaption(ccaption[0].strip(), ccaption[1].strip())
                remove.append(part)
            elif re.search(pattern_burst, part):
                res = re.search(pattern_burst, part)
                burst = res.groups()
                self.__Buffer += self.__outputHandler.Burst(burst[0].strip(), burst[1].strip())
                remove.append(part)
            elif re.search(pattern_whisper, part):
                res = re.search(pattern_whisper, part)
                whisper = res.groups()
                self.__Buffer += self.__outputHandler.Whisper(whisper[0].strip(), whisper[1].strip())
                remove.append(part)
            elif re.search(pattern_wavery, part):
                res = re.search(pattern_wavery, part)
                wavery = res.groups()
                self.__Buffer += self.__outputHandler.Wavery(wavery[0].strip(), wavery[1].strip())
                remove.append(part)
            elif re.search(pattern_frosted, part):
                res = re.search(pattern_frosted, part)
                frosted = res.groups()
                self.__Buffer += self.__outputHandler.Frosted(frosted[0].strip(), frosted[1].strip())
                remove.append(part)
            else:
                self.__Buffer += self.__outputHandler.Text(part)
                remove.append(part)
        
        for rem in remove:
            self.__lines.remove(rem)
        

    def Parse(self, output):

        fd = open(self._scriptFilename)
        self._scriptString = fd.read()
        fd.close()

        self.__loadOutputFilters()

        parts = string.split(self._scriptString, "\n")
        #parts = map(parts, strip)
        parts = map(string.strip, parts)
        parts = map(self.__removeComments, parts)
        parts = filter(None, parts)

        self.__lines = parts
       
        self.__outputHandler = self._outputModules[output].ScritParserOutput()
        self.__parseHeader()
        self.__parseBody()
        
        self.__buffer  = self.__outputHandler.Header(self.__headerTitle, self.__headerIssue, self.__headerAuthor, self.__headerAddress)
        self.__buffer += self.__Buffer
        self.__buffer += self.__outputHandler.Footer()
        
        print self.__buffer;

if __name__ == '__main__':
    if len(sys.argv) is 3:
        parser = ScriptParser(sys.argv[1], sys.argv[2])
    else:
        parser = ScriptParser(sys.argv[1])
