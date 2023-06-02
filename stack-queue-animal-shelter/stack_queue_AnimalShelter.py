class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


class AnimalShelter:
    def __init__(self):
       
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0

    def enqueue(self, animal):
       
        animal.timestamp = self.timestamp
        self.timestamp += 1

        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
       
        if self.dog_queue:
            return self.dog_queue.pop(0)
        elif self.cat_queue:
            return self.cat_queue.pop(0)
        else:
            return None

    def _dequeue_cat(self):
     
        if self.cat_queue:
            return self.cat_queue.pop(0)
        elif self.dog_queue:
            return self.dog_queue.pop(0)
        else:
            return None


# Example usage:
shelter = AnimalShelter()

# Enqueue
shelter.enqueue(Animal("dog", "Max"))
shelter.enqueue(Animal("cat", "Whiskers"))
shelter.enqueue(Animal("dog", "Buddy"))
shelter.enqueue(Animal("cat", "Mittens"))

# Dequeue
dog = shelter.dequeue("dog")
if dog:
    print(f"Adopted dog: {dog.name}")

cat = shelter.dequeue("cat")
if cat:
    print(f"Adopted cat: {cat.name}")

# Dequeue an animal without specifying preference
animal = shelter.dequeue("unknown")
if animal:
    print(f"Adopted animal: {animal.species} - {animal.name}")
else:
    print("No preference specified. Adopted oldest animal in the shelter.")