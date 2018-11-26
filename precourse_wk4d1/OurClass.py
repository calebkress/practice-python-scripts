### A rework of OurClass() from the lesson notes
# create basic class template for OurClass and instantiate our_class
class OurClass():
    def __init__(self, name, location, size=0, members=[]):
        self.name = name
        self.location = location
        self.size = size
        self.members = members
        self.at_capacity = self.check_if_at_capacity()

    def add_class_members(self, member):
        self.check_if_at_capacity()
        if self.at_capacity:
            print('Capacity Reached!!')
        else:
            self.size += 1
            self.members.append(member)

    def check_if_at_capacity(self):
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity

our_class = OurClass('Python', 'Austin')
print(our_class.name, our_class.location, our_class.size, our_class.members, our_class.at_capacity)

# create class for Member
class Member():
    def __init__(self, name, hair_color, birthdate, coding_level='beginner'):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = coding_level

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def get_coding_level(self):
        if self.num_lines_coded <= 100:
            self.coding_level = 'beginner'
        elif 100 < self.num_lines_coded <= 1000:
            self.coding_level = 'novice'
        elif 1000 < self.num_lines_coded <= 10000:
            self.coding_level = 'intermediate'
        else:
            self.coding_level = 'master'

    def add_coded_line(self, code):
        self.num_lines_coded += 1
        self.lines_of_code.append(code)
        self.get_coding_level()

# have OurClass and Member interact with one another
