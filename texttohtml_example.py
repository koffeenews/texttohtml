# -*- coding: utf-8 -*-
import texttohtml

with open("texttohtml_rawtext.txt") as f:
    rawText = f.read()
    html = texttohtml.formatHtml('\n\n'+rawText+'\n\n')

print(html)
