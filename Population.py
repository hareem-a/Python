"""
This program compares the populations of the US and Mexico.
Author: Hareem
"""

US_pop = 328200000
mexico_pop = 127600000
US_rate = 0.53
mexico_rate = 1.06
US_dec = .9947
mexico_inc = 1.0106
years = 0


print("The current population of the US is %d and decreases by %f each year." % (US_pop, US_rate), sep = " ")
print("The current population of Mexico is %d and increases by %f each year." % (mexico_pop, mexico_rate), sep = " ")

while (US_pop >= mexico_pop):
    print ("\nYear: ", years + 1)
    
    US_pop = US_pop * US_dec
    print("The new population of the US is roughly %.f." % US_pop, sep = " ")

    mexico_pop = mexico_pop * mexico_inc
    print("The new population of Mexico is roughly %.f." % mexico_pop, sep = " ")

    years += 1

print("\nIt took %d years for the population of Mexico to exceed the population of the US." % (years))

    
