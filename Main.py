# import the conversion functions from the modules
from miles import convertToKilometers
from kilometers import convertToMiles

# set flags
validValue = True
processing = True

# continue procesing until the user chooses to exit (x)
while processing:

    # accept a distance value from the user
    userDistance = float(input("Please enter a distance value: "))
    # accept a unit of length from the user
    userUnit = input("What is the unit of length (M = miles, KM = kilometers): ")

    # invoke the appropriate function from the modules for the given unit of length value
    if userUnit.upper() == "M":  # if the value the user entered in uppercase is an "M"
        convertDistance = convertToKilometers(
            userDistance)  # call the functioon (within the kilometers module) to convert to kilometers passing in the user entered distance
        conversionUnit = "kilometers"  # set the full name of the conversion unit for display
        userUnit = "miles"  # set the full name of the user entered unit for display
    elif userUnit.upper() == "KM":  # if the value the user entered in uppercase is an "KM"
        convertedDistance = convertToMiles(
            userDistance)  # call the function (within the miles module) to convert to miles passing in the user entered distance
        conversionUnit = "miles"  # set the full name of the conversion unit for display
        userUnit = "kilometers"  # set the full name of the user entered unit for display
    else:
        validValue = False

    if validValue:
        print("Your distance of ", userDistance, " ", userUnit, "is equivalent to", convertedDistance,
              conversionUnit)  # display conversion results
    else:
        print("You entered an invalid unit of length.")  # display error message for invalid value

    userKey = input(
        "Press X to quit or enter to continue processing. ")  # accept a value from user to determine if processing continues

    if userKey.upper() == "X":  # if the value the user entered in uppercase is an "X" set the processing flag to false so the program will quit running
        processing = False