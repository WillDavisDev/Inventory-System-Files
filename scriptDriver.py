from inventorySRC import *
from interfaceFiles import gui

IntializeInventoryCSV()

#CN = input("Enter ComputerName: ")
#UN = input("Enter UserName: ")
#SN = input("Enter Serial Number: ")
#MI = input("Enter Model Info: ")

CN = 'dsd0022-NBK'
UN = 'dsd0022'
SN = '141414'
MI = 'Dell Latitude'

CreatesQRMain(CN,UN,SN,MI)

print("Data Successfully Added!")

CN = 'wld0016-NBK'
UN = 'wld0016'
SN = '6969696'
MI = 'HP Elitebook'

CreatesQRMain(CN,UN,SN,MI)

print("Data Successfully Added!")

CN = 'bgf0007-MAC'
UN = 'bgf0007'
SN = '420Blaze'
MI = 'Macbook Air'

CreatesQRMain(CN,UN,SN,MI)

print("Data Successfully Added!")

gui.makeWindow()

