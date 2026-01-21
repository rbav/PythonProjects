# Calculator module for Self-driving CO2RR cells
# Forschungszentrum Juelich - Department of Theoretical Electrochemistry & Data Science
# GOAL:
# The following code is built for calculating the conversion of CO2 to CO during CO2RR
# Code by Robert Bavisotto

#_________________________________________________________________________________________
# This section imports the values from prior data processing
import sys

#_________________________________________________________________________________________
# This section is for initializing the error count
errorcount = 0

#_________________________________________________________________________________________
# This function will take the moles of CO2, CO, and HCOOH and calculate a conversion
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
        errorcount = errorcount + 1
        print("Chemical_conversion program has finished with ", errorcount, " errors")
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

if errorcount >= 1:
    print("There has been a system error")
#_________________________________________________________________________________________
# *** PROGRAM END ***