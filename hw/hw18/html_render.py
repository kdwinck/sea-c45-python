#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, tag=""):
        self.tag = tag
        self.content = []

    def append(self, item):
        self.content.append(item)

    def render(self, file_out, ind=""):
        indent = '    ' + ind
        if (self.tag == 'html'):
            file_out.write('<!DOCTYPE html>\n')
        file_out.write((ind + '<{}>\n').format(self.tag))
        for item in self.content:
            if (type(item) != str):
                item.render(file_out, indent)
            else:
                file_out.write(indent + item + '\n')
        file_out.write((ind + '</{}>\n').format(self.tag))


class Html(Element):

    def __init__(self):
        Element.__init__(self, "html")


class Head(Element):

    def __init__(self):
        Element.__init__(self, "head")


class Body(Element):

    def __init__(self):
        Element.__init__(self, "body")


class P(Element):

    def __init__(self, line=""):
        Element.__init__(self, "p")
        self.line = line
        self.append(line)


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        file_out.write(('{ind}<{tag}>{con}</{tag}>\n')
                       .format(ind=ind, tag=self.tag, con=self.content[0]))


class Title(OneLineTag):

    def __init__(self, line=""):
        OneLineTag.__init__(self, "title")
        self.line = ''
        self.append(line)
