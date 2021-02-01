#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import calendar

# decoration
print(stylize("\n---- | Print calendar | ----\n", fg("red")))

# class
class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    # output magic method
    def __repr__(self):
        output = stylize(self.print_calendar(self.year, self.month), fg("red"))
        return output

    # methods
    def print_calendar(self, yr, mo):
        return calendar.month(year, month)

# main execution
if __name__ == "__main__":
    # user interaction
    year = int(input("Year: "))
    month = int(input("Month: "))
    print()

    print(Calendar(year, month))
