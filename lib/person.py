#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, name=None):
        self.name = name
    #Instance method definition
    def talk(self):
        print("Hello World!")
    def walk(self):
        print("The person is walking.")
