import qrcode
import pandas as pd
from csv import writer

#Creates a QRCode based off of the serial number of a computer 
#Then saves the file somewhere on the computer
def encode(qrtext):
    #Varialble inputs
   

    #creating qr code
    img = qrcode.make(qrtext)
    type(img) 

    #saving qr code image
    path = ('C:\inventory_system_files/'+ qrtext + '.png')
    img.save(path, format="PNG")


    print("QR code created successfully!")

#This is the main function that will be called on
#It basically takes in all of the necessary info and drives the rest of the functions
def ProcessQRInfo(ComputerName, Username, SerialNumber, ModelInfo):
    
    newComp = [ComputerName, Username, SerialNumber, ModelInfo]

    with open('Data\Inventory.csv') as f_object:

        writer_object = writer(f_object)

        writer_object.writerow(newComp)

        f_object.close()

    
    return -1


