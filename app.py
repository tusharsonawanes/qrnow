import requests as req
import pandas as pd
import time
import os

from PIL import Image, ImageOps, ImageFont, ImageDraw 

dataframe = pd.read_excel('data/data_qr.xlsx', 'Sheet1', skiprows=0)
count=0
border = (200, 200, 200, 200)
raw_qr_codes_dir="raw_qr_codes/"
named_qr_codes_dir="named_qr_codes/"
sos="SCAN  IN  EMERGENCY"
club="SONS OF ANARCHY"
origin="STOCKTON, CALIFORNIA"
url = "https://api.qrcode-monkey.com/qr/custom"
police_image=Image.open(r"data/police.png")

for i in range(len(dataframe)): 
    raw_dataframe = dataframe.loc[i].to_string().replace("  ", "")
    print(raw_dataframe)
    payload = {"data":raw_dataframe,"config":{"body":"square","eye":"frame14","eyeBall":"ball16","erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#000000","eye2Color":"#000000","eye3Color":"#000000","eyeBall1Color":"#000000","eyeBall2Color":"#000000","eyeBall3Color":"#000000","gradientColor1":"#000000","gradientColor2":"#000000","gradientType":"linear","gradientOnEyes":"true","logo":"https://e7.pngegg.com/pngimages/739/857/png-clipart-sons-of-anarchy-california-logo-jax-teller-happy-television-show-motorcycle-club-anarchy-miscellaneous-television.png","logoMode":"clean"},"size":1000,"download":"imageUrl","file":"png"}
    resp = req.post(url , json=payload)
    if resp.status_code == 200 :
        print("\n[+] Status : Success\n")
        output = resp.json()
        link = output.get('imageUrl')
        link = "http:" + link
        response = req.get(link)
        svnm = "{}.png".format(dataframe["Rider Name - "].values[count])
        raw_qr=os.path.join(raw_qr_codes_dir, svnm)
        file = open(raw_qr, "wb")
        file.write(response.content)
        file.close()
        # Code for name on image
        named_qr_temp=os.path.join(raw_qr_codes_dir, svnm)
        named_qr=os.path.join(named_qr_codes_dir, svnm)
        img = Image.open(named_qr_temp)
        resized_image_temp = img.resize((1200,1200))
        resized_image = ImageOps.expand(resized_image_temp, border=border, fill=(252,188,5))
        filename = "{}".format(dataframe["Rider Name - "].values[count])
        resized_image.save("{}".format(named_qr))
        my_image=Image.open("{}".format(named_qr))
        my_image=my_image.rotate(90)
        title_font = ImageFont.truetype('font/barbaro_punta.ttf', 120)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((350,50), origin, align='center', fill="black", embedded_color=True, font=title_font)
        my_image=my_image.rotate(180)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((500, 50), club, align='center', fill="black", embedded_color=True, font=title_font)
        my_image=my_image.rotate(90)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((400, 75), sos, align='center', fill="black", embedded_color=True, font=title_font)
        image_editable.text((200, 1450), filename, align='center', fill="black", embedded_color=True, font=title_font)
        my_image.paste(police_image,(200, 20), mask=police_image)
        my_image.paste(police_image,(1250, 20), mask=police_image)
        my_image.save("{}".format(named_qr))
        # Code ends
        print("\nImage ",svnm," Saved in (current directory)")
    else:
        print("[-] Status : Error ",resp.status_code)
    count=count+1
    time.sleep(5)