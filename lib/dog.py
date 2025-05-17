#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def __init__(self, name=None):
        self.name = name

    #Instance method definition
    def bark(self): # Instance method definition
        print("Woof!")
    def sit(self):
        print(f"The dog is sitting.")
