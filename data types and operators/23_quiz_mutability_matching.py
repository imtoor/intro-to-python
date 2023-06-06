sentence1 = "I wish to register a complaint."

sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
print("sentence1: " + sentence1)
print("sentence2:", sentence2)

sentence2[6] = "!"
print('sentence2[6] = "!" :', sentence2)
sentence2[0] = "Our Majesty"
print('sentence2[0] = "Our Majesty" :', sentence2)
sentence1[30] = "!"
print('sentence1[30] = "!" :', sentence1)
sentence2[0:2] = ['We', 'want']
print("sentence2[0:2] = ['We', 'want'] :", sentence2)