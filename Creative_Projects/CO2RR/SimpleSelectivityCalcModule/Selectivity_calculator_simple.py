# Temporary calculator for proof of concept for Self-driving CO2RR cells
# Forschungszentrum Juelich - Department of Theoretical Electrochemistry & Data Science
# Part of the PHEONIX Project at IET-1
# GOAL:
# The following code is built for calculating the selectivity for CO during CO2RR
# This program will later be converted into a module to run as a part of the SDL process

#Code by Robert Bavisotto


#_________________________________________________________________________________________
# This section imports the values from prior data processing
import sys
    # import CO_GC_area
    # import CO2_GC_area
    # import HCOOH_GC_area
        #Instead of importing each peak individually: This could be done as a loop?
            #Labelled with corresponding peaks from retention times?


#_________________________________________________________________________________________
# This section reads the values from the integrated GC_CO and GC_CO2 traces
    # Then it assigns the values to variables


#_________________________________________________________________________________________
# This section initializes to ensure area never equals 0
CO_area = 95
HCOOH_area = 95

#_________________________________________________________________________________________
# This section is for initializing the error count
errorcount = 0

#_________________________________________________________________________________________
# This function will take the CO_GC integrated area and CO2_GC integrated area
#       This is written in CO2 ppm and needs to be coverted to concentration in Moles

def chemical_conversion(Moles_CO, Moles_HCOOH):
    global errorcount

    if Moles_CO <= 0 and Moles_HCOOH <= 0:
        print("The integration program is not working properly")
        print("Both Moles CO and Moles HCOOH have been read as 0 values")
        print("Cannot divide by zero")
        errorcount = errorcount + 1
        selectivity_HCOOH = 0
        selectivity_CO = 0
        print("The reaction is" , selectivity_CO, "% selective to CO")
        print("The reaction is" , selectivity_HCOOH, "% selective to HCOOH")
        return selectivity_HCOOH
        return selectivity_CO

    elif Moles_CO <= 0:
        print("Warning CO_area cannot be equal to or less than 0")
        errorcount = errorcount + 1
        selectivity_CO = 0
        Moles_temp_CO = 0
        selectivity_HCOOH = (Moles_HCOOH)/(Moles_temp_CO + Moles_HCOOH)
        selectivity_HCOOH_percentage = selectivity_HCOOH * 100
        #Check to see if the code is working using this print statement    
        print("The reaction is" , selectivity_HCOOH_percentage, "% selective to HCOOH")
        return selectivity_HCOOH
        return selectivity_CO
    
    elif Moles_HCOOH <= 0:
        print("HCOOH_area is equal to or less than 0")
        Moles_temp_HCOOH = 0
        selectivity_CO = (Moles_CO)/(Moles_CO + Moles_temp_HCOOH)
        selectivity_CO_percentage = selectivity_CO * 100
        selectivity_HCOOH = 0
        #Check to see if the code is working using this print statement    
        print("The reaction is" , selectivity_CO_percentage, "% selective to CO")
        return selectivity_CO
        return selectivity_HCOOH
    
    else:
        selectivity_CO = (Moles_CO)/(Moles_CO + Moles_HCOOH)
        selectivity_CO_percentage = selectivity_CO * 100
        #Check to see if the code is working using this print statement    
        print("The reaction is" , selectivity_CO_percentage, "% selective to CO")
        selectivity_HCOOH = (Moles_HCOOH)/(Moles_CO + Moles_HCOOH)
        selectivity_HCOOH_percentage = selectivity_HCOOH * 100
        #Check to see if the code is working using this print statement    
        print("The reaction is" , selectivity_HCOOH_percentage, "%  selective to HCOOH")
        return selectivity_CO, selectivity_HCOOH

chemical_conversion(CO_area, HCOOH_area)


#_________________________________________________________________________________________
# This section will save the values/ add the values to a specific program to be
# read by the ML modelling
    # Save the file as a specific name using variable_date format
    # Save the file again as a staging file for the ML modelling input program


#_________________________________________________________________________________________
# *** PROGRAM END ***
print("Chemical_conversion program has finished with ", errorcount, " errors")