import requests
from bs4 import BeautifulSoup 
import datetime
import sys
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# WebDriver'ı başlat
driver = webdriver.Chrome() 

pdf_link=[]
driver.get("http://dergi.mo.org.tr/detail.php?id=1")
url = f'http://dergi.mo.org.tr/detail.php?id=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
li_sayilar=[]
sayi=soup.findAll("ul" , {"class" : "volume_groups"})
for i in sayi:
    sayi2=i.findAll("li")
    li_sayilar.append(len(sayi2))

yil=1980
for i in range(1,50) : 
    
    element = driver.find_element(By.XPATH, f"//*[@id='info_altsol']/ul/li[{i}]/a")
    ActionChains(driver).click(element).perform()
    
    dongu=1
    for j in range(li_sayilar[i-1]) : 
        if yil==1942 : 
            yil=yil-1
        element2= driver.find_element(By.XPATH, f"//*[@id='volume_group_{yil}']/li[{dongu}]/a")
        ActionChains(driver).click(element2).perform()
        dongu=dongu+1
        response = requests.get(driver.current_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        link=soup.find("div",{'id' : "info_altsag"}).find_all("li")

        for z in link : 
                bilgi=z.find("a")
                pdf_link.append(bilgi.get("href"))
                
        time.sleep(1)
    yil=yil-1
    time.sleep(1)
    
#//*[@id="volume_group_1979"]/li[1]/a
#//*[@id="volume_group_1980"]/li[1]/a
# #firma_baslik=soup.findAll("a", {"class": "brand-logo"})  //*[@id="info_altsag"]/ul/li[3]/span[2]

# {
#      "url": VERININ_CEKILDIGI_ADRES, *
#      "service": KISALTILMIS_ADRES_KODU (örnek wikipeadia), *
#      "title": BASLIK,
#      "description": ACIKLAMA, *
#      "text": ICERIK, *
#      "file": DOSYA_LINKI,
#      "writers": YAZAR,
#      "release_date": YAZILMA_TARIHI,
#      "created_at": datetime.datetime.now() * 
#  }

def download_file(url, save_path):
    # İndirilecek dosyanın URL'sini belirtin
    file_url = url
    
    # Dosyayı indirin
    r = requests.get(file_url, stream=True)
    
    # İndirme işlemi başarılı ise
    if r.status_code == 200:
        # Dosyayı yerel olarak kaydedin
        with open(save_path, 'wb') as file:
            for chunk in r.iter_content(chunk_size=128):
                file.write(chunk)
        print("Dosya başarıyla indirildi.")
    else:
        print("Dosya indirilemedi.")
sayi4=0
for i in pdf_link : 

    file_url = f"{i}"
    save_path = f"C:\\Users\\bilal\\OneDrive\\Masaüstü\\pdf\\{sayi4}.pdf"
    download_file(file_url, save_path)
    sayi4=sayi4+1




time.sleep(500000)




    
