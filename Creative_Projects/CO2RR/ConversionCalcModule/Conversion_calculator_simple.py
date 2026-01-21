# Temporary calculator for proof of concept for Self-driving CO2RR cells
# The following code is built for calculating the conversion of CO2 to CO during CO2RR
# This program will later be converted into a module to run as a part of the SDL process

#Code by Robert Bavisotto

#_________________________________________________________________________________________
# This section imports the values from prior data processing
import sys
    # import CO_GC_area
    # import CO2_GC_area
    # import HCOOH_GC_area
        #Instead of importing each peak individually: This could be done as a loop?


#_________________________________________________________________________________________
# This section reads the values from the integrated GC_CO and GC_CO2 nd GC_HCOOH traces
    # Then it assigns the values to variables


#_________________________________________________________________________________________
# This section initializes to ensure area never equals 0
CO_area = 50
CO2_area = 100
HCOOH_area = -5

#_________________________________________________________________________________________
# This section is for initializing the error count
errorcount = 0

#_________________________________________________________________________________________
# This function will take the CO_GC integrated area and CO2_GC integrated area
#       This is written in CO2 ppm and needs to be coverted to concentration in Moles

def chemical_conversion(Moles_CO2, Moles_CO, Moles_HCOOH):
    global errorcount

    if (Moles_CO + Moles_HCOOH + Moles_CO2 == 0):
        print("A division by zero error has occured")
        print("Moles_CO + Moles_HCOOH + Moles_CO2 = 0")
        errorcount = errorcount + 1
        print("Chemical_conversion program has finished with ", errorcount, " errors")
        sys.exit()

    elif Moles_CO <= 0 and Moles_CO2 <= 0 and Moles_HCOOH <= 0:
        print("The integration program is not working properly")
        print("Moles CO, Moles HCOOH, and Moles CO2 have been read as 0 values")
        print("Cannot divide by zero")
        print("Chemical_conversion program has finished with ", errorcount, " errors")
        errorcount = errorcount + 1
        sys.exit()

    elif Moles_CO <= 0 and Moles_HCOOH <= 0:
        print("Warning CO_area and HCOOH_area are equal to or less than 0")
        print("Your catalyst might be DEAD!!!")
        Moles_CO_temp = 0
        Moles_HCOOH_temp = 0
        conversion_total = (Moles_CO_temp + Moles_HCOOH_temp)/(Moles_CO_temp + Moles_CO2 + Moles_HCOOH_temp)
        conversion_percentage = conversion_total * 100   
        print("The conversion from CO2 is" , conversion_percentage, "%")
        return conversion_total
       
    elif Moles_CO <= 0:
        print("Warning CO_area cannot be equal to or less than 0")
        print("Your catalyst might be DEAD!!!")
        errorcount = errorcount + 1
        Moles_CO_temp = 0
        conversion_total = (Moles_CO_temp + Moles_HCOOH)/(Moles_CO_temp + Moles_CO2 + Moles_HCOOH)
        conversion_percentage = conversion_total * 100    
        print("The conversion from CO2 is" , conversion_percentage, "%")
        return conversion_total
   
    elif Moles_CO2 <= 0:
        print("Warning CO2_area cannot be equal to or less than 0")
        print("100% conversion seems unlikely")
        errorcount = errorcount + 1
        Moles_CO2_temp = 0
        conversion_total = (Moles_CO + Moles_HCOOH)/(Moles_CO + Moles_CO2_temp + Moles_HCOOH)
        conversion_percentage = conversion_total * 100   
        print("The conversion from CO2 is" , conversion_percentage, "%")
        return conversion_total

    elif Moles_HCOOH <= 0:
        Moles_HCOOH_temp = 0
        conversion_total = (Moles_CO + Moles_HCOOH_temp)/(Moles_CO + Moles_CO2 + Moles_HCOOH_temp)
        conversion_percentage = conversion_total * 100  
        print("The conversion from CO2 is" , conversion_percentage, "%")
        return conversion_total
    
    else:
        conversion_total = (Moles_CO + Moles_HCOOH)/(Moles_CO + Moles_CO2 + Moles_HCOOH)
        conversion_percentage = conversion_total * 100    
        print("The conversion from CO2 is" , conversion_percentage, "%")
        return conversion_total

chemical_conversion(CO2_area, CO_area, HCOOH_area)


#_________________________________________________________________________________________
# This section will save the values/ add the values to a specific program to be
# read by the ML modelling
    # Save the file as a specific name using variable_date format
    # Save the file again as a staging file for the ML modelling input program


#_________________________________________________________________________________________
# *** PROGRAM END ***
print("Chemical_conversion program has finished with ", errorcount, " errors")

if errorcount >= 1:

    print("There has been a system error")
