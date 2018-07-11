#instantiste a new Dog and print out the resultd of making it speak
from dog import Dog
from pet import Pet

goldendoodle = Dog("Goldendoodle")

aj = Pet("AJ", goldendoodle)

aj.set_owner("The Landsbergs", "310-882-3105")

print(aj)

print(f"What's that girl? {goldendoodle.speak()} Timmy's in the well? Oh no!")