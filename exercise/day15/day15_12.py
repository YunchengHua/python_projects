class DeepsharePeople:
    school = 'deepshare'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def f1(self):
        print('爹的f1')


class DeepshareTeacher(DeepsharePeople):

    def modify_score(self):
        print('teacher %s is modifying score' % self.name)

    def f1(self):
        print('儿子的f1')


tea1 = DeepshareTeacher('albert', 18, 'male')
tea1.f1()

