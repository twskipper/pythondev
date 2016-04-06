#!/usr/bin/env python
#coding:utf-8
class Person:
    def __init__(self,name = '' ,age = 0):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    def set_age(self,age):
        if 0 < age <= 150:
            self._age = age
            
    def display(self):
        print(self,'1')
    
    def __str__(self):
        return "Person('%s',%s)" % (self._name,self._age)
    '不懂'
    def __repr__(self):
        return str(self)
    '不太懂'
    @age.setter
    def age(self,age):
        if 0 < age <= 150:
            self._age = age
    
