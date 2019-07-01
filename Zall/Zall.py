from selenium import webdriver
from time import sleep
import json
import traceback
import re
from selenium.webdriver.firefox.options import Options
#import googlemaps


options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
#gmaps_key=googlemaps.Client(key = "")

sleep(2)
browser = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
url='https://www.loopnet.com/for-lease/?sk=a6b4f854ccc540dc1c47dfa7fe92f01a&bb=uk8usny0_Sh2jnsi7_pkB'
browser.get(url)
num=0
    
for x in range(1, 18):
    try:
        expected_rent="__NA__"
        title=browser.find_elements_by_xpath('//*[@id="placardSec"]/div[2]/ul[2]/li[" + str(x) + "]/article/header/div[1]/h6/a')
        # image=browser.find_elements_by_xpath('//*[@id="main"]/article[" + str(x) + "]/a/img')
        city=browser.find_elements_by_xpath('//*[@id="placardSec"]/div[2]/ul[2]/li[" + str(x) + "]/article/header/div[2]/h6/a')
        # i=image[num].get_attribute("src")
        country="USA"
        t=title[num].text
        c=city[num].text
        city_dict=c[:c.find(",")]
        state=c[c.find(","):]
        area_unit="Square Feet"
        info=browser.find_elements_by_xpath('//*[@id="placardSec"]/div[2]/ul[1]/li[" + str(x) + "]/article/header/div[2]/h4/a')
        area=info[num].text
        area_dict=area[:area.find("sf")]
        link=browser.find_elements_by_xpath('//*[@id="placardSec"]/div[2]/ul[1]/li[" + str(x) + "]/article/header/div[1]/h4/a')
        l=link[num].get_attribute("href")
        print(l)
        building_name="__NA__"
        street="__NA__" 
        
        #add in dictionary
        #geocode_result=gmaps_key.geocode(t)
        #lat=geocode_result[0]["geometry"]["location"]["lat"]
        #lon=geocode_result[0]["geometry"]["location"]["lng"]
        floor_count="__NA__"
        browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
        browser1.get(l)
        landmark="__NA__"
        #area=browser1.find_elements_by_class_name('sf-number')
        description=browser1.find_elements_by_xpath('//*[@id="top"]/section/main/section/div[2]/div[2]/div/div/div[1]/section[3]/div[2]/div/p')
        d=description[0].text
        image=browser1.find_elements_by_xpath('//*[@id="mosaic-profile"]/div[1]/div[1]/img')
        i=image[num].get_attribute("src")
        #ae=area[0].text
        pincode=browser1.find_elements_by_xpath('//*[@id="top"]/section/main/section/div[2]/div[2]/div/div/div[1]/section[1]/h2/span[2]')
        p=pincode[0].text
        #print(p)
        p_one= re.search('[0-9][0-9][0-9][0-9][0-9]', p)
        pincode_dict=p_one.group(0)

        #landmark_dict=landmark[0].text
        
        browser1.quit()
        dict={"area":area_dict,"area_unit":area_unit,"building_name":building_name,"city":city_dict,"country":country,"description":d,"expected_rent":expected_rent,"floor_count":floor_count,"landmark":landmark,"pincode":pincode_dict,"property_image":i,"state":state,"street":street,"title":t}
        print(dict)
        # with open('/home/poulami/Documents/AppearHere_UK_data.json', 'a') as file:
        #     file.write(json.dumps(dict))
        num=num+1
            
        print(num)
    except:
        print(traceback.format_exc())





    
        