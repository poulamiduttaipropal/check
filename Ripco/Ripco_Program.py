from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
import re
options = Options()
options.headless = True


profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)

n=1
num=0
image_num=53
while(n!=430):
    sleep(2)
    browser = webdriver.Firefox(options=options, executable_path='/home/poulami/Documents/geckodriver')
    url='https://www.ripcony.com/property-listings/?leaseOrSale=lease'
    browser.get(url)
    try:
        expected_rent = '__NA__'
        floor_count='__NA__'
        building_name='__NA__'

        title = browser.find_elements_by_xpath('//*[@id="algolia-hits"]/div/div[" + str(n) + "]/article/a/div[2]/h6')
        city ='__NA__'
        area = browser.find_elements_by_xpath('//*[@id="algolia-hits"]/div/div[" + str(n) + "]/article/a/div[2]/p[2]')
        area_unit='Square Foot'
        image = browser.find_elements_by_xpath('//*[@id="algolia-hits"]/div/div[" + str(n) + "]/article/a/div[1]/img')
        image_dict = image[num].get_attribute("src")
        country = "USA"
        area_dict = area[num].text
        title_dict=title[num].text
        link = browser.find_elements_by_xpath('//*[@id="algolia-hits"]/div/div[" + str(n) + "]/article/a')
        l = link[num].get_attribute("href")
        print(l)
        #dict={"building_name":building_name,"expected_rent":expected_rent,"floor_count":floor_count,"title":title_dict,"city":city,"area":area_dict,"area_unit":area_unit,"image":image_dict,"country":country}
        browser1 = webdriver.Firefox(options=options, executable_path='/home/poulami/Documents/geckodriver')
        browser1.get(l)
        description = browser1.find_elements_by_xpath('//*[@id="info"]')
        address=browser1.find_elements_by_class_name('address')
        landmark = browser1.find_elements_by_class_name('secondary-copy')
        description_dict = description[0].text
        address_dict=address[0].text
        landmark_dict=landmark[0].text
        pattern = '[0-9][0-9][0-9][0-9][0-9]'
        pincode = re.findall(pattern, address_dict)
        pincode_dict=pincode[0]
        street=(address_dict[0:address_dict.find(',')])
        browser1.quit()
        browser2 = webdriver.Firefox(options=options, executable_path='/home/poulami/Documents/geckodriver')
        browser2.get('https://www.latlong.net')
        text_area = browser2.find_element_by_id('place')
        text_area.send_keys(address_dict)
        browser2.find_element_by_id("btnfind").click()
        sleep(2)
        lat_long=browser2.find_elements_by_xpath('//*[@id="latlngspan"]')
        lat_long_dict=lat_long[0].text
        lat_long_dict=lat_long_dict.replace('(','')
        lat_long_dict=lat_long_dict.replace(')','')
        seperate=lat_long_dict.split(',')
        latitude=seperate[0]
        longitude=seperate[1]
        print(latitude)
        print(longitude)
        print(lat_long_dict)
        browser2.quit()

        dict = {"address":address_dict,"area":area_dict,"area_unit":area_unit,"building_name":building_name,"city":city,"country":country,"description":description_dict,"expected_rent":expected_rent,"floor_count":floor_count,"landmark":landmark_dict,"latitude":latitude,"longitude":longitude,"property_images":[image_dict],"pincode":pincode_dict,"street":street,"title":title_dict}
        print(dict)
        with open('/home/poulami/Documents/Ripco.json', 'a') as file:
            file.write(json.dumps(dict))
        num = num + 1
        n=n+1
        image_num=image_num+1
        print(num)
        # print(dict)
    except:
        print(traceback.format_exc())