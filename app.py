import requests as req
import pandas as pd
import time

dataframe = pd.read_excel('data/data.xlsx', 'Sheet1', skiprows=0)
count=0

for i in range(len(dataframe)): 
    a = dataframe.loc[i].to_string()
    print(a)
    url = "https://api.qrcode-monkey.com/qr/custom"
    # Add the logo URL below before running python. Replace <insert-url> with the url
    payload = {"data":a,"config":{"body":"circle-zebra","eye":"frame14","eyeBall":"ball16","erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#000000","eye2Color":"#000000","eye3Color":"#000000","eyeBall1Color":"#000000","eyeBall2Color":"#000000","eyeBall3Color":"#000000","gradientColor1":"#000000","gradientColor2":"#000000","gradientType":"linear","gradientOnEyes":"true","logo":"<insert-url>","logoMode":"clean"},"size":1000,"download":"imageUrl","file":"png"}
    resp = req.post(url , json=payload)
    if resp.status_code == 200 :
        print("\n[+] Status : Success\n")
        output = resp.json()
        link = output.get('imageUrl')
        link = "http:" + link
        response = req.get(link)
        svnm = "{}.png".format(dataframe['Name -'].values[count])
        file = open(svnm, "wb")
        file.write(response.content)
        file.close()
        print("\nImage ",svnm," Saved in (current directory)")
    else:
        print("[-] Status : Error ",resp.status_code)
    count=count+1
    time.sleep(5)