# Gravity Simulation

import math
import numpy as np

# Welcome

print("Welcome to a 1D Free Fall Simulation. Please enter only in metric integers. ")
print("You will enter the amount of time you want to simulate, it includes information about impact, \n"
      "even if the simulation stops before impact.")

# Constants

g = 9.81

# Variables

height = int(input("Drop Height: "))
timeElapsed = 1
runTime = int(input("How long do you want to record data from the fall? "))
location = 0
mass = int((input("Mass: ")))
timeToImpact = 0

# Simulation

print("Second by second info of free fall in given time.")
while timeElapsed <= runTime and timeToImpact >= 0 and location >= 0:

    # Equations

    distanceTraveled = (g * timeElapsed ** 2) / 2
    velocity = distanceTraveled / timeElapsed
    location = height - distanceTraveled
    momentum = mass * velocity
    timeToImpact = math.sqrt((2 * height) / g)

    # Print Stats

    print("\nTime to simulation end: " + str(runTime - timeElapsed))
    print('Y Location: ' + str(location) + 'M')
    print('Velocity: ' + str(velocity) + 'M/S')
    print('Distance Traveled: ' + str(distanceTraveled) + 'M')
    print('Momentum: ' + str(momentum) + 'N')
    print('Time Elapsed: ' + str(timeElapsed))
    print('Rough time to impact: ' + str(timeToImpact - timeElapsed))
    print()

    # Add to time elapsed

    timeElapsed = timeElapsed + 1

# Print impact results

print("\n The Simulation is done. \n")
print("*This is printed even if the object fell past the ground, or never hit it.* \n Info on impact: ")
print('Y Location: 0M')
print('Velocity: ' + str(height / runTime) + 'M/S')
print('Distance Traveled: ' + str(height) + 'M')
print('Momentum: ' + str(mass * (height / runTime)) + 'N')
print('Time Spent in free fall: ' + str(timeToImpact))
print()

# To Do:
# Add Terminal Velocity
# Add warning for faster than Newtonian Physics
# Slow time
