#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, name="", **kwargs):
        self.name = name
        self.content = []
        self.kwargs = kwargs

    def append(self, item):
        self.content.append(item)

    def render(self, file_out, ind=""):
        indent = '    ' + ind

        if (self.name == 'html'):
            file_out.write('<!DOCTYPE html>\n')

        file_out.write("{}<{}".format(ind, self.name))
        if(self.kwargs):
            for kwargs, value in self.kwargs.items():
                file_out.write(' {}="{}"'.format(kwargs, value))
        file_out.write(">\n")

        for child in self.content:
            if (type(child) != str):
                child.render(file_out, indent)
            else:
                file_out.write(indent + child + '\n')

        file_out.write((ind + '</{}>\n').format(self.name))


class Html(Element):

    def __init__(self):
        super(Html, self).__init__(name="html")


class Head(Element):

    def __init__(self):
        super(Head, self).__init__(name="head")


class Body(Element):

    def __init__(self):
        super(Body, self).__init__(name="body")


class P(Element):

    def __init__(self, line="", **kwargs):
        super(P, self).__init__(name="p", **kwargs)
        self.line = line
        self.append(line)


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        file_out.write(('{ind}<{name}>{con}</{name}>\n')
                       .format(ind=ind, name=self.name, con=self.content[0]))


class Title(OneLineTag):

    def __init__(self, line=""):
        OneLineTag.__init__(self, "title")
        self.line = ''
        self.append(line)


class SelfClosingTag(Element):

    def render(self, file_out, ind=""):
        file_out.write(('{ind}<{name} />\n')
                       .format(ind=ind, name=self.name, kwargs=self.kwargs))


class Hr(SelfClosingTag):

    def __init__(self):
        super(Hr, self).__init__(name="hr")


class Br(SelfClosingTag):

    def __init__(self):
        super(Hr, self).__init__(name="br")
