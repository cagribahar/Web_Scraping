import requests
from bs4 import BeautifulSoup 
import datetime
import sys
import json
post_detaylink=[]
firma_detaylink=[]
firmapostall=[]
detaylar_listesi = []
for i in range(13123):
    url = f'https://www.sikayetvar.com/tum-markalar?page={i+1}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}



    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.text, 'html.parser')

    
    #post_saat=soup.findAll("div", {"class":"time"})
    #post_isim=soup.findAll("span", {"class":"username"})
    firma_baslik=[]
    firma_baslik=soup.findAll("a", {"class": "brand-logo"})
    #post_firma=[i.get("href").split("/")[1] for i in post_baslik]
    for g in range(len(firma_baslik)):
        firma_detaylink.append(firma_baslik[g].get("href"))
        with open("firmalink.txt", "a") as txt_file:
            txt_file.write(str(firma_baslik[g].get("href")) + "\n")
    print(i,". sayfa alındı")
      

   
       


# print(firma_detaylink)

for i in firma_detaylink : #vodafone
    for j in range(350):
       

        url=f'https://www.sikayetvar.com{i}?page={j+1}' #vodafone?page=1
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for c in soup.findAll("a", {"class": "complaint-layer"}):
            post_detaylink.append(c.get("href"))
        print(i," isimli firma alındı",j,". sayfa alındı"+i)

        if j > 1:
            url2=f'https://www.sikayetvar.com{i}?page={j}' #vodafone?page=1
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}
            response = requests.get(url2, headers=headers)
            soup2 = BeautifulSoup(response.text, 'html.parser')
            if soup == soup2:
                break
            
# print(post_detaylink)
   





post_detaylink2 = []
[post_detaylink2.append(item) for item in post_detaylink if item not in post_detaylink2]

for i in range(len(post_detaylink2)+1):
    url = f'https://sikayetvar.com/{post_detaylink2[i]}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}
    


    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.text, 'html.parser')
    post_baslik2=soup.find("h1",{"class":"complaint-detail-title"})
    post_aciklama=soup.find("div",{"class":"complaint-detail-description"})
    post_firma2=soup.find("a",{"class":"company-link ga-v ga-c"})
    post_tarih=soup.find("time",{"class":"time js-tooltip tooltipstered"})
    post_username=soup.find("span",{"class":"username"}).get("data-href")
    post_cozulmeDurum=soup.find("span",{"class":"solved-badge-txt"})
    post_dosya_link=soup.find("div",{"class":"complaint-attachments box-style"})

    if post_tarih is None:
        post_tarih=soup.find("div",{"class" : "js-tooltip time"})
        print(post_tarih.get("title"))    
    else : 
        print(post_tarih.get("title"))
    print("\n")
    print(post_username)
    print("\n")
    print(post_baslik2.text)
    print("\n")
    if post_firma2 is None:
        print("Açıklama yok")
    else:
        print(post_aciklama.text)
    print("\n")
    if post_firma2 is None:
        print("Firma ismi yok")
    else:
        print(post_firma2.text)
    print("\n")
    if post_cozulmeDurum is None:
        print("Çözümlenmedi")
    else:
        print(post_cozulmeDurum.text)
    print("*******************")
    print("*******************")
    print("*******************")
    
    # detaylar=dict()
    # detaylar[i]= {
    #     "url" : f'https://sikayetvar.com/{post_detaylink2[i]}' ,
    #     "service": 'sikayetvar',
    #     "description": post_baslik2.text, 
    #     "text": post_aciklama.text,
    #     "file": post_dosya_link.img.get("src") if post_dosya_link and post_dosya_link.img else None,
    #     "writers": post_username,
    #     "release_date": post_tarih.get("title") ,
    #     "created_at": datetime.datetime.now() , 
    # } 
    # print(detaylar[i])
    # print("***********************************************************")

    # with open("dosya.json", "a") as json_file:
    #     json.dump(detaylar, json_file, indent=2)
