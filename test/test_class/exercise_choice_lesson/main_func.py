#coding=utf-8
# @Author: wjn


import pickle

class Common:

    def write_txt(self,data,filepath):
        data = pickle.dumps(data)
        with open(filepath,'wb') as f:
            f.write(data)

    def read_txt(self,filepath):
        with open(filepath,'rb') as f:
            data = f.read()
        data = pickle.loads(data)
        return data


class School:
    lessons = []
    grades = []

    def __init__(self,name,locate):
        self.name = name
        self.locate= locate

    def school_info(self):
        return {'name':self.name,'locate':self.locate}

    def add_lesson(self,lesson):
        self.lesson = lesson
        School.lessons.append(lesson)
        Common.write_txt(self,School.lessons,'lessons.txt')

    def show_lesson(self):
        # print(School.lessons)
        ret = Common.read_txt(self,'lessons.txt')
        print('lessons:',ret)

    def add_grade(self,grade):
        self.grade = grade
        School.grades.append(grade)
        Common.write_txt(self,School.grades,'grades.txt')

    def show_grade(self):
        # print(School.grades)
        ret = Common.read_txt(self, 'grades.txt')
        print('grades:', ret)


class Lesson:
    def __init__(self,name,cost,time,school,teacher):
        self.name = name
        self.cost = cost
        self.time = time
        self.school = school
        self.teacher = teacher

    def lesson_info(self):
        return {'name':self.name,'cost':self.cost,'time':self.time,'school':self.school,
                'teacher':self.teacher}

class Teacher:
    teachers = []

    def __init__(self,name,school,balance):
        self.name = name
        self.balance = balance
        self.school = school

    def teacher_info(self):
        return {'name':self.name,'balance':self.balance,'school':self.school}

    def add_teacher(self,teacher):
        self.teacher = teacher
        Teacher.teachers.append(teacher)
        Common.write_txt(self,Teacher.teachers,'teachers.txt')

    def show_teacher(self):
        ret = Common.read_txt(self,'teachers.txt')
        print('teacher:',ret)


class Grade:
    def __init__(self,name,teacher,lesson):
        self.name = name
        self.teacher = teacher
        self.lesson = lesson

    def grade_info(self):
        return {'name':self.name,'teacher':self.teacher,'lesson':self.lesson}

if __name__ == '__main__':

    bjsch_obj = School('北京大学','北京')
    shsch_obj = School('上海大学','上海')

    wjn_teacher = Teacher('王佳宁','北京大学',1000)
    wjn_teacher.add_teacher(wjn_teacher.teacher_info())
    wjn_teacher.show_teacher()
    ym_teacher = Teacher('姚明','上海大学',1000)

    # 增加课程
    bj_linux_less = Lesson('linux',100,'2h',bjsch_obj.name,wjn_teacher.name)
    sh_linux_less = Lesson('linux',100,'2h',shsch_obj.name,ym_teacher.name)
    bjsch_obj.add_lesson(bj_linux_less.lesson_info())
    bjsch_obj.show_lesson()

    # 增加班级
    grade1 = Grade('grade1',wjn_teacher.name,bj_linux_less.name)
    bjsch_obj.add_grade(grade1.grade_info())
    bjsch_obj.show_grade()