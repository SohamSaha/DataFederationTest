#coding: utf-8

from bs4 import BeautifulSoup
import urllib2
import sys
import math

average = 0.00
divisor = 0
startLine = 0
endLine = 0
numerator = 0.00
variance = 0.00
tempAverage = 0.00

if (len(sys.argv)==4):
    startDate = (sys.argv[1])
    endDate = sys.argv[2]
    metal = sys.argv[3]
else:
    exit

if metal == "gold":
    with open("goldPriced.txt") as fp:
        for i, line in enumerate(fp):
            if line[6:16] == startDate:
                startPrice=line[24:32]
                startLine = i
            elif line[6:16] == endDate:
                endPrice=line[24:32]
                endLine = i
            divisor = -(endLine-startLine)

    with open("goldPriced.txt") as fp:
        for i, line in enumerate(fp):
            price = 0.00
            toConvert = line[24:32]
            price=float(toConvert.replace(",",""))
            average+=price

    tempAverage = float("{0:.2f}".format(average/divisor))

    with open("goldPriced.txt") as fp:
        for i, line in enumerate(fp):
            price2 = 0.00
            toConvert = line[24:32]
            price2=float(toConvert.replace(",",""))
            numerator+=(price2-tempAverage)**2
            denominator = divisor
            variance = math.sqrt (numerator/denominator)

elif metal == "silver":
    with open("silverPriced.txt") as fp:
        for i, line in enumerate(fp):
            if line[6:16] == startDate:
                startPrice=line[24:32]
                startLine = i
            elif line[6:16] == endDate:
                endPrice=line[24:32]
                endLine = i
            divisor = -(endLine-startLine)

    with open("silverPriced.txt") as fp:
        for i, line in enumerate(fp):
            price = 0.00
            toConvert = line[24:32]
            price=float(toConvert.replace(",",""))
            average+=price

    tempAverage = float("{0:.2f}".format(average/divisor))

    with open("silverPriced.txt") as fp:
        for i, line in enumerate(fp):
            price2 = 0.00
            toConvert = line[24:32]
            price2=float(toConvert.replace(",",""))
            numerator+=(price2-tempAverage)**2
            denominator = divisor
            variance = math.sqrt (numerator/denominator)

print "Average: " + "{0:.2f}".format(average/divisor)
print "Variance: " + "{0:.2f}".format(variance)