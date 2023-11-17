# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import csv
import pandas
import re
import html5lib
import time
import faker
from faker import Faker
# from faker_vehicle import VehicleProvider
fake = Faker()

# generate fake user data
users = []
for i in range(100):
    username = fake.user_name()
    email = fake.email()
    age = fake.random_int(min=18, max=65)
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=65)
    gender = fake.random_element(elements=('Male', 'Female'))

    users.append([username, email, age, birthdate, gender])

# write user data to csv file
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for user in users:
        writer.writerow(user)

interest = []
for i in range(100):

    car_model = fake.vehicle_model()
    text_of_interest = fake.text(max_nb_chars=200)

    interest.append([car_model, text_of_interest])

# write user data to csv file
with open('interests.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for user in interest:
        writer.writerow(user)
# s = Service("/Users/muhammadabdelmohsen/Downloads/chromedriver_mac64/chromedriver")
# chromeOptions = Options()
# chromeOptions.headless=False
# driver = webdriver.Chrome(service=s, options=chromeOptions)
#
# driver.get("https://www.olx.com.eg/en/ad/رينو-داستر-٢%D9%A0٢%D9%A0-الفئة-الثانية-بالتقسيط-بمقدم-١١%D9%A0-%D9%A0%D9%A0%D9%A0-ID195116250.html")
# print("tmam")
# time.sleep(2)
# LoginButton = driver.find_element(By.CLASS_NAME, value="_1b04dcc1")
# LoginButton.click()
# time.sleep(2)
# cookies = driver.get_cookies()
# print(cookies)

finalLinks = []

for counter in range(2,67):

    links = []

    if (counter == 1):
        Url = "https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?filter=new_used_eq_2%2Cyear_between_2000_to_2023"
    else:
        Url = f'https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?page={counter}&filter=new_used_eq_2%2Cyear_between_2000_to_2023'

    page = requests.get(Url)

    soup = BeautifulSoup(page.content, 'html5lib')
    sections = soup.find_all('li', class_="c46f3bfe")

    for ad in sections:
        for a in ad.find_all('a'):
            links.append("https://www.olx.com.eg" + a['href'])

     #remove duplicates from array links
    #file = open("FLinks.txt", 'a', encoding="utf-8")
    for link in links:
        if link not in finalLinks:
            finalLinks.append(link)
            #file.write(link+"\n")
    #file.close()


# # now we have all the links in finalLinks array and we can loop over it to get the details
#
# # finalLinks = ["https://www.olx.com.eg/en/ad/gla200-amg-ID196066452.html"]
#
print("finished getting links")
print("finalLinks length: ", len(finalLinks))
#
# #
# # #
# # # # finalLinks = finalLinks[0:20]
# # #
# #
# # file = open("FLinks.txt", "r")
# # finalLinks = file.readlines()
# # file.close()
for car in finalLinks:
    #souping
    try:
        page = requests.get(car)
        soup = BeautifulSoup(page.content, 'html.parser')
        details = soup.find_all('div', class_="b44ca0b3")
        Description = soup.find('div', class_="_0f86855a")
        ExtraFeatures = soup.find_all('span', class_="_66b85548")
        # title = soup.find('h1', class_="a38b8112")
        location = soup.find('span', class_="_8918c0a8")
        date = soup.find_all('span', class_="_8918c0a8")
        creationdate = date[1]
        title = soup.find('h1', class_="a38b8112").text
        x = soup.find('div', class_="_1075545d c6bdd888 _5f872d11")
        AdID = x.find('div', class_="_171225da").text
        JoinDate = soup.find('div', class_="_05330198")
        SellerName = soup.find_all('span', class_="_261203a9 _2e82a662")
#
#
#
#
        brand = ""
        model = ""
        year = ""
        price = ""
        kilometers = ""
        PaymentOptions = ""
        color = ""
        EngineCapacity = ""
        Body = ""
        Transmission = ""
        TextDescription = ""
        sellerFinalID = ""
        AdType = ""
        FuelType = ""
        Condition = ""
        Video = ""
        VirtualTour = ""
        Description = ""

        sellerID = soup.find_all("div", class_="_1075545d d059c029")
        for data in sellerID:
            for link in data.find_all('a'):
                sellerFinalID = link['href']
            UniqueLink = [sellerFinalID]
    #
        for detail in details:
            if detail.find_all('span')[0].text == "Brand":
                brand = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Model":
                model = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Ad Type":
                AdType = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Fuel Type":
                FuelType = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Price":
                price = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Payment Options":
                PaymentOptions = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Year":
                year = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Kilometers":
                kilometers = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Transmission Type":
                Transmission = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Condition":
                Condition = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Color":
                color = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Body Type":
                Body = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Engine Capacity (CC)":
                EngineCapacity = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Video":
                Video = detail.find_all('span')[1].text
            if detail.find_all('span')[0].text == "Virtual Tour":
                VirtualTour = detail.find_all('span')[1].text


    #
    #Features
        file1 = open('featureslast.csv', 'a', encoding='utf-8-sig')
        if len(ExtraFeatures) != 0:
            for feature in ExtraFeatures:
                feature = feature.get_text(' ', strip=True)
                #allCarsFeatures.append(feature)
                file1.write(AdID + "," + feature + "\n")
            file1.close()

    #
    #
    #Describtion
        function = [{"ad_id": AdID, "description": Description.get_text(' ', strip=True)}]
        table = pandas.DataFrame(function)
        table.to_csv("desclast.csv", sep=',', encoding='UTF-8-sig', mode='a', index=False, header=False)

    # Car Table
        with open('carlast.csv', 'a', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            CarDetails = [brand, model, AdType, FuelType, price, PaymentOptions, year, kilometers, Transmission, Condition, color, Body, EngineCapacity, Video, VirtualTour]
            file.write(AdID+",")
            writer.writerow(CarDetails + UniqueLink)
        file.close()
     # Ad Table
        file = open('adlast.csv', 'a', encoding='utf-8-sig')
        file.write(AdID+",")
        title = title.replace("\n", " ")
        title = title.replace(",", "/")
        file.write(title + ",")
        file.write(location.get_text(' ', strip=True) + ",")
        file.write(creationdate.get_text(' ', strip=True) + ",")
        file.write("https://www.olx.com.eg" + sellerFinalID + ",")
        file.write("\n")
    # seller table
        file = open('sellerlast.csv', 'a', encoding='utf-8-sig')
        file.write("https://www.olx.com.eg" + sellerFinalID + ",")
        file.write(SellerName[1].get_text(' ', strip=True) + ",")
        file.write(JoinDate.get_text(' ', strip=True) + ",\n")
        file.close()
        print(AdID)
    except:
        continue
# # # #
#
print("finished parsing the links")

#
#
# with open('Cdetails.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         ["Brand", "Model", "AdType", "FuelType", "price", "PaymentOptions", "year",
#          "kilometers", "Transmission", "Condition", "color", "Body", "EngineCapacity", "Video", "VirtualTour"])
#
# import stealth
