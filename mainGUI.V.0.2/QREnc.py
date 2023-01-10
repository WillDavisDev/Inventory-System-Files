import qrcode
def encode(qrtext):
    #Varialble inputs
   

    #creating qr code
    img = qrcode.make(qrtext)
    type(img) 

    #saving qr code image
    path = ('C:\inventory_system_files/'+ qrtext + '.png')
    img.save(path, format="PNG")


    print("QR code created successfully!")

input()