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
attr_num=2
num=0
browser = webdriver.Firefox(options=options, executable_path='/home/poulami/Downloads/geckodriver')
url='https://therealdeal.com/new-research/properties/'
browser.get(url)
while(n!=430):
    sleep(2)
    try:
        expected_rent = '__NA__'n
        floor_count='__NA__'n
        floor_count
        building_name=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[1]/span[2]/a')

        title = browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[1]/span[2]/a')
        city ='New York'
        area = browser.find_elements_by_xpath('//*[@id="algolia-hits"]/div/div[" + str(attr_num) + "]/article/a/div[2]/p[2]')n
        area_unit='Square Foot'
        address=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[2]/span[2]')
        address_dict=address[num].text
        image = browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[1]/div/a/img')
        image_dict = image[num].get_attribute("src")
        country = "USA"
        area_dict = area[num].text   n
        title_dict=title[num].text
        link = browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[1]/span[2]/a')
        landmark = browser1.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[3]/span[2]')
        landmark_dict=landmark[num].text
        l = link[num].get_attribute("href")
        print(l)
        #dict={"building_name":building_name,"expected_rent":expected_rent,"floor_count":floor_count,"title":title_dict,"city":city,"area":area_dict,"area_unit":area_unit,"image":image_dict,"country":country}
        browser1 = webdriver.Firefox(options=options, executable_path='/home/poulami/Downloads/geckodriver')
        browser1.get(l)
        description = browser1.find_elements_by_xpath('//*[@id="property_content_for_change"]/div[3]')
        
        description_dict = description[0].text
        
        pattern = '[0-9][0-9][0-9][0-9][0-9]'
        pincode = re.findall(pattern, address_dict)
        pincode_dict=pincode[0]
        street=(address_dict[0:address_dict.find(',')])
        browser1.quit()
        browser2 = webdriver.Firefox(options=options, executable_path='/home/poulami/Downloads/geckodriver')
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
        with open('/home/poulami/Project/data/Ripco.json', 'a') as file:
            file.write(json.dumps(dict))
        num = num + 1
        n=n+1
        image_num=image_num+1
        attr_num=attr_num+1
        print(num)
        # print(dict)
    except:
        print(traceback.format_exc())