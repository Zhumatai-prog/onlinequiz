from django.db import models
from multiselectfield import MultiSelectField


from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    #marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    option5 = models.CharField(max_length=200, null=True, blank=True)

    # Вопросы в которых нужно быбрать картинку
    picture1 = models.ImageField(upload_to='images', null=True, blank=True)
    picture2 = models.ImageField(upload_to='images', null=True, blank=True)
    picture3 = models.ImageField(upload_to='images', null=True, blank=True)
    picture4 = models.ImageField(upload_to='images', null=True, blank=True)
    picture5 = models.ImageField(upload_to='images', null=True, blank=True)

    cat=(('Option1','Option1'),
         ('Option2','Option2'),
         ('Option3','Option3'),
         ('Option4','Option4'),
         ('Option5','Option5'),
         ('Picture1','Picture1'),
         ('Picture2','Picture2'),
         ('Picture3','Picture3'),
         ('Picture4','Picture4'),
         ('Picture5','Picture5'))

    answer = MultiSelectField(max_length=200,choices=cat)



class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
