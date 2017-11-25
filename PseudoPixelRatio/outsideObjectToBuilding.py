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

    topLeftPoint = False
    topRightPoint = False
#if top left point of a car is within building, that is top of car is higher than building and if left side of car box is further than left of building box
    if yTopCar > yBottomBuilding and yLeftCar > yLeftBuilding:
        topLeftPoint = True
        print("topLeftPoint of car withing building")
    if yTopCar > yBottomBuilding and yRightCar < yRightBuilding:
        topRightPoint = True
        print("topRightPoint ofcar is within building")
    else:
        print("dont use this object")
        #i need to include something here to move on to next line
    yCarPixel = int(cars[0]) - int(cars[1])
    yBuildingPixel = int(buildings[0]) - int(buildings[1])
    buildingMeasurement = ((yBuildingPixel / yCarPixel) * 79.2) / 12
    print("car to building")
    print(buildingMeasurement)

    yHydrantPixel = int(firehydrant[0]) - int(firehydrant[1])
    yBuildingPixel = int(buildings[0]) - int(buildings[1])
    buildingMeasurement = ((yBuildingPixel / yHydrantPixel) * 30.5) / 12
    print("FIREHYDRANT to building: ")
    print(buildingMeasurement)

    yPersonPixel = int(person[0]) - int(person[1])
    yBuildingPixel = int(buildings[0]) - int(buildings[1])
    buildingMeasurement = ((yBuildingPixel / yPersonPixel) * 66.75) / 12
    print("PERSON to building: ")
    print(buildingMeasurement)

    yStreetLightPixel = int(streetlight[0]) - int(streetlight[1])
    yBuildingPixel = int(buildings[0]) - int(buildings[1])
    buildingMeasurement = ((yBuildingPixel / yStreetLightPixel) * 300) / 12
    print("FIREHYDRANT to building: ")
    print(buildingMeasurement)

    yStreetSignPixel = int(streetsign[0]) - int(streetsign[1])
    yBuildingPixel = int(buildings[0]) - int(buildings[1])
    buildingMeasurement = ((yBuildingPixel / yStreetSignPixel) * 84) / 12
    print("FIREHYDRANT to building: ")
    print(buildingMeasurement)
    print("this is obj[0]: ")
    print(obj[0] )


    '''with open("Output.txt", "w") as text_file:
    text_file.write("Purchase Amount: %s" % TotalAmount)
    #incase you want to pass multiple arguments
    price = 33.3
with open("Output.txt", "w") as text_file:
    text_file.write("Purchase Amount: %s price %f" % (TotalAmount, price))'''
