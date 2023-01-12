import qrcode
import pandas as pd
from csv import writer
from pathlib import Path


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
def CreatesQRMain(ComputerName, Username, SerialNumber, ModelInfo):
    
    #Gets File Path
    OUTPUT_PATH = Path(__file__).parent
    DATA_PATH = OUTPUT_PATH.with_name("Data")

    #Creates Computer entity
    newComp = [ComputerName, Username, SerialNumber, ModelInfo]

    #Opens and edits CSV file
    #with open(DATA_PATH / "Inventory.csv", "w") as f_object:

    #    writer_object = writer(f_object)

    #    f_object.write(newComp)

    #    f_object.close()

    
    return -1

def IntializeInventoryCSV():
    OUTPUT_PATH = Path(__file__).parent
    DATA_PATH = OUTPUT_PATH.with_name("Data")
    
    df = pd.read_csv(DATA_PATH / "Inventory.csv")

    df.columns = ['ComputerName', 'Username', 'SerialNumber', 'ModelInfo']

    df.to_csv(DATA_PATH / "Inventory2.csv", index=False)


