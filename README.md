# QR NOW 

<img src="./.pictures/qr-code2.png" width="300" />

QRNOW is a simple python scipt that reads your excel file and generates QR codes from the same. QRNOW uses pandas to perform operations on the excel file. It also uses [qrcodemonkey-api](https://www.qrcode-monkey.com/qr-code-api-with-logo/) to generate the QR codes.

Please note :-
- Replace the **<insert-url>** in the **payload** with your desired image URL.
- QR now uses the excel file in the data folder, generates and saves a QR code every 5 seconds based on the number of data rows in the excel file, ignoring the headers
- The QR code files are named after the data in the row 1. Here, **Names -**, in a .png format. Can be changed as needed
- The QR code now contains member name, club_name, city and sos message
