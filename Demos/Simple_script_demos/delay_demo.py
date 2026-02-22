import time

class Student:
    def take_nap(self, seconds):
        print("A 5 second delay will now occur.")
        time.sleep(seconds)
        print("The 5 second delay has concluded!")

student = Student()
student.take_nap(5)
    