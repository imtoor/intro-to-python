# A data type for immutable ordered sequences of elements
AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))
print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude {}".format(AngkorWat[1]))

dimensions = 52, 40, 100
length, width, height = dimensions
length2, width2, height2 = 52, 40, 100
print("The dimensions are {}x{}x{}".format(length, width, height))