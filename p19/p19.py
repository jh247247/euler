#############################################################################################################
# You are given the following information, but you may prefer to do some research for yourself.             #
#                                                                                                           #
# 1 Jan 1900 was a Monday.                                                                                  #
# Thirty days has September,                                                                                #
# April, June and November.                                                                                 #
# All the rest have thirty-one,                                                                             #
# Saving February alone,                                                                                    #
# Which has twenty-eight, rain or shine.                                                                    #
# And on leap years, twenty-nine.                                                                           #
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400. #
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? #
#############################################################################################################

import math

def date2day(d,m,y):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    y -= m < 3;
    return (y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) + t[m-1] + d) % 7;

ts = 0 # total sundays
for m in range(1,13):
    for y in range(1901,2001):
        ts += date2day(1,m,y) == 0

print(ts)
