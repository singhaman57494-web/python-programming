#                                  temperature converter in ststicmethod

class temperature:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        result = (celcius * 9/5) + 32
        return result

print(temperature.celcius_to_fahrenheit(25))