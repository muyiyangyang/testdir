#!/usr/bin/python
# -*- coding: utf-8 -*-
class Employee:
    empCount = 0
    __e = 1
  
    def __init__(self, name, salary):
        self.name = name
        self.salary  = salary
        Employee.empCount = Employee.empCount + 1

    def displayCount(self):
        print "total %d" % Employee.empCount

    def displayEmployee(self):
        print "name: ", self.name,  ", salary: ", self.salary

e1 = Employee("aa", 1122)
print e1.empCount
print e1._Employee__e

class Parent:
    def __init__(self):
        print "调用父类的构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self, attr):
	Parent.parentAttr = attr
        self.pattr = attr
  
    def getAttr(self):
        print "父类属性：", Parent.parentAttr
        print "父类属性1：", self.pattr

class Child(Parent, Employee):
    def __init__(self):
        print "调用子类构造函数"

    #def parentMethod(self):
    #    print "调用子类'父类'方法"

    def childMethod(self):
        print "调用子类方法"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.displayCount()
