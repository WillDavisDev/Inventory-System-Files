import qrcode

#Varialble inputs
filename = input("Please enter file name...")
qrtext = input("Please input data...")

#creating qr code
img = qrcode.make(qrtext)
type(img) 

#saving qr code image
path = ('C:\inventory_system_files/'+ filename + '.png')
img.save(path, format="PNG")


print("QR code created successfully!")

input()