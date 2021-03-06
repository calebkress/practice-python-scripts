### A rework of OurClass() from the lesson notes
# create basic class template for OurClass and instantiate our_class
class OurClass():
    def __init__(self, name, location, members, instructors):
        self.name = name
        self.location = location
        self.members = members
        self.instructors = instructors
        self.size = len(self.members)
        self.at_capacity = self.check_if_at_capacity()
        self.num_questions_asked = self.get_num_questions_asked()
        self.total_lines_code = self.get_num_lines_code()
        self.num_questions_answered = self.get_num_questions_answered()
        self.questions_remain = self.check_unanswered_questions()

    def add_class_members(self, member):
        if self.at_capacity:
            print('Capacity Reached!!')
        else:
            self.size += 1
            self.members.append(member)
        self.check_if_at_capacity()

    def check_if_at_capacity(self):
        if self.size >= 10:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity

    def get_num_questions_asked(self):
        total_qs = 0
        for member in self.members:
            total_qs += len(member.questions_asked)
        return total_qs

    def get_num_lines_code(self):
        total_lines = 0
        for member in self.members:
            total_lines += member.num_lines_coded
        return total_lines

    def get_num_questions_answered(self):
        total_answered = 0
        for instructor in self.instructors:
            total_answered += len(instructor.questions_answered)
        return total_answered

    def check_unanswered_questions(self):
        if self.num_questions_asked == self.num_questions_answered:
            return False
        else:
            return True

# create class for Member
class Member():
    def __init__(self, name, num_lines_coded):
        self.name = name
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = int(num_lines_coded)
        self.coding_level = self.get_coding_level()

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def get_coding_level(self):
        if self.num_lines_coded <= 100:
            return 'beginner'
        elif 100 < self.num_lines_coded <= 1000:
            return 'novice'
        elif 1000 < self.num_lines_coded <= 10000:
            return 'intermediate'
        else:
            return 'master'

    def add_coded_line(self, code):
        self.num_lines_coded += 1
        self.lines_of_code.append(code)
        self.get_coding_level()

# create class for Instructor
class Instructor():
    def __init__(self, name, questions_answered=[]):
        self.name = name
        self.questions_answered = questions_answered

    def add_question_answered(self, question):
        self.questions_answered.append(question)

###### test class interactions
# create test functions
def test_OurClass(ourclass):
    print(ourclass.name, ourclass.location, ourclass.size, ourclass.at_capacity, ourclass.num_questions_asked, ourclass.total_lines_code, ourclass.num_questions_answered, ourclass.questions_remain)

def test_Member(member):
    print(member.name, member.questions_asked, member.lines_of_code, member.num_lines_coded, member.coding_level)

def test_Instructor(instructor):
    print(instructor.name, instructor.questions_answered)

# define + test members
caleb = Member('Caleb', 5000)
test_Member(caleb)
noble = Member('Noble', 5000)
test_Member(noble)
ross = Member('Ross', 12000)
test_Member(ross)
cameron = Member('Cameron', 11000)
test_Member(cameron)
carter = Member('Carter', 5000)
test_Member(carter)
josh = Member('Josh', 999)
test_Member(josh)
clay = Member('Clay', 12000)
test_Member(clay)
ben = Member('Ben', 999)
test_Member(ben)
ceci = Member('Ceci', 15000)
test_Member(ceci)
class_members = [caleb, noble, ross, cameron, carter, josh, clay, ben, ceci]

# define + test instructors
patrick = Instructor('Patrick', ['What\'s a loop?', 'How do I console.log?'])
test_Instructor(patrick)
caleb_instructor = Instructor('Caleb', ['What does this function do?'])
test_Instructor(caleb_instructor)
class_instructors = [patrick, caleb_instructor]

# define + test OurClass
our_class = OurClass('HRATX30', 'Austin', class_members, class_instructors)
test_OurClass(our_class)

# use a few methods
caleb.add_question_asked('Does this work?')
caleb.add_question_asked('What\'s a loop?')
caleb.add_question_asked('How do I console.log?')
caleb.add_question_asked('What does this function do?')
test_Member(caleb)
# our_class = OurClass('HRATX30', 'Austin', class_members, class_instructors)
test_OurClass(our_class)
josh.add_coded_line('line of code')
test_Member(josh)
# our_class = OurClass('HRATX30', 'Austin', class_members, class_instructors)
test_OurClass(our_class)

# add a new member
tim = Member('Tim', 99)
test_Member(tim)
our_class.add_class_members(tim)
test_OurClass(our_class)
