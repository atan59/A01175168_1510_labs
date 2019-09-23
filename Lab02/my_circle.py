"""Short program that calculates circumference and area of a circle given a radius."""


PI = 3.14159
radius = 0

radius = float(input("Input a value for the radius of the circle: "))
double_radius = radius * 2

circumference = 2 * PI * radius
area = PI * radius * radius

circumference_double_r = 2 * PI * double_radius
area_double_r = PI * double_radius * double_radius

circumference_increase = circumference_double_r / circumference
area_increase = area_double_r / area

print("The circumference of a circle with a radius of " + str(radius) + " is: " + str(circumference))
print("The area of a circle with a radius of " + str(radius) + " is: " + str(area))

print("If the radius is doubled to equal " +
      str(double_radius)+
      ", then the new circumference is " +
      str(circumference_increase) +
      " times bigger than the original circumference.")
print("If the radius is doubled to equal " +
      str(double_radius) +
      ", then the new area is " +
      str(area_increase) +
      " times bigger than the original area.")
