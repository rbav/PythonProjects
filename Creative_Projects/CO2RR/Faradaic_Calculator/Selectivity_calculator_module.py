# GOAL:
# The following module is built for calculating the selectivity for CO during CO2RR
# Code by Robert Bavisotto

#_________________________________________________________________________________________
# This section imports the values from prior data processing
import sys

#_________________________________________________________________________________________
# This section is for initializing the error count
errorcount = 0

#_________________________________________________________________________________________
#This section calculates the chemical selectivity if only CO and HCOOH are formed
def chemical_selectivity(Moles_CO, Moles_HCOOH):
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

if errorcount >= 1:
    print("There has been a system error")
#_________________________________________________________________________________________

# *** PROGRAM END ***
