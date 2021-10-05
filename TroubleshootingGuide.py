"""
This troubleshooting program gives you solutions to diesel engine problems.
Author: Hareem Akram
"""

light = input("What color are your status lights? ")

if (light.lower() == "green"):
    print("\nPlease proceed with the restart procedure.")
    print("Thank you.")

elif (light.lower() == "amber"):
    print("\nPlease check fuel line service routine.")
    print("Thank you.")

elif (light.lower() == "red"):
    print("\nShut off all input lines immediately, check meter #3.")
    meter = eval(input("\nWhat number is the meter showing? "))
    
    if (meter < 50):
        print("\nCheck main line for test pressure.")
        pressure = input("\nIs the pressure normal, high, or low? ")

        if (pressure.lower() == "normal"):
            print("\nRefer to motor service manual.")
            print("Thank you.")

        elif (pressure.lower() == "high" or "low"):
            print("\nRefer to main line manual.")
            print("Thank you.")

        else:
            print("\nPlease check that you have entered the correct pressure reading.")
            print("Please try again.")

    elif (meter >= 50):
        print("\nMeasure flow velocity at inlet 2-B.")
        velocity = input("\nIs the flow velocity normal, high, or low? ")

        if (velocity.lower() == "normal"):
            print("\nRefer to inlet service manual.")
            print("Thank you.")

        elif (velocity.lower() == "high" or "low"):
            print("\nRefer unit for factory service.")
            print("Thank you.")

        else:
            print("\nPlease check to confirm you have entered flow velocity correctly.")
            print("Please try again.")

    else:
        print("\nPlease check that you have entered the correct meter reading.")
        print("Please try again.")
        
else:
    print("\nThe color you entered is not included in the system.")
    print("Please try again.")
