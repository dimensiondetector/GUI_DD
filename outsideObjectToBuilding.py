'''
This Code accounts for the object outside the building.
Let object class 3 = car                               Actual Height: 6.6ft = 79.2inches
                 4 = PERSON                            Actual Height: 5.5634999 ft 66.75 inches took average of male and female
                 5 = STREET SIGN (STOP OR SPEED LIMIT) Actual Height: 7ft =84 inches
                 6 = FIREHYDRANT                       Actual Height: 30.5"
                 7 = STREETLIGHT                        Actual Height: 25ft =300inches
                 8 = TRAFFICLIGHT
get xmin and ymin or ymin and x max or other 2 points of any object
see if any of those points' x is less than that of building and y of that point less than ymax of building, then that is an object we could use
'''
import re
file_object = "img_5625.txt"

elements = []
dataInLine = []
buildings = []
cars = []
person = []
streetsign = []
firehydrant = []
streetlight = []

with open(file_object) as f:
    for line in f:#reads each line in in the text file
        split_line = line.split()
        dataInLine.append(split_line)

    for obj in dataInLine:

        if obj[0] == "1":
            yBottomBuilding = obj[1]
            yTopBuilding = obj[2]
            yLeftBuilding = obj[3]
            yRightBuilding= obj[4]
            #get Object's coordinates at the border point of bounding box
            #put coordinate values in a list... list name is same as object class name
            buildings.append([int(obj[0]), int(yBottomBuilding), int(yTopBuilding), int(yLeftBuilding), int(yRightBuilding)])

        if obj[0] == "3":
            yBottomCar = obj[1]
            yTopCar = obj[2]
            yLeftCar = obj[3]
            yRightCar= obj[4]

            cars.append([int(obj[0]), int(yBottomCar), int(yTopCar), int(yLeftCar), int(yRightCar)])

        if obj[0] == "4":
            yBottomPerson = obj[1]
            yTopPerson = obj[2]
            yLeftPerson = obj[3]
            yRightPerson= obj[4]

            person.append([int(obj[0]), int(yBottomPerson), int(yTopPerson), int(yLeftPerson), int(yRightPerson)])

        if obj[0] == "5":
            yBottomSign = obj[1]
            yTopSign = obj[2]
            yLeftSign = obj[3]
            yRightSign= obj[4]

            streetsign.append([int(obj[0]), int(yBottomSign), int(yTopSign), int(yLeftSign), int(yRightSign)])

        if obj[0] == "6":
            yBottomHydrant = obj[1]
            yTopHydrant = obj[2]
            yLeftHydrant = obj[3]
            yRightHydrant = obj[4]

            firehydrant.append([int(obj[0]), int(yBottomHydrant), int(yTopHydrant), int(yLeftHydrant), int(yRightHydrant)])

        if obj[0] == "7":
            yBottomLight = obj[1]
            yTopLight = obj[2]
            yLeftLight = obj[3]
            yRightLight = obj[4]

            streetlight.append([int(obj[0]), int(yBottomLight), int(yTopLight), int(yLeftLight), int(yRightLight)])


#line 155 to 168 compiles but does not run because logic is not right
# it always goes to the else statement
topLeftPoint = False
topRightPoint = False

#1. NEED TO DECIDE WHICH BUILDING - since there could be 1 or more buildings in the picture
# For now, we can work on the very first building
areaBuildings = list()
index = 0
if len(buildings) > 0:

    #The biggest building is what we are interested in
    #so we find it
    for newArrayBuild in buildings:

        buildTopLeftCoordinate = newArrayBuild[1]
        buildTopRightCoordinate = buildTopLeftCoordinate + newArrayBuild[3]
        buildBottomLeftCoordinate = buildTopLeftCoordinate + newArrayBuild[4]
        buildBottomRightCoordinate = buildBottomLeftCoordinate + newArrayBuild[3]

        area = newArrayBuild[3] * newArrayBuild[4]

        temp = [area, newArrayBuild]
        areaBuildings.append(temp)
        index = index+1
else:
    print("No building in the picture")

areaBuildings = sorted(areaBuildings, key=lambda x:x[0], reverse=True)

building = areaBuildings[0][1]

#2. NEED TO FILTER ALL CARS BY TESTING IF A CAR OVERLAP LOCATION OF THE BUILDING
# NOTE: one or more car can overal building location, if there are more than one, then we need to decide which one

