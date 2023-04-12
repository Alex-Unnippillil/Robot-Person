# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:55:57 2023

@author: Alex Unnippillil
"""

class Robot:
    def __init__(self,n,c,a):
        self.name = n
        self.color = c
        self.age = a
    
    def introduce_self(self):
        print ("MY name is " + self.name) 
        
r1 =Robot("Alex","green",29)
r2 =Robot("Alice","red",30)

r1.introduce_self()


class Person:
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p 
        self.is_sitting = i
        
    def sit_down(self):
        self.is_sitting = True
        
    def stand_up(self):
        self.is_sitting = False
        
p1 = Person("Eve","aggressive",False)
p2 = Person("Bob","talkative",True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
