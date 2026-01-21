# GOAL:
# The following code is built for calling the other calculator modules and running them in the correct order
# Code by Robert Bavisotto

#___________________________________SECTION_1_____________________________________________
from Selectivity_calculator_module import chemical_selectivity
from Conversion_calculator_module import chemical_conversion

#___________________________________SECTION_2_____________________________________________
# GC Trace Processing modules still need to be written
# Will get data from GC trace processing module
# 1) Needs to read file
# 2) Baseline GC trace
# 3) Integrate area for values to save below
# Placeholder for temporary testing using selected numbers
CO_area = 95.0
HCOOH_area = 5.0
CO2_area = 100.0

#___________________________________SECTION_3_____________________________________________
# GC Area processing modules still need to be written
# Will take GC integrated areas for each measured molecule
# Convert from integrated area to observed moles product
# Will depend on GC molecular sensitivites and GC calibration
# Temporary conversion from integrated area to Moles measured of each
Moles_CO2 = CO2_area
Moles_CO = CO_area
Moles_HCOOH = HCOOH_area

#___________________________________SECTION_4_____________________________________________
result_conversion = chemical_conversion(Moles_CO2, Moles_CO, Moles_HCOOH)
result_selectivity  = chemical_selectivity(Moles_CO, Moles_HCOOH)

#___________________________________SECTION_5_____________________________________________
# Will write another module for Faradaic efficincy

#___________________________________SECTION_6_____________________________________________

# PROGRAM END
