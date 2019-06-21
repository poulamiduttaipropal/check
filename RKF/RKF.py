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

sleep(2)
browser = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
url='https://www.rkf.com/lease-property-list/?from=view_all'
browser.get(url)
num=0
    
for x in range(1, 324):
    try:
        expected_rent="__NA__"
        title=browser.find_elements_by_xpath('//*[@id="results"]/table[" + str(x) + "]/tbody/tr[1]/td[1]/a')
        area=browser.find_elements_by_xpath('//*[@id="results"]/table[" + str(x) + "]/tbody/tr[2]/td[3]/span[2]')
        image=browser.find_elements_by_xpath('//*[@id="results"]/table[" + str(x) + "]/tbody/tr[2]/td[1]/a/img')
        i=image[num].get_attribute("src")
        country="USA"
        t=title[num].text
        city=t[t.find("|"):]
        city.replace("|", "")
            #add in dict
        street=t[:t.find("|")]
        
        ae=area[num].text
            
            
        area_unit="Square Feet"
        link=browser.find_elements_by_xpath('//*[@id="results"]/table[" + str(x) + "]/tbody/tr[1]/td[1]/a')
        l=link[num].get_attribute("href")
        print(l)
        building_name="__NA__"
            
        pincode="__NA__"
        #add in dictionary
        #geocode_result=gmaps_key.geocode(t)
        #lat=geocode_result[0]["geometry"]["location"]["lat"]
        #lon=geocode_result[0]["geometry"]["location"]["lng"]
        floor_count="__NA__"
        browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Documents/geckodriver')
        browser1.get(l)
        landmark=browser1.find_elements_by_xpath('//*[@id="address"]/div')
        description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]')
        landmark_dict=landmark[0].text
        d=description[0].text
        browser1.quit()
        dict={"area":ae,"area_unit":area_unit,"building_name":building_name,"city":city,"country":country,"description":d,"expected_rent":expected_rent,"floor_count":floor_count,"landmark":landmark_dict,"pincode":pincode,"property_image":i,"street":street,"title":t}
        print(dict)
        with open('/home/poulami/Documents/AppearHere_UK_data.json', 'a') as file:
            file.write(json.dumps(dict))
        num=num+1
            
        print(num)
    except:
        print(traceback.format_exc())





    
        