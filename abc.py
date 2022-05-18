import math as M  
Radius = float (input ("Please enter the radius of the given circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle) 
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
