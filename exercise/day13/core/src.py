from lib import common

class Student:

    def __init__(self,subjects={},name='',gender='male'):
        self.subjects = subjects
        self.name = name
        self.gender = gender

    def get_average_score(self):
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


class School:

    def __init__(self,info):
        self.students = {}
        for k, v in info.items():
            self.students[k] = (Student(subjects=v,name=k))

    def get_student_score(self,student_name,name=''):
        if student_name in self.students:
            if name == '':
                return self.students[student_name].get_all_subjects()
            else:
                return self.students[student_name].get_subject_score(name)

    def get_all_average_score(self):
        sum = 0
        for s in self.students.values():
            sum += s.get_average_score()
        return sum/len(self.students.values())

    def get_subject_scores(self,name):
        r = {}
        for s in self.students.values():
            r[s.name] = s.get_subject_score(name)
        return r

    def change_score(self,student_name,subject_name,score):
        if student_name in self.students:
            self.students[student_name].change_subject_score(name=subject_name,score=score)
            self.save()

    def add_score(self,student_name,subject_name,score):
        if student_name in self.students:
            self.students[student_name].add_subject(name=subject_name,score=score)
            self.save()

    def delete_score(self,student_name,subject_name):
        if student_name in self.students:
            self.students[student_name].delete_subject_score(name=subject_name)
            self.save()

    def save(self):
        all_students = {}
        for s in self.students.values():
            all_students[s.name] = s.get_all_subjects()
        common.save_db(all_students)

students = School(common.conn_db())

def run():
    while True:
        print('\n1. Get all average score\n2. Get student score\n3. Get subject score\n4. Get specific subject\n5. Change score\n6. Add score\n7. Delete score')

        choice = input('Your choice >>:')
        if choice == '1':
            print(students.get_all_average_score())
        elif choice == '2':
            name = input('student name >>:')
            print(students.get_student_score(student_name=name))
        elif choice == '3':
            name = input('subject name >>:')
            print(students.get_subject_scores(name))
        elif choice == '4':
            s_name = input('student name >>:')
            subject_name = input('subject name >>:')
            print(students.get_student_score(student_name=s_name,name=subject_name))
        elif choice == '5':
            s_name = input('student name >>:')
            subject_name = input('subject name >>:')
            score = input('score')
            students.change_score(student_name=s_name,subject_name=subject_name,score=score)
        elif choice == '6':
            s_name = input('student name >>:')
            subject_name = input('subject name >>:')
            score = input('score >>:')
            students.add_score(student_name=s_name, subject_name=subject_name, score=score)
        elif choice == '7':
            s_name = input('student name >>:')
            subject_name = input('subject name >>:')
            students.delete_score(student_name=s_name, subject_name=subject_name)