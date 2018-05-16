#!/usr/bin/python3
""" module 8-rectangle contains subclass Rectangle
which inherits from class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class Rectangle """

    def __init__(self, width, height):
        """ initializes empty Rectangle and
        validates width and height as positive integers"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
