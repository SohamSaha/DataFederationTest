#coding: utf-8

from bs4 import BeautifulSoup
import urllib2
import sys

goldFilename="goldPriced.txt"
silverFilename="silverPriced.txt"
gold = "https://www.investing.com/commodities/gold-historical-data"
silver = "https://www.investing.com/commodities/silver-historical-data"
req1 = urllib2.Request(gold, headers={'User-Agent' : "Magic Browser"}) 
con1 = urllib2.urlopen( req1 )
req2 = urllib2.Request(silver, headers={'User-Agent' : "Magic Browser"}) 
con2 = urllib2.urlopen( req2 )

soup1 = BeautifulSoup(con1, "html.parser")
soup2 = BeautifulSoup(con2, "html.parser")

goldPrice = soup1.findAll("td", {"class": "first left bold noWrap"})
silverPrice = soup2.findAll("td", {"class": "first left bold noWrap"})

date = "Date: "
price = "Price: "

fileOpen1 = open (goldFilename,"w")
fileOpen2 = open (silverFilename,"w")

f1 = open (goldFilename,"r+w")
f2 = open (silverFilename,"r+w")

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
    f1.write(line)

for element in silverPrice:

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
    f2.write(line)

f1.close()
f2.close()