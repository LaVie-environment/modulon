#!/usr/bin/env python3

class Circle:
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius

    @classmethod
    def total_area(cls):
        """Static method to total the areas of all Cicles"""
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total