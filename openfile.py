#coding: utf-8

from bs4 import BeautifulSoup
import urllib2
import sys

filename="goldPriced.txt"
gold = "https://www.investing.com/commodities/gold-historical-data"
req = urllib2.Request(gold, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )

soup = BeautifulSoup(con, "html.parser")

goldPrice = soup.findAll("td", {"class": "first left bold noWrap"})
date = "Date: "
price = "Price: "

if (len(sys.argv)==4):
    startDate = (sys.argv[1])
    endDate = sys.argv[2]
    metal = sys.argv[3]
else:
    exit

f = open (filename,"r+w")

for element in goldPrice:

    dateElement= element.parent.find("td", {"class": "first left bold noWrap"}).text
    
    months={"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct": "10", "Nov" : "11", "Dec" : "12"}
    
    month = dateElement[0:3]
    day = dateElement[4:6]
    year = dateElement[8:12]

    monthFormatted = months[month]

    dateFormatted = year + "-" + monthFormatted + "-" + day

    if (element.parent.find("td", {"class": "greenFont"})):
        priceElement= (element.parent.find("td", {"class": "greenFont"})).text
    else:
        priceElement= (element.parent.find("td", {"class": "redFont"})).text
    line= (date + dateFormatted + " " + price + priceElement + "\n")
    f.write(line)

average = 0.00
divisor = 0
startLine = 0
endLine = 0

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

print average/divisor

f.close()