carsInsideTheBuilding = list()
if len(cars) > 0:

    buildTopLeft = building[1]
    buildTopRight = buildTopLeft + building[3]
    buildBottomLeft = buildTopLeft + building[4]
    buildBottomRight = buildBottomLeft + building[3]

    for car in cars:
        carTopLeft = car[1]
        carTopRight = carTopLeft + car[3]
        carBottomLeft = carTopLeft + car[4]
        carBottomRight = carBottomLeft + car[3]
        carActual = carBottomRight + car[4]

        if (buildBottomLeft <= carTopLeft) or (buildBottomRight >= carTopRight):
            carsInsideTheBuilding.append(car)

        print("cars inside building")
        print(carsInsideTheBuilding)
        print("building")
        print(building)
# Text file: ybottom,ytop,xleft,xright,actual height, building height, building width
        carInBuildStr = ' '.join(str(e) for e in carsInsideTheBuilding)

        #print("convertion cars in build list To String: ")
        #print(carInBuildStr)

        c = '[,]'
        for char in c:
            carInBuildStr = carInBuildStr.replace(char,"")

        word = carInBuildStr.split(' ')
        print(word)

        yCarPixel = float(word[1]) - float(word[2])
        print(yCarPixel)

        buildingInStr = ' '.join(str(e) for e in building)
        print("convertion cars in build list To String: ")
        print(carInBuildStr)

        b = '[,]'
        for char in b:
            building = buildingInStr.replace(char,"")
        wordB = buildingInStr.split(' ')
        print(wordB)
        yBuildingPixel = float(wordB[1]) - float(wordB[2])
        print(yBuildingPixel)
        buildingMeasurementCar = ((yBuildingPixel/yCarPixel) * 79.2) / 12
        print("car to buildingMeasure")
        print(buildingMeasurementCar)
        with open("Output", "w") as text_file:
            text_file.write("Purchase Amount: %s buildingMeasurement %f" % (buildingInStr, buildingMeasurementCar))

else:
    print("No car detected")


#3. Sections below show the calculated height of the building using each object's dimension
'''
yCarPixel = int(carsInsideTheBuilding[0]) - int(cars[1])
yBuildingPixel = int(buildings[0]) - int(buildings[1])
buildingMeasurementCar = ((yBuildingPixel / yCarPixel) * 79.2) / 12
print("car to building")
print(buildingMeasurementCar)

yHydrantPixel = int(firehydrant[0]) - int(firehydrant[1])
yBuildingPixel = int(buildings[0]) - int(buildings[1])
buildingMeasurementHydrant = ((yBuildingPixel / yHydrantPixel) * 30.5) / 12
print("FIREHYDRANT to building: ")
print(buildingMeasurementHydrant)

yPersonPixel = int(person[0]) - int(person[1])
yBuildingPixel = int(buildings[0]) - int(buildings[1])
buildingMeasurementPerson = ((yBuildingPixel / yPersonPixel) * 66.75) / 12
print("PERSON to building: ")
print(buildingMeasurementPerson)

yStreetLightPixel = int(streetlight[0]) - int(streetlight[1])
yBuildingPixel = int(buildings[0]) - int(buildings[1])
buildingMeasurementLight = ((yBuildingPixel / yStreetLightPixel) * 300) / 12
print("FIREHYDRANT to building: ")
print(buildingMeasurementLight)

yStreetSignPixel = int(streetsign[0]) - int(streetsign[1])
yBuildingPixel = int(buildings[0]) - int(buildings[1])
buildingMeasurementSign = ((yBuildingPixel / yStreetSignPixel) * 84) / 12
print("FIREHYDRANT to building: ")
print(buildingMeasurementSign)

print("CHECK this is obj[0]: ")
print(obj[0] )

#I made this Measurement = [] list because when I print to text file without hardcoding this is necessary
Measurement = []
Measurement.append(3)
Measurement.append(buildingMeasurementCar)
Measurement.append(4)
Measurement.append(buildingMeasurementHydrant)
Measurement.append(5)
Measurement.append(buildingMeasurementPerson)
Measurement.append(6)
Measurement.append(buildingMeasurementLight)
Measurement.append(7)
Measurement.append(buildingMeasurementSign)
print("\n this is building measurement")
print(Measurement)

#pseudocode for outputing to textfile
#Step1. Print obj[0] to obj[6]
#step2. if obj[0] == Measurement[0]
            #print Measurement[1] ....this is for car to building measurement
            #if obj[0] == Measurement[2]
                #print Measurement[3]... this  is for hydrantTobuilding Measurement
            #continue step 2 until obj[0]==Measurement[8]
#Step3. print

#testing how output to file works I am not able to print multiple lines to output file without hardcoding
TotalAmount = 0.0
price = 56
with open("Output", "w") as text_file:
    text_file.write("Purchase Amount: %s price %f" % (TotalAmount, price))

'''
    #incase you want to pass multiple arguments
