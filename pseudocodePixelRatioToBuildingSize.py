'''
Note: This pseudocode only amounts for the door on a building, not window
Let object door = '2' in JSON
Let object building ='1' in JSON
Get the object class (from reading text file that YOLO outputs)

if object class =='2'
     y0Door= get left bottom coordinates of door class
     y1Door = get left top coordinates of door class
     yDoorPixel = distance formula on y0Door and y1Door
if object class == '1'
     y3Building = get left bottom coordinate of building class
     y4Building = get left top coordinate of building class
     yBuildingPixel = distance formula on y3 and y4

yframePixel = frame.get(height of Frame)//it will be pixel count of image you are looking at

Step1: Find Door to Frame Ratio in pixel counts(yDoorPixel/yBuildingPixel)
Note: Assume average door height is 6ft
Step2: Find actual Frame height in feet by doing a pixel to ft comparison{(6ft door size/yFrameSize in Ft )= (yDoorPixel/yframePixel) }
Step3: Find Building to Frame in pixel counts(similar to step1)
Step4: Find actual building Height using actual frame size in feet --> ?ftBuildingHeight = {(yBuildingPixel * ActualFrameHeight) /yFramePixel } }
def function name: of each pseudocode
Todo: put in pseudocode in the code where it makes sense
'''


file_object = "blah.txt"
elements = []
dataInLine = []
doors = []
buildings = []

with open(file_object) as f:
    for line in f:
        split_line = line.split()

        elements = []

        for data in split_line:
            elements.append(data)

        dataInLine.append(elements)

    for obj in dataInLine:
        print(obj)
        print("===============")
        print(obj[0])
        print("===============\n\n\n")

        if obj[0] == "2":
            yBottomDoor = obj[1]
            yTopDoor = obj[2]
            yLeftDoor = obj[3]
            yRightDoor = obj[4]

            yBottomDoor = int(yBottomDoor)
            yTopDoor = int(yTopDoor)
            yLeftDoor = int(yLeftDoor)
            yRightDoor = int(yRightDoor)

            doors.append(yBottomDoor)
            doors.append(yTopDoor)
            doors.append(yLeftDoor)
            doors.append(yRightDoor)

        if obj[0] == "1":
            yBottomBuilding = obj[1]
            yTopBuilding = obj[2]
            yLeftBuilding = obj[3]
            yRightBuilding= obj[4]

            yBottomBuilding = int(yBottomBuilding)
            yTopBuilding = int(yTopBuilding)
            yLeftBuilding = int(yLeftBuilding)
            yRightBuilding = int(yRightBuilding)

            buildings.append(yBottomBuilding)
            buildings.append(yTopBuilding)
            buildings.append(yLeftBuilding)
            buildings.append(yRightBuilding)


    print(doors)
    leftToRight = False
    #here comparing left of door is more than left of building and right of door is less than right of building
    if yLeftDoor > yLeftBuilding and yRightDoor < yRightBuilding:
        print("left to right works")
        leftToRight = True
        x = str(int(yBottomBuilding)-100)
        if yTopDoor < yTopBuilding and yBottomDoor < x:
        # this is not printing as of now....we need to check
            print("top to bottom works")

    yDoorPixel = int(doors[0]) - int(doors[1])

    print(buildings)

    yBuildingPixel = int(buildings[0]) - int(buildings[1]) #topy-bottom y of building

    buildingMeasurement = ((yBuildingPixel / yDoorPixel) * 80) / 12

    print(buildingMeasurement)

#check if left x of door is more than left of buildingx, AND if rightx of door is less than x of building
#check if top y of door is less than building AND bottomy of the door building-100
'''
        arr.append(line)
        #line = arr[0]
        # 'door'a: 9,
        #'window': 10,
        #'building': 11
        split_line= line.split(' ')
        #Finding door's height in pixels
        #alist = list()
        yDoorPixel_new = 0.0
        #Assume split_line[5] & split_line[6] last two elems of each line of blah.txt is the pixel count of the original image of that name
        #split line 5 is height of full image
        yFramePixel = float(split_line[5])

        for x in split_line:
            if split_line[0] == "9":
            #Assume  split_line[1] ==door left bottom coordinates
            #Assume split_line[2] ==door left top coordinates
            #get distance formular of those two coordinates
                yBottomDoor = split_line[1]
            #print("Y bottom " + yBottomDoor)
                yTopDoor = split_line[2]
            #print("y Top " + yTopDoor)
                yDoorPixel = float(yTopDoor) - float(yBottomDoor)
                yDoorPixel_new=yDoorPixel
                #alist.append(yDoorPixel)
                #print(*alist, sep='\n')
                print( str(yDoorPixel) + " door pixel" )

            #Finding BUILDING's height in pixels
            if split_line[0] == "11":
            #Assume  split_line[1] ==door left bottom coordinates
            #Assume split_line[2] ==door left top coordinates
            #get distance formular of those two coordinates
                yBottomBuilding = split_line[1]
            #print("Y bottom " + yBottomDoor)
                yTopBuilding = split_line[2]
            #print("y Top " + yTopDoor)
                yBuildingPixel = float(yTopBuilding) - float(yBottomBuilding)
                print( str(yBuildingPixel) + " buildng pixel")

            frameSize = 80*yFramePixel/yDoorPixel_new


            #EX: Building is 100 pixels tall; door is 10 pixels tall
            # 100/10 = 10 -> the building is 10 doors tall
            # 10 * 80inches = 800inches
            #800 inches /12 inches/ft = 66.6666667 ft tall

            print( str(frameSize) + "is frameSize"
            #buildingSize = yBuildingPixel*frameSize/yFramePixel
            #print(str(buildingSize) + " is size")
        #Lets assume average door size is 80 inches


        #    buildingSize = yBuildingPixel*frameSize/yFramePixel
'''
