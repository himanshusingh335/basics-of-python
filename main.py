import vehicle

swift = vehicle.FourWheeler("red", False)

print("Colour of swift is " + swift.colour)
print("Number of wheels %d", swift.wheels)
print("Car automatic " + str(swift.automatic))

swift.changeColour("blue")

print("Colour of swift is " + swift.colour)
print("Number of wheels %d" % swift.wheels)
print("Car automatic " + str(swift.automatic))
