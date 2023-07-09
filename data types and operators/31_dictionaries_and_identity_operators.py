elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
# print("helium: " + str(elements["helium"]))
elements["helium"] = 3
# print("helium: " + str(elements["helium"]))
# print("carbon" in elements)
print(elements.get("dilithium", "There\'s no such element"))
n = elements.get("dilithium")
print(n)
print(n is None)
print(n is not None)