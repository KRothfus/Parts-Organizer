def main(): 

    import ujson
    from partsclass import Part

    prgm = True

    try: 
        with open('Partdata.json') as file:
            parts = ujson.load(file)
    except:
        print('There has been a corruption with the file. Will need to restart the parts file.')
        parts = []
        
    partData = {}
    readResult = "0"
    
    #Functions
    def removePart(parts,i,j,k):
        parts[:] = [part for part in parts if not (part['location'] == [i, j, k])]
                
    def addPartQty(parts:dict, qty:int, quad:int, row:int, col:int):
        for part in parts:
            if part.get('location') == [quad,row,col]:
                initQty = part.get('qty')
                print(type(qty))
                qty = int(qty) + int(initQty)
                part.update({'qty': qty})
                print(f"You have {qty} of {part['description']}")
                
    def removePartQty(parts:dict, qty:int, quad:int, row:int, col:int):
        for part in parts:
            if part.get('location') == [quad,row,col]:
                initQty = part.get('qty')
                qty = int(initQty) - int(qty)
                if qty <= 0:
                    part.update({'qty': 0})
                    print(f"You have 0 qty of {part['description']}")
                else:
                    part.update({'qty': qty})
                    print(f"You have {qty} of {part['description']}")
                
    def saveParts(parts):
        with open("Partdata.json",'w') as f:
            ujson.dump(parts,f)
            
    def searchParts(parts: dict,searchTermList: list):
        for part in parts:
            #part.get('description').replace(':','')
            #part.get('description').replace(';','')
            searchDesc = part.get('description').split(" ")
            
            for eachDesc in searchDesc:
                if len(searchTermList) == 1:       
                    if eachDesc == searchTermList[0]:
                        foundPart = part.get('location')
                        print(f'Part {eachDesc} matches the term {searchTermList} at location {foundPart}.')
                    #else:
                        #print(f'No parts were found using any of the following search terms: {searchTermList}')
                        
                elif len(searchTermlist) >= 2:
                    for searchTerm in searchTermList:                
                        if eachDesc == searchTerm:
                            foundPart = part.get('location')
                            print(f'Part {eachDesc} matches the term {searchTerm} at location {foundPart}.')
                        #else:
                            #print(f'No parts were found using any of the following search terms: {searchTermList}')

    #Main loop     
    while prgm:
        readResult = input("Do you want to: \n1. Search for a part? \n2. Add a part? \n3. Delete a part?\n4. Change a qty? \n5. Exit and Save?\n")

        if readResult == "1":
            print("You have chosen to search for a part.")
            readResult = input("Please input the list of search terms you would like to use separated by commas.")
            readResultList = readResult.split(',')
            searchParts(parts, readResultList)
            
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
                saveParts(parts)       
                
            else:
                continue
                
        elif  readResult == "3":
            print("You have chosen to delete a part.")
            readResult = input("What is the location of the part you want to delete: quadrant, row, col")
            readResult.replace(" ","")
            x,y,z = readResult.split(",")
            removePart(parts,x,y,z)
            saveParts(parts)
            
        elif readResult == "4":
            readResult = input("Do you want to add or remove a part?\n")
            readResult.lower()
            
            if readResult == "add":
                readResult = input("Input the qty you want to add and the location: quadrant, row, col: ")
                readResult.replace(" ","")
                q,x,y,z = readResult.split(",")
                addPartQty(parts,q,x,y,z)
                saveParts(parts)
                
            elif readResult == "remove":
                readResult = input("Input the qty you want to remove and the location: quadrant, row, col: ")
                readResult.replace(" ","")
                q,x,y,z = readResult.split(",")
                removePartQty(parts,q,x,y,z)
                saveParts(parts)
            
        elif readResult == "5":
            prgm = False 
            break
        

    
        
            


