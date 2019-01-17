class Student:

    def __init__(self,subjects={},name='',gender='male'):
        self.subjects = subjects
        self.name = name
        self.gender = gender

    def average_score(self):
        sum = 0
        for k,v in self.subjects.items():
            sum += v
        return (sum/len(self.subjects))

    def get_subject_score(self,subject_name):
        return self.subjects.get(subject_name)

    def add_subject(self,name,score):
        self.subjects[name] = score

    def get_all_subjects(self):
        return self.subjects

    def change_subject_score(self,name,score):
        self.subjects[name] = score

    def delete_subject_score(self,name):
        if name in self.subjects:
            self.subjects.pop(name)
