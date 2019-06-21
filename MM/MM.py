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
url='https://archive.madisonmarquette.com/?state=0&asset_type=0&post_type=properties&searchform=simple&submit=Go'
browser.get(url)
num=0
    
for x in range(1, 47):
    try:
        expected_rent="__NA__"
        title=browser.find_elements_by_xpath('//*[@id="main"]/article[" + str(x) + "]/div/p[1]/a')
        image=browser.find_elements_by_xpath('//*[@id="main"]/article[" + str(x) + "]/a/img')
        city=browser.find_elements_by_xpath('//*[@id="main"]/article[" + str(x) + "]/div/p[2]/a')
        i=image[num].get_attribute("src")
        country="USA"
        t=title[num].text
        c=city[num].text
        area_unit="Square Feet"
        link=browser.find_elements_by_xpath('//*[@id="main"]/article[" + str(x) + "]/div/p[1]/a')
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
        area=browser1.find_elements_by_class_name('sf-number')
        description=browser1.find_elements_by_class_name('col-2')
        d=description[0].text
        ae=area[0].text
        pincode=browser1.find_elements_by_class_name('col-1')
        p=pincode[0].text
        #print(p)
        p_one= re.search('[0-9][0-9][0-9][0-9][0-9]', p)
        pincode_dict=p_one.group(0)

        #landmark_dict=landmark[0].text
        
        browser1.quit()
        dict={"area":ae,"area_unit":area_unit,"building_name":building_name,"city":c,"country":country,"description":d,"expected_rent":expected_rent,"floor_count":floor_count,"landmark":landmark,"pincode":pincode_dict,"property_image":i,"street":street,"title":t}
        print(dict)
        with open('/home/poulami/Documents/AppearHere_UK_data.json', 'a') as file:
            file.write(json.dumps(dict))
        num=num+1
            
        print(num)
    except:
        print(traceback.format_exc())





    
        