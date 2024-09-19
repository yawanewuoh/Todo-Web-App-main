from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
      user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
      title= models.CharField(max_length=100)
      description= models.TextField(null=True, blank=True)
      complete= models.BooleanField(default=False)
      description= models.TextField(null=True, blank=True)
      create= models.DateTimeField(auto_now_add=True)

      def __str__(self):
         return self.title

      class Meta:
         ordering=['complete']

class User_wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"Wallet for {self.user.username} with balance {self.balance}"



