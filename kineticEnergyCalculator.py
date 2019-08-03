# Sample Python/Pygame Programs
# Calculate Kinetic Energy
 
print("I will Calculates the Kinetic Energy of a Moving Object for you.")
m_string = input("What is the Object's mass in Kilograms?: ")
m = float(m_string)
v_string = input("What is the Object's speed in Meters per Second?: ")
v = float(v_string)
 
e = 0.5 * m * v * v
print("The Object has " + str(e) + " Joules of Energy")
