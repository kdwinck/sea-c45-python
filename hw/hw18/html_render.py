#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, tag="html", content=None):
        self.tag = tag
        self.content = content

    def append(self, string):
        self.content.append(string)

    def render(self, file_out, ind=""):

        file_out.write("<{tag}>" + '\n').format(tag=self.tag)
        file_out.write("</{tag}" + '\n').format(tag=self.tag)
