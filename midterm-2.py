# Author: CRS 12/14/21
initial_velocity = int(input("Input the initial velocity in meters per second."))
final_velocity = int(input("Input the final velocity in meters per second."))
time = int(input("Enter the time in seconds."))
acceleration = (final_velocity - initial_velocity) / time
print("The acceleration was {0} meters per second.".format(acceleration))
