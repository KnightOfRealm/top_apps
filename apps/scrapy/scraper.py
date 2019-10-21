# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup 
import csv 
from apps.models import Applications

class Scrapy():

    URL = "https://play.google.com/store/apps/collection/topselling_free"


    def getData(self):
        r = requests.get(self.URL) 
        data = BeautifulSoup(r.content, 'html5lib') 
        self.parseAndSaveData(data)

    def parseAndSaveData(self,data):
        apps=[]  # a list to store quotes 
        rows = data.findAll('div',{'class':'ImZGtf mpg5gc'})
        for row in rows: 
            obj, created = Applications.objects.get_or_create(
                name = row.find('div',{'class':'WsMG1c nnK0zc'}).text,
                package = row.find('a',{"class":"poRVub"})['href'].split("=")[1],
                company = row.find('div',{"class":"KoLSrc"}).text,
                rating = row.find('div',{"class":"pf5lIe"})\
                                .find('div',{"role":"img"})['aria-label'],
                )
            if obj:
                apps.append(obj)
            elif created:
                apps.append(created)
        print(apps)