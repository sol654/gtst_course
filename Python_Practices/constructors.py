class human:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def running(self):
        return "I can run!"
    def dancing(self):
        return "I can dance!"
    def eating(self):
        return "I can eat!"
human1 = human("Solace", "21", "CS")
print(f"My name is  {human1.name}\n I am {human1.age} years old.\n I am {human1.grade} student.")
print(f"My skills are: {human.running(human1)} , {human.dancing(human1)} and {human.eating(human1)}\n Thank you!")