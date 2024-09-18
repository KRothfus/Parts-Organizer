# this is the main file after boot
import json
from partsclass import Part
# size = 64
# part = [0] * size
# for i in range(0,size,1):
#     part[i]= Part("3 mm machine screw", 50, 1,1,1)
#     print(part[i])

prgm = True


with open('Partdata.json') as file:
    parts = json.load(file)
partData = {}
readResult = "0"
while prgm:
    readResult = input("Do you want to: \n1. Search for a part? \n2. Add a part? \n3. Delete a part? \n4. Exit and Save?\n")

    if readResult == "1":
        print("You have chosen to search for a part.")
        print(parts)
    elif  readResult == "2":
        
        readResult = input("You have chosen to add a part.\nEnter the description, qty, quadrant, row, col separated by commas: ")
        
        
        if readResult is not "":
            partInputs = readResult.split(",")
            for partInput in partInputs:
               if partInput.isdigit():
                   partInput == int(partInput)
                
            partInst= Part(partInputs[0],partInputs[1],partInputs[2],partInputs[3],partInputs[4])
            print('You just added '+partInst.qty+' '+partInst.description+'.')
            Part.partCount()
            print(partInst.partDict)
            parts.append(partInst.partDict)
            print(parts)
                     
            
        else:
            continue
            
    elif  readResult == "3":
        print("You have chosen to delete a part.")
        
    elif readResult == "4":
        break

with open("Partdata.json",'w') as f:
    json.dump(parts,f)
    
        

