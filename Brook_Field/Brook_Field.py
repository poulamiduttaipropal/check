from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
#import googlemaps

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
#gmaps_key=googlemaps.Client(key = "")

n=1
num=0
sleep(2)
browser = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
url='https://www.brookfieldpropertiesretail.com/properties.html'
browser.get(url)
for n in range(1,162):
    try:
        expected_rent="__NA__"
        title=browser.find_elements_by_xpath('//*[@id="propResults"]/div[1]/div/div[" + str(n) + "]/div/a/div/span[1]')
        city=browser.find_elements_by_xpath('//*[@id="propResults"]/div[1]/div/div[" + str(n) + "]/div/a/div/span[2]')
        area_unit="Square Feet"
        image=browser.find_elements_by_xpath('//*[@id="propResults"]/div[1]/div/div[" + str(n) + "]/div/a/img')
        i=image[num].get_attribute("src")
        country="USA"
        floor_count="__NA__"
            # title[num].text=title[num].text.replace('\u2019','')
            # title[num].text=title[num].text.replace('\u2018','')
            # title[num].text=title[num].text.replace('\u2013','')
            # title[num].text=title[num].text.replace('\u2012','')

        t=title[num].text
        c=city[num].text
        city_dict=c[:c.find(",")]
        
        building_name=t
        street="__NA__"
        link=browser.find_elements_by_xpath('//*[@id="propResults"]/div[1]/div/div[" + str(n) + "]/div/a')
        l=link[num].get_attribute("href")
        print(l)
        browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
        browser1.get(l)
        area=browser1.find_elements_by_xpath('/html/body/main/section[2]/div/div[2]/div[3]/div/div[2]/div[2]')
            
        description=browser1.find_elements_by_xpath('/html/body/main/section[2]/div/div[2]/div[1]/div[2]/p')
        landmark=browser1.find_elements_by_xpath('/html/body/section/div/div/div/div/div/div[2]/div[1]/div[1]/span[1]')
        pincode=browser1.find_elements_by_xpath('/html/body/section/div/div/div/div/div/div[2]/div[1]/div[1]/span[5]')
            # description[0].text=description[0].text.replace('\u2019','')
            # description[0].text=description[0].text.replace('\u2018','')
            # description[0].text=description[0].text.replace('\u2013','')
            # description[0].text=description[0].text.replace('\u2012','')
        ae=area[0].text
        d=description[0].text
        landmark_dict=landmark[0].text
        pincode_dict=pincode[0].text
        browser1.quit()
        dict={"area":ae,"area_unit":area_unit,"building_name":building_name,"city":city_dict,"country":country,"description":d,"expected_rent":expected_rent,"floor_count":floor_count,"landmark":landmark_dict,"pincode":pincode_dict,"property_image":i,"street":street,"title":t}
        print(dict)
        with open('/home/ubuntu/data/AppearHere_changeone_UK.json', 'a') as file:
            file.write(json.dumps(dict))
        n=n+1
        num=num+1
            
        print(num)
    except:
        print(traceback.format_exc())
num=0