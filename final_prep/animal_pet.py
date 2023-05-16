from animal_class import Animal, Dog

dog_A = Dog("Bob", 12, "Doberman")
print(dog_A)
print("I am a " + dog_A.get_type())

dog_A.set_age(13)
print(dog_A)
