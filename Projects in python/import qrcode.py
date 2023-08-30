import qrcode

try:
    img = qrcode.make('https://incomparable-daffodil-83d0ea.netlify.app/')
    img.save('myQRcode.png')
    img.show()
except Exception as e:
    print("An error occurred:", e)
