'''
This Code accounts for the object outside the building.
Let object class 3 = car                               Actual Height: 6.6ft = 79.2inches
                 4 = PERSON                            Actual Height: 5.5634999 ft 66.75 inches took average of male and female
                 5 = STREET SIGN (STOP OR SPEED LIMIT) Actual Height: 7ft =84 inches
                 6 = FIREHYDRANT                       Actual Height: 30.5"
                 7= STREETLIGHT                        Actual Height: 25ft =300inches
                 8 = TRAFFICLIGHT
get xmin and ymin or ymin and x max or other 2 points of any object
see if any of those points' x is less than that of building and y of that point less than ymax of building, then that is an object we could use
'''
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

        elements = []
#in that line read, pick each number separated by space,
#so object number(3), y max, y min, x min, xmax, actual_height_ofObject, actual_widthOfObject, predictedBuildingHeight
        for data in split_line:

            elements.append(data)

        dataInLine.append(elements)

    for obj in dataInLine:
        print(obj)
        print("===============")
        print(obj[0])
        print("===============\n\n\n")

        if obj[0] == "1":
            yBottomBuilding = obj[1]
            yTopBuilding = obj[2]
            yLeftBuilding = obj[3]
            yRightBuilding= obj[4]
            #get Object's coordinates at the border point of bounding box
            yBottomBuilding = int(yBottomBuilding)
            yTopBuilding = int(yTopBuilding)
            yLeftBuilding = int(yLeftBuilding)
            yRightBuilding = int(yRightBuilding)
            #put coordinate values in a list... list name is same as object class name
            buildings.append(yBottomBuilding)
            buildings.append(yTopBuilding)
            buildings.append(yLeftBuilding)
            buildings.append(yRightBuilding)

        if obj[0] == "3":
            yBottomCar = obj[1]
            yTopCar = obj[2]
            yLeftCar = obj[3]
            yRightCar= obj[4]

            yBottomCar = int(yBottomCar)
            yTopCar = int(yTopCar)
            yLeftCar = int(yLeftCar)
            yRightCar = int(yRightCar)

            cars.append(yBottomCar)
            cars.append(yTopCar)
            cars.append(yLeftCar)
            cars.append(yRightCar)

        if obj[0] == "4":
            yBottomPerson = obj[1]
            yTopPerson = obj[2]
            yLeftPerson = obj[3]
            yRightPerson= obj[4]

            #need for compare statement to change it to int
            yBottomPerson = int(yBottomPerson)
            yTopPerson = int(yTopPerson)
            yLeftPerson = int(yLeftPerson)
            yRightPerson = int(yRightPerson)

            person.append(yBottomPerson)
            person.append(yTopPerson)
            person.append(yLeftPerson)
            person.append(yRightPerson)

        if obj[0] == "5":
            yBottomSign = obj[1]
            yTopSign = obj[2]
            yLeftSign = obj[3]
            yRightSign= obj[4]

            #need for compare statement to change it to int
            yBottomSign = int(yBottomSign)
            yTopSign = int(yTopSign)
            yLeftSign = int(yLeftSign)
            yRightSign = int(yRightSign)

            streetsign.append(yBottomSign)
            streetsign.append(yTopSign)
            streetsign.append(yLeftSign)
            streetsign.append(yRightSign)

        if obj[0] == "6":
            yBottomHydrant = obj[1]
            yTopHydrant = obj[2]
            yLeftHydrant = obj[3]
            yRightHydrant = obj[4]

            #need for compare statement to change it to int
            yBottomHydrant = int(yBottomHydrant)
            yTopHydrant = int(yTopHydrant)
            yLeftHydrant = int(yLeftHydrant)
            yRightHydrant = int(yRightHydrant)

            firehydrant.append(yBottomHydrant)
            firehydrant.append(yTopHydrant)
            firehydrant.append(yLeftHydrant)
            firehydrant.append(yRightHydrant)

        if obj[0] == "7":
            yBottomLight = obj[1]
            yTopLight = obj[2]
            yLeftLight = obj[3]
            yRightLight = obj[4]

            #need for compare statement to change it to int
            yBottomLight = int(yBottomLight)
            yTopLight = int(yTopLight)
            yLeftLight = int(yLeftLight)
            yRightLight = int(yRightLight)

            streetlight.append(yBottomLight)
            streetlight.append(yTopLight)
            streetlight.append(yLeftLight)
            streetlight.append(yRightLight)
    print("\nfirehydrant: \n")
    print(firehydrant)
    print("\nstreetlight :\n")
    print(streetlight)
    print("\nstreetsign :\n")
    print(streetsign)
    print("\nperson :\n")
    print(person)
    print("\ncars :\n")
    print(cars)
    print("\nbuilding: \n")
    print(buildings)


#line 155 to 168 compiles but does not run because logic is not right
# it always goes to the else statement
    topLeftPoint = False
    topRightPoint = False

#if top left point of a car is within building, that means if top of car is higher than building bottom AND if left side of car box is further than left of building box
#when I check with ttext file the math works but not able to fix it
    if yTopCar > yBottomBuilding and yLeftCar > yLeftBuilding:
        topLeftPoint = True
        print("topLeftPoint of car withing building")
    if yTopCar > yBottomBuilding and yRightCar < yRightBuilding:
        topRightPoint = True
        print("topRightPoint ofcar is within building")
    else:
        print("dont use this object")



    #Sections below show the calculated height of the building using each object's dimension

    yCarPixel = int(cars[0]) - int(cars[1])
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


    #incase you want to pass multiple arguments
