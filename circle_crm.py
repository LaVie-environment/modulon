#!/usr/bin/env python3

class Circle:
    all_circles = []
    pi = 3.14159

    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)

    def circumference(self):
        """determine the circumference of the Circle"""
        return 2 * self.__class__.pi * self.radius

    @classmethod
    def total_circumference(cls):
        """Class method to total the circumference of all Cicles"""
        total = 0
        for c in cls.all_circles:
            total += c.circumference()
        return total