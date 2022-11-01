# this is a program that will be able to handle unit conversion according to the user choice.

def speed_Conversion(speed, speed_Unit) :

    if speed_Unit == 'KMP':      # verifies that the speed unit is in KMP 
        convertedSpeed = 0.6214 * speed  # changes the speed to MPH
    
    
    elif speed_Unit == 'MPH':    # verifies that the speed unit is in MPH
        convertedSpeed = speed * 1.60934;  # changes the speed to KMP
     
        
    return convertedSpeed 


def temperature_Conversion(temperature, temperatureUnit) :

    if temperatureUnit == 'C':  # verifies that the temperature unit is in celcius 
        convertedTemperature = ((9 * temperature) / 5 + 32)     # changes the temperature to fahrenhite
    
    elif temperatureUnit == 'F':     # verifies that the temperature unit is in fahrenhite 
        convertedTemperature = ((temperature - 32) * 5 / 9)     # changes the temperature to fahrenhite
      
        
    return convertedTemperature 


def main() :
    conversionType = int(input("What you'd like to convert : For speed enter 1, and for temperature enter 2 : ")) # Ask user to select from the given choice

    if conversionType == 1 :    
        inputSpeed = float(input("\nEnter the speed you want to convert : "))   # Ask user to enter the speed 
        speedUnit = input("Enter the current unit for the speed : ") #Ask user to enter the initial unit of the speed
         
        print("Converted speed is : {:.3f}".format(speed_Conversion(inputSpeed, speedUnit)))    # prints the converted speed
        
    elif conversionType == 2 :
        inputTemperature = float(input("\n Please enter the temperature you want to convert : ")) # Ask user to enter the temperature
        tempUnit = input("Please enter the initial unit of the temperature: ") # ask user to enter the initial unit of the temperature
        
        print("Conversion of the temperature is : {:.2f}".format(temperature_Conversion(inputTemperature, tempUnit))) # print the converted temperature
        
    else :

        print("Invalid input !")  # prints invalid input if user choose the unvalid option
        
main()

