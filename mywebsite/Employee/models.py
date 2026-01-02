from django.db import models

# Create your models here.
class employee(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Images')
    e_mail = models.CharField(max_length=50, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.First_name+ " " + self.Last_name
                            