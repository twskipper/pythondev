#!/usr/bin/env python
#coding:utf-8
class FooClass(object):
        """my very first class:FoodClass"""
        version = 0.1       #class(data) Attribute
        def __init__(self):
            nm='skipper'
            """Constructor"""
            self.name = nm  #class instance (data) attribute
            print 'Create a class instance for',nm

        def showname(self):
            """display instance attribute and class name"""
            print 'Your name is',self.name
            print 'My name is ',self.__class__.__name__
        def showver(self):
            """display class static attribute"""
            print self.version
        def addMe2Me(self,x):
            """apply + operation to argument"""
          
            print x + x
            


foo1 = FooClass()
foo1.showname()
foo1.showver()
foo1.addMe2Me(10)

