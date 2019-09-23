"""
Short program that calculates how many cans of paint are needed to paint a room given the
length, width, height, and number of coats of paint.
"""


COVERAGE = 400

length = float(input("Input the length of the room in feet: "))
width = float(input("Input the width of the room in feet: "))
height = float(input("Input the height of the room in feet: "))
coats = int(input("Input the amount of coats you plan to apply: "))

surface_area = (length * width) + (length * height * 2) + (width * height * 2)
coverage_needed = surface_area * coats

cans_of_paint_required = coverage_needed / COVERAGE

print("You will need to buy " + str(round(cans_of_paint_required)) + " cans of paint.")
