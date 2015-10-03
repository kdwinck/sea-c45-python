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

    def append(self, string):
        self.content.append(string)

    def render(self, file_out, ind=""):
        tab = '    '
        file_out.write(('<{tag}>\n').format(tag=self.tag))
        for string in self.content:
            file_out.write(tab + string + '\n')
        file_out.write(('</{tag}>\n').format(tag=self.tag))
