from helpers.funcs import get_group
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# date = timezone.now()
class Card(models.Model):
  id = models.AutoField(primary_key=True)
  card_number = models.CharField(max_length=19)
  card_serial = models.CharField(max_length=4)
  amount = models.CharField(max_length=999)
  issued_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{} -  {}, {}'.format(self.issued_date, self.card_serial, self.amount)
  

class SecurityQuestion(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.CharField(max_length=50)
  answer = models.CharField(max_length=50)
  
  def __str__(self):
    return '{} - {}'.format(self.id, self.question)

GENDER = (('male', 'Male'), ('female', 'Female'),)
class Profile (models.Model):
  fullname = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  address = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=100, blank=True)
  dob = models.DateField(blank=True, auto_now_add=True)
  gender = models.CharField(max_length=50, choices=GENDER, default='Male')
  user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
  question = models.ManyToManyField(to=SecurityQuestion, blank=True)
  card = models.OneToOneField(to=Card, on_delete=models.CASCADE, related_name='profile_card', blank=True, null=True)
  completed = models.BooleanField(default=False,null=True)
  
  def __str__(self):
    return str(self.user.username)
  
  @property
  def get_all_questions(self):
    questions = self.question.all()
    quest = []
    for q in questions:
      quest.append(q)
      
    return quest
  
  @property
  def get_user_groups(self):
    return self.user.groups.all()
  
  
  @property
  def is_completed_transaction(self):
    groups = self.get_user_groups
    print(groups)
    exist = [ g.name for g in groups if g.name == get_group('incompleted_transaction') ] != []

    return  exist

  
  
class Transaction(models.Model):
  amount = models.CharField(max_length=9999)
  profile = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE, null=True)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{} - {}'.format(self.profile, self.amount)
  
  
  @property
  def my_amount(self):
    return self.amount
  
  
  
