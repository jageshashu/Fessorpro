
# class-> blueprint of object
# object-> instance of class
# attribute-> variable inside class
# class attribute-> variable inside class but outside method
# instance attribute-> variable inside class but inside method
# method-> function inside class

# class attribute and class variable are same

# Object oriented programming-> we can create our own data type using class and object
# class attribute
class student:
    school_name="ABC School"  # class attribute
    dress_code="Blue"  # class variable

s1=student()                            # object of class Student
print(s1.school_name)                   # accessing class using object

s2=student()                            # object of class Student
print(s2.dress_code)                    # accessing class using object

# Instance attribute
class student:
    school_name="ABC School"            # class attribute
    dress_code="Blue"                   # class variable

    def __init__(self,name,email,r):
        self.name=name                  # instance attribute
        self.email=email                # instance attribute
        self.roll_no=r                  # instance attribute
    

s1=student('sam','sam@gmail.com',50)    # object of class Student
print(s1.school_name)                   # accessing class using object
print(s1.name)                          # accessing instance attribute using object

s2=student('john','john@gmail.com',60)  # object of class Student
print(s2.dress_code)                    # accessing class using object
print(s2.name)                          # accessing instance attribute using object


class student:
    school_name="ABC School"            # class attribute
    dress_code="Blue"                   # class variable

    def __init__(self,name,email,r):
        self.name=name                  # instance attribute
        self.email=email                # instance attribute
        self.roll_no=r                  # instance attribute

    def get_student_details(self):
        print(f'studentname is {self.name} and email is {self.email} and roll no is {self.roll_no}')

s1=student('sam','sam@gmail.com',50)    # object of class Student
print(s1.school_name)                   # accessing class using object
print(s1.name)                          # accessing instance attribute using object

s2=student('john','john@gmail.com',60)  # object of class Student
print(s2.dress_code)                    # accessing class using object
print(s2.name)                          # accessing instance attribute using object

s1.get_student_details()                # accessing method using object
s2.get_student_details()                # accessing method using object


# structural programming-> we use built in data type list, dict, set, tuple to store data and we use function to perform operation on data
student_info={'school_name':'ABC School','dress_code':'Blue','students':
              [{'name':'sam','email':'sam@gmail.com','roll_no':50},
                {'name':'john','email':'john@gmail.com','roll_no':60},
                {}
                ]}