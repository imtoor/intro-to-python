name = 'Jim'
student = name
name = 'Tim'
print(name)
print(student)

scores = ["B", "C", "A", "D", "B", "A", ]
grades = scores
print("scores: " + str(scores))
print("grades: " + str(grades))
scores[3] = "B"
print("scores: " + str(scores))
print("grades: " + str(grades))

print("len: ", len(scores))
batch_sizes = [15, 6, 89, 34, 65, 35]
print("max: ", max(batch_sizes))
python_varietes = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print("max: ", max(python_varietes))
# print("max: ", max([42, 'African Swallow']))
sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes, reverse=True))