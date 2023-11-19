class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

    def inches(self):
        if self.unit == 'inches':
            return self.length
        elif self.unit == 'feet':
            return self.length * 12
        elif self.unit == 'yards':
            return self.length * 36
        elif self.unit == 'miles':
            return self.length * 63360
        elif self.unit == 'kilometers':
            return self.length * 39370.1
        elif self.unit == 'meters':
            return self.length * 39.3701
        elif self.unit == 'centimeters':
            return self.length * 0.393701
        elif self.unit == 'millimeters':
            return self.length * 0.0393701
        else:
            return None

    def feet(self):
        return self.inches() / 12

    def yards(self):
        return self.inches() / 36

    def miles(self):
        return self.inches() / 63360

    def kilometers(self):
        return self.inches() / 39370.1

    def meters(self):
        return self.inches() / 39.3701

    def centimeters(self):
        return self.inches() / 0.393701

    def millimeters(self):
        return self.inches() / 0.0393701


c = Converter(9, 'meters')
print(c.feet())  # Output: 0.75
print(c.meters())  # Output: 0.2286
print(c.miles())  # Output: 0.00014106728324210882
print(c.inches(), "inches")  # Output: 60

'''c2 = Converter(5, 'feet')
print(c2.inches(),"inches")  # Output: 60
print(c2.meters())  # Output: 1.524
print(c2.yards())  # Output: 1.6666666666666667
'''
