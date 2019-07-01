from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
import re
#import googlemaps

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
#gmaps_key=googlemaps.Client(key = "")

n=1
while(n!=18):
    
    sleep(2)
    browser = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
    url='https://tel.local.ch/de/q/Mcdonalds.html?page=' + str(n) + '&rid=fPQt&where='
    browser.get(url)
    num=0
    for x in range(1, 11):
        try:
            # image=browser.find_elements_by_class_name('result-list-result-category-placeholder')
            # i=image[num].get_attribute("src")
            country="Switzerland"      
            landmark="__NA__"
            building_name="__NA__"
            link=browser.find_elements_by_class_name('listing-link clearfix')
            l=link[num].get_attribute("href")
            print(l)
            browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
            browser1.get(l)
            title=browser1.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/h1')
            area=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/span')
            address=browser1.find_elements_by_xpath('/html/body/div[3]/div[3]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[2]/span')
            contact=browser1.find_elements_by_xpath('/html/body/div[3]/div[3]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[2]/span/a')
            description="__NA__"
            
            ad=address[0].text
            ct=contact[0].text
            t=title[0].text
            pincode = re.search([0-9][0-9][0-9][0-9],ad)
            pincode_dict=pincode.group(0)
            city=ad[:ad.find(pincode_dict)]
            browser1.quit()
            dict={"address":ad,"building_name":building_name,"city":city,"contact":ct,"country":country,"description":description,"landmark":landmark,"pincode":pincode_dict,"title":t}
            print(dict)
            # with open('/home/ubuntu/data/AppearHere_changeone_UK.json', 'a') as file:
            #     file.write(json.dumps(dict))
            num=num+1
            n=n+1
            print(num)
        except:
            print (traceback.format_exc())
    
    