from django.db import models
class RegistrationForm(models.Model):
  username=models.EmailField()
  password=models.CharField(max_length=20)
  cpassword=models.CharField(max_length=20)  
class LoginForm(models.Model):
  Username=models.EmailField()
  password=models.CharField(max_length=50)
class Product(models.Model):
  pname=models.CharField(max_length=50)
  pcost=models.FloatField()
  pdetails=models.CharField(max_length=100)
  cat=models.IntegerField()
  is_active=models.BooleanField(default=True)
  pimage=models.ImageField(upload_to="image" )
  def __str__(self):
    return self.pname